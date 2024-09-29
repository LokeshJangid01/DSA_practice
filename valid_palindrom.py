"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: s = "race a car"
Output: false


"""


#         while left < right and not s[left].isalnum():
#             left += 1

def is_palindrome(s):
    S = ''
    for c in s:
        if c.isalnum():
            S += c
    print(S.lower())
    print(S.lower()[::-1])

    return S.lower() == S.lower()[::-1]
print(is_palindrome(" "))
