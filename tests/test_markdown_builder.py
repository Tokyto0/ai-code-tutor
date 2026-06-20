from utils.markdown_builder import MarkdownReportBuilder


def test_report_navigation_and_collapsible_sections():
    builder = MarkdownReportBuilder(problem_title="????")
    builder.set_project_info("??4", "AI????????")
    builder.add_error_diagnosis("### ????\n??", "### ????\n??")

    report = builder.build()

    assert 'class="report-nav"' in report
    assert '<details class="report-section" open>' in report
    assert 'id="section-' in report
    assert 'href="#section-' in report
    assert 'report-section-summary' in report


def test_report_places_sandbox_before_error_diagnosis_with_updated_numbers():
    builder = MarkdownReportBuilder(problem_title="Order")
    builder.add_ast_analysis("AST")
    builder.add_sandbox_results([
        {
            "input": "nums = [1]",
            "expected": "1",
            "actual": "1",
            "passed": True,
            "error": "",
        }
    ])
    builder.add_error_diagnosis("DIAGNOSIS", "FIX")

    report = builder.build()

    ast_pos = report.index("一、代码结构分析")
    sandbox_pos = report.index("二、运行验证")
    diagnosis_pos = report.index("三、错误诊断")
    fix_pos = report.index("四、修复建议")

    assert ast_pos < sandbox_pos < diagnosis_pos < fix_pos
