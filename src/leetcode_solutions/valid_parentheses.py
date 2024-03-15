"""
Solution for Valid Parentheses problem
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    """
    Solution for Valid Parentheses problem
    """

    def isValid(self, s: str) -> bool:
        """
        Checks if string is valid based on parentheses

        Args:
            s (str): String to check

        Returns:
            bool: True if valid, False otherwise
        """
        opening_brackets = {"(", "{", "["}
        bracket_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False

        return not stack
