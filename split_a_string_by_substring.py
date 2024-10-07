class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
            # Check if str1 + str2 == str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of the two strings
        gcd_length = math.gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of either string up to the GCD length
        return str1[:gcd_length]
        