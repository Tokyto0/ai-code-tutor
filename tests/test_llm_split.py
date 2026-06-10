from analyzer.llm_diagnosis import LLMDiagnosis


def test_split_diagnosis_response_moves_fix_sections():
    response = "\n".join(
        [
            "### 1. Error Location",
            "LOCATION_CONTENT",
            "",
            "### 2. Cause Analysis",
            "CAUSE_CONTENT",
            "",
            "### 3. \u4fee\u590d\u5efa\u8bae",
            "FIX_CONTENT",
            "",
            "### 4. Knowledge Summary",
            "SUMMARY_CONTENT",
        ]
    )

    error_analysis, fix_suggestion = LLMDiagnosis()._split_diagnosis_response(response)

    assert "LOCATION_CONTENT" in error_analysis
    assert "CAUSE_CONTENT" in error_analysis
    assert "FIX_CONTENT" not in error_analysis
    assert "SUMMARY_CONTENT" not in error_analysis
    assert "FIX_CONTENT" in fix_suggestion
    assert "SUMMARY_CONTENT" in fix_suggestion


def test_split_diagnosis_response_keeps_text_when_fix_heading_missing():
    response = """### 1. Error Location
LOCATION_CONTENT

### 2. Cause Analysis
CAUSE_CONTENT
"""

    error_analysis, fix_suggestion = LLMDiagnosis()._split_diagnosis_response(response)

    assert error_analysis == response.strip()
    assert fix_suggestion == ""
