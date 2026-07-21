import pytest

from leetcode_py import logged_test

try:
    from .helpers import assert_generate_parenthesis, run_generate_parenthesis
except ImportError:
    from helpers import assert_generate_parenthesis, run_generate_parenthesis
try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestGenerateParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, ["()"]),
            (2, ["(())", "()()"]),
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
            (
                4,
                [
                    "(((())))",
                    "((()()))",
                    "((())())",
                    "((()))()",
                    "(()(()))",
                    "(()()())",
                    "(()())()",
                    "(())(())",
                    "(())()()",
                    "()((()))",
                    "()(()())",
                    "()(())()",
                    "()()(())",
                    "()()()()",
                ],
            ),
            (0, [""]),
            (
                5,
                [
                    "((((()))))",
                    "(((()())))",
                    "(((())()))",
                    "(((()))())",
                    "(((())))()",
                    "((()(())))",
                    "((()()()))",
                    "((()())())",
                    "((()()))()",
                    "((())(()))",
                    "((())()())",
                    "((())())()",
                    "((()))(())",
                    "((()))()()",
                    "(()((())))",
                    "(()(()()))",
                    "(()(())())",
                    "(()(()))()",
                    "(()()(()))",
                    "(()()()())",
                    "(()()())()",
                    "(()())(())",
                    "(()())()()",
                    "(())((()))",
                    "(())(()())",
                    "(())(())()",
                    "(())()(())",
                    "(())()()()",
                    "()(((())))",
                    "()((()()))",
                    "()((())())",
                    "()((()))()",
                    "()(()(()))",
                    "()(()()())",
                    "()(()())()",
                    "()(())(())",
                    "()(())()()",
                    "()()((()))",
                    "()()(()())",
                    "()()(())()",
                    "()()()(())",
                    "()()()()()",
                ],
            ),
            pytest.param(1, ["()"], id="dup1"),
            pytest.param(2, ["(())", "()()"], id="dup2"),
            pytest.param(3, ["((()))", "(()())", "(())()", "()(())", "()()()"], id="dup3a"),
            pytest.param(3, ["((()))", "(()())", "(())()", "()(())", "()()()"], id="dup3b"),
            pytest.param(3, ["((()))", "(()())", "(())()", "()(())", "()()()"], id="dup3c"),
        ],
    )
    def test_generate_parenthesis(self, n: int, expected: list[str]):
        result = run_generate_parenthesis(Solution, n)
        assert_generate_parenthesis(result, expected)
