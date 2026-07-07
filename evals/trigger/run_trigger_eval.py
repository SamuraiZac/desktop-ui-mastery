#!/usr/bin/env python3
"""Measure whether the skill's frontmatter description triggers when it should.

For each query in queries.json, plants a probe command whose description is the
skill's description, runs `claude -p <query>`, and watches the event stream for
whether the probe gets invoked. Reports precision / recall / accuracy.

Each run gets its own throwaway project directory. This is load-bearing: with a
shared directory, concurrent workers see each other's identically-described
probes and pick one at random, collapsing recall to ~1/N regardless of how good
the description is. For the same reason, UNINSTALL OR DISABLE the real
desktop-ui-mastery plugin before running — an installed copy shadows the probe
and every positive query scores as a miss.

Usage:
    python3 run_trigger_eval.py [--skill-md ../../skills/desktop-ui-mastery/SKILL.md]
                                [--queries queries.json] [--runs 3] [--workers 8]
                                [--model claude-sonnet-5] [--timeout 90]

Requires the `claude` CLI on PATH and Python 3.10+. No third-party packages.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def read_description(skill_md: Path) -> str:
    text = skill_md.read_text()
    match = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        sys.exit(f"No frontmatter found in {skill_md}")
    desc_match = re.search(r"^description:\s*(.+?)(?=^\w+:|\Z)", match.group(1), re.DOTALL | re.MULTILINE)
    if not desc_match:
        sys.exit(f"No description in {skill_md} frontmatter")
    return " ".join(desc_match.group(1).split())


def run_one(query: str, description: str, timeout: int, model: str | None) -> bool:
    """One claude -p run in an isolated project dir. True iff the probe fired."""
    probe = f"trigger-probe-{uuid.uuid4().hex[:8]}"
    work_dir = Path(tempfile.mkdtemp(prefix=f"{probe}-"))
    commands_dir = work_dir / ".claude" / "commands"
    try:
        commands_dir.mkdir(parents=True)
        indented = "\n  ".join(description.split("\n"))
        (commands_dir / f"{probe}.md").write_text(
            f"---\ndescription: |\n  {indented}\n---\n\n# {probe}\n\nThis skill handles: {description}\n"
        )

        cmd = ["claude", "-p", query, "--output-format", "stream-json", "--verbose"]
        if model:
            cmd += ["--model", model]
        # CLAUDECODE guards against interactive nesting; harmless for subprocesses.
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            cwd=work_dir, env=env, text=True,
        )
        try:
            for line in proc.stdout:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") == "assistant":
                    for block in event.get("message", {}).get("content", []):
                        if block.get("type") != "tool_use":
                            continue
                        name, tool_input = block.get("name", ""), block.get("input", {})
                        if name == "Skill":
                            return probe in tool_input.get("skill", "")
                        if name == "Read":
                            return probe in tool_input.get("file_path", "")
                        return False  # first tool call went elsewhere
                elif event.get("type") == "result":
                    return False
            return False
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait()
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


def main() -> None:
    here = Path(__file__).parent
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--skill-md", type=Path, default=here / "../../skills/desktop-ui-mastery/SKILL.md")
    ap.add_argument("--queries", type=Path, default=here / "queries.json")
    ap.add_argument("--runs", type=int, default=3, help="runs per query (majority decides)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument("--timeout", type=int, default=90)
    args = ap.parse_args()

    description = read_description(args.skill_md.resolve())
    queries = json.loads(args.queries.read_text())

    jobs = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, item in enumerate(queries):
            for r in range(args.runs):
                fut = pool.submit(run_one, item["query"], description, args.timeout, args.model)
                jobs[fut] = i
        hits = [0] * len(queries)
        for fut in as_completed(jobs):
            if fut.result():
                hits[jobs[fut]] += 1

    tp = fp = tn = fn = 0
    for item, h in zip(queries, hits):
        fired = h > args.runs / 2
        expected = item["should_trigger"]
        ok = fired == expected
        tp += fired and expected
        fp += fired and not expected
        tn += not fired and not expected
        fn += not fired and expected
        print(f"[{'PASS' if ok else 'FAIL'}] {h}/{args.runs} expected={expected}: {item['query'][:70]}")

    total = len(queries)
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    print(f"\naccuracy {(tp + tn)}/{total}  precision {precision:.0%}  recall {recall:.0%}")
    sys.exit(0 if fp == 0 and fn == 0 else 1)


if __name__ == "__main__":
    main()
