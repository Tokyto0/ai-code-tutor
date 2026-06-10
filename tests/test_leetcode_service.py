from services.leetcode_service import normalize_leetcode_slug


def test_normalize_leetcode_slug_accepts_slug_and_urls():
    assert normalize_leetcode_slug("two-sum") == "two-sum"
    assert normalize_leetcode_slug("https://leetcode.cn/problems/two-sum/") == "two-sum"
    assert normalize_leetcode_slug("https://leetcode.com/problems/two-sum/description/") == "two-sum"
