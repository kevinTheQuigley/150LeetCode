import pytest

from leetcode_py import logged_test

try:
    from .helpers import assert_check_valid_string, run_check_valid_string
except ImportError:
    from helpers import assert_check_valid_string, run_check_valid_string
try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestValidParenthesisString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()", True),
            ("(*)", True),
            ("(*))", True),
            ("(", False),
            (")", False),
            ("*", True),
            ("***", True),
            ("((*)", True),
            ("())", False),
            ("(()", False),
            ("(((******))", True),
            ("(*()", True),
            (")*", False),
            ("(()*", True),
        ],
    )
    def test_check_valid_string(self, s: str, expected: bool):
        result = run_check_valid_string(Solution, s)
        assert_check_valid_string(result, expected)
