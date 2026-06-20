"""Formatting and parsing helpers for sandbox test cases."""

from __future__ import annotations

import re
from typing import Iterable


_INPUT_HEADER = re.compile(
    r"(?im)^={3,}\s*(?:测试用例|TEST\s+CASE)\s*(\d+)\s*={3,}\s*$"
)
_EXPECTED_HEADER = re.compile(
    r"(?im)^={3,}\s*(?:期望输出|EXPECTED\s+OUTPUT)\s*(\d+)\s*={3,}\s*$"
)


def format_examples_for_ui(examples: Iterable[dict]) -> tuple[str, str]:
    """Render LeetCode examples as two strictly numbered UI fields."""
    complete = [
        {
            "input": str(example.get("input", "")).strip(),
            "expected": str(example.get("output", "")).strip(),
        }
        for example in examples
        if str(example.get("input", "")).strip()
        and str(example.get("output", "")).strip()
    ]
    if not complete:
        return "", ""

    if len(complete) == 1:
        return complete[0]["input"], complete[0]["expected"]

    input_blocks = []
    expected_blocks = []
    for index, example in enumerate(complete, 1):
        input_blocks.append(f"===== 测试用例 {index} =====\n{example['input']}")
        expected_blocks.append(f"===== 期望输出 {index} =====\n{example['expected']}")
    return "\n\n".join(input_blocks), "\n\n".join(expected_blocks)


def parse_test_cases(test_input: str, test_expected: str) -> tuple[list[dict[str, str]], str]:
    """Parse single or numbered test cases and enforce one-to-one pairing."""
    input_text = (test_input or "").strip()
    expected_text = (test_expected or "").strip()

    if not input_text and not expected_text:
        return [], ""
    if not input_text or not expected_text:
        return [], "测试输入和期望输出必须同时填写。"

    input_blocks = _parse_numbered_blocks(input_text, _INPUT_HEADER)
    expected_blocks = _parse_numbered_blocks(expected_text, _EXPECTED_HEADER)

    if input_blocks is None and expected_blocks is None:
        return [{"input": input_text, "expected": expected_text}], ""
    if input_blocks is None or expected_blocks is None:
        return [], "多组测试必须同时使用“测试用例 N”和“期望输出 N”编号格式。"

    input_ids = set(input_blocks)
    expected_ids = set(expected_blocks)
    if input_ids != expected_ids:
        missing_outputs = sorted(input_ids - expected_ids)
        missing_inputs = sorted(expected_ids - input_ids)
        details = []
        if missing_outputs:
            details.append(f"缺少期望输出：{', '.join(map(str, missing_outputs))}")
        if missing_inputs:
            details.append(f"缺少测试输入：{', '.join(map(str, missing_inputs))}")
        return [], "测试用例与期望输出编号不匹配；" + "；".join(details) + "。"

    ordered_ids = sorted(input_ids)
    return [
        {"input": input_blocks[index], "expected": expected_blocks[index]}
        for index in ordered_ids
    ], ""


def _parse_numbered_blocks(text: str, header_pattern: re.Pattern) -> dict[int, str] | None:
    matches = list(header_pattern.finditer(text))
    if not matches:
        return None

    blocks: dict[int, str] = {}
    for position, match in enumerate(matches):
        number = int(match.group(1))
        start = match.end()
        end = matches[position + 1].start() if position + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        if number in blocks or not content:
            return {}
        blocks[number] = content
    return blocks
