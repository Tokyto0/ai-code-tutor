from analyzer.sandbox import SandboxRunner
from services.test_case_service import format_examples_for_ui, parse_test_cases


def test_format_and_parse_multiple_examples_strictly_pairs_by_number():
    examples = [
        {"input": 's = "aa"\np = "a"', "output": "false"},
        {"input": 's = "aa"\np = "a*"', "output": "true"},
        {"input": 's = "ab"\np = ".*"', "output": "true"},
    ]

    test_input, test_expected = format_examples_for_ui(examples)
    parsed, error = parse_test_cases(test_input, test_expected)

    assert "===== 测试用例 1 =====" in test_input
    assert "===== 测试用例 3 =====" in test_input
    assert "===== 期望输出 1 =====" in test_expected
    assert parsed == [
        {"input": 's = "aa"\np = "a"', "expected": "false"},
        {"input": 's = "aa"\np = "a*"', "expected": "true"},
        {"input": 's = "ab"\np = ".*"', "expected": "true"},
    ]
    assert error == ""


def test_parse_test_cases_keeps_single_case_backward_compatible():
    parsed, error = parse_test_cases("nums = [2,7]\ntarget = 9", "[0,1]")

    assert parsed == [{"input": "nums = [2,7]\ntarget = 9", "expected": "[0,1]"}]
    assert error == ""


def test_parse_test_cases_rejects_mismatched_numbered_groups():
    parsed, error = parse_test_cases(
        "===== 测试用例 1 =====\na = 1\n\n===== 测试用例 2 =====\na = 2",
        "===== 期望输出 1 =====\n1",
    )

    assert parsed == []
    assert "缺少期望输出：2" in error


def test_multiple_numbered_cases_run_as_independent_sandbox_calls():
    code = """
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first = bool(s) and p[0] in {s[0], "."}
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (
                first and self.isMatch(s[1:], p)
            )
        return first and self.isMatch(s[1:], p[1:])
"""
    test_input, test_expected = format_examples_for_ui(
        [
            {"input": 's = "aa"\np = "a"', "output": "false"},
            {"input": 's = "aa"\np = "a*"', "output": "true"},
            {"input": 's = "ab"\np = ".*"', "output": "true"},
        ]
    )
    test_cases, error = parse_test_cases(test_input, test_expected)
    runner = SandboxRunner(timeout=2, max_output=1024)
    try:
        results = runner.run_tests(code, test_cases)
    finally:
        runner.cleanup()

    assert error == ""
    assert len(results) == 3
    assert [result.actual_output.strip() for result in results] == ["False", "True", "True"]
    assert [result.passed for result in results] == [True, True, True]
