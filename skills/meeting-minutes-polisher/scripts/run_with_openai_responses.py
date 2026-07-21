#!/usr/bin/env python3
"""
Run the meeting-minutes workflow with an OpenAI-compatible Responses API.

This script does not ship with a real API key. Users must provide their own
OPENAI_API_KEY via environment variables.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from export_minutes_to_docx import build_document


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_workflow_instructions() -> str:
    skill_dir = Path(__file__).resolve().parents[1]
    skill_md = read_text(skill_dir / "SKILL.md")
    style_guide = read_text(skill_dir / "references" / "style-guide.md")
    return (
        "You are running the Meeting Minutes Polisher workflow.\n\n"
        "Follow the workflow rules and style guide below exactly.\n\n"
        "[SKILL]\n"
        f"{skill_md}\n\n"
        "[STYLE GUIDE]\n"
        f"{style_guide}"
    )


def build_user_prompt(company: str, transcript: str) -> str:
    return (
        "请处理下面的会议转写，并严格遵守workflow要求。\n"
        f"公司名称：{company}\n\n"
        "要求：\n"
        "1. 不擅自删减内容；\n"
        "2. 不要出现莫名其妙的空格；\n"
        "3. 数字之间不要有逗号；\n"
        "4. 最后输出完整会议纪要和要点总结；\n"
        "5. 请自检是否漏信息、误改数字、误改专业名词。\n\n"
        "会议转写如下：\n"
        f"{transcript}"
    )


def call_responses_api(base_url: str, api_key: str, model: str, instructions: str, user_prompt: str) -> str:
    url = f"{base_url.rstrip('/')}/responses"
    payload = {
        "model": model,
        "store": False,
        "input": [
            {"role": "developer", "content": instructions},
            {"role": "user", "content": user_prompt},
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        body = json.loads(response.read().decode("utf-8"))
    output_text = body.get("output_text", "").strip()
    if output_text:
        return output_text
    raise RuntimeError("API returned no output_text.")


def save_outputs(company: str, content: str, output_text: Path | None, output_docx: Path | None) -> None:
    if output_text is not None:
        output_text.parent.mkdir(parents=True, exist_ok=True)
        output_text.write_text(content, encoding="utf-8")

    if output_docx is not None:
        output_docx.parent.mkdir(parents=True, exist_ok=True)
        document = build_document(company, content)
        document.save(output_docx)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run meeting-minutes workflow with OpenAI Responses API.")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--transcript", required=True, help="Path to transcript text file")
    parser.add_argument("--output-text", help="Path to save the polished memo as text")
    parser.add_argument("--output-docx", help="Path to save the polished memo as docx")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Missing OPENAI_API_KEY environment variable.", file=sys.stderr)
        return 1

    model = os.getenv("OPENAI_MODEL", "gpt-5")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

    transcript = read_text(Path(args.transcript))
    instructions = load_workflow_instructions()
    user_prompt = build_user_prompt(args.company, transcript)

    try:
        output = call_responses_api(base_url, api_key, model, instructions, user_prompt)
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(f"API request failed: {exc.code} {exc.reason}\n{error_body}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"API request failed: {exc}", file=sys.stderr)
        return 1

    output_text = Path(args.output_text) if args.output_text else None
    output_docx = Path(args.output_docx) if args.output_docx else None
    save_outputs(args.company, output, output_text, output_docx)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
