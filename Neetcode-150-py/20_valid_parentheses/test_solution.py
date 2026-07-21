import pytest

from leetcode_py import logged_test

try:
    from .helpers import assert_is_valid, run_is_valid
except ImportError:
    from helpers import assert_is_valid, run_is_valid
try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestValidParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([])", True),
            ("([)]", False),
            ("", True),
            ("(", False),
            (")", False),
            ("{[()]}", True),
            ("{[(])}", False),
            ("((", False),
            ("))", False),
            ("([{}])", True),
            ("([{]})", False),
            ("{[}]", False),
            ("((()))", True),
            ("((())", False),
            ("(){}[]", True),
            ("{[(", False),
            ("]})", False),
        ],
    )
    def test_is_valid(self, s: str, expected: bool):
        result = run_is_valid(Solution, s)
        assert_is_valid(result, expected)
