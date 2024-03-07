"""
Solution for String Encode Decode problem
"""

# import ast
from typing import List


class Solution:
    """
    Solution for String Encode Decode problem
    """

    delim = "#"

    @staticmethod
    def encode(strs: List[str]) -> str:
        """
        Encode a list of strings to a single string.

        Args:
            strs (List[str]): List of strings
        Returns:
            str: Encoded string
        """
        # return str(strs)
        return "".join(str(len(s)) + Solution.delim + s for s in strs)

    @staticmethod
    def decode(s: str) -> List[str]:
        """
        Decode a single string to a list of strings.

        Args:
            s (str): Encoded string
        Returns:
            List[str]: List of strings
        """
        # return ast.literal_eval(s)
        decoded_strs = []

        i = 0
        while i < len(s):
            delim_index = s.find(Solution.delim, i)
            str_len = int(s[i:delim_index])
            i = delim_index + str_len + 1
            decoded_str = s[delim_index + 1 : i]
            decoded_strs.append(decoded_str)

        return decoded_strs
