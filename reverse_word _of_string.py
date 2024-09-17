# s = "the sky is blue"
# L = s.split(" ")
# print(L)
# L = L[::-1]
# print(L)
# print(" ".join(L))

class Solution:
    def reverseWords(self, s: str) -> str:
        import re

        L = s.split(" ")
        
        L = L[::-1]
        res = re.sub(' +', ' ', " ".join(L).strip())
        return str(res)