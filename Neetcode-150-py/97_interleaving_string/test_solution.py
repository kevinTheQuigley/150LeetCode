import pytest

from leetcode_py import logged_test

try:
    from .helpers import assert_is_interleave, run_is_interleave
except ImportError:
    from helpers import assert_is_interleave, run_is_interleave
try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestInterleavingString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, s3, expected",
        [
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("", "", "", True),
            ("", "", "a", False),
            ("a", "", "a", True),
            ("", "b", "b", True),
            ("a", "b", "ab", True),
            ("a", "b", "ba", True),
            ("a", "b", "a", False),
            ("ab", "cd", "acbd", True),
            ("ab", "cd", "abcd", True),
            ("ab", "cd", "cdab", True),
            ("ab", "cd", "acdb", True),
            ("aa", "ab", "aaab", True),
            ("aa", "ab", "aaba", True),
            ("abc", "def", "abcdef", True),
            ("abc", "def", "adbecf", True),
            ("abc", "def", "defabc", True),
        ],
    )
    def test_is_interleave(self, s1: str, s2: str, s3: str, expected: bool):
        result = run_is_interleave(Solution, s1, s2, s3)
        assert_is_interleave(result, expected)
