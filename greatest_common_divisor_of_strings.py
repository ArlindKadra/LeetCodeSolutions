class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        str1_length: int = len(str1)
        str2_length: int = len(str2)

        if len(str1) < len(str2):
            target_str: str = str1
        else:
            target_str: str = str2

        target_length: int = len(target_str)

        for i in range(target_length - 1, -1, -1):

            possible_overlap = target_str[0:i + 1]
            multiplicative_factor_str1  = int(str1_length / (i + 1))
            multiplicative_factor_str2 = int(str2_length / (i + 1))
            if possible_overlap * multiplicative_factor_str1 == str1:
                if possible_overlap * multiplicative_factor_str2 == str2:
                    return possible_overlap

        return ""
