"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
This code implements the longestCommonPrefix function that takes a list of strings v as input and returns the longest common prefix of all the strings. Here is an explanation of how the code works:

Initialize an empty string ans to store the common prefix.
Sort the input list v lexicographically. This step is necessary because the common prefix should be common to all the strings, so we need to find the common prefix of the first and last string in the sorted list.
Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string.
If the current character of the first string is not equal to the current character of the last string, return the common prefix found so far.
Otherwise, append the current character to the ans string.
Return the ans string containing the longest common prefix.
Note that the code assumes that the input list v is non-empty, and that all the strings in v have at least one character. If either of these assumptions is not true, the code may fail.
"""
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
    

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the potential common prefix
    prefix = strs[0]
    
    # Compare this prefix with each string in the list
    for string in strs[1:]:
        # Reduce the prefix until it's a common prefix between prefix and the current string
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]  # Reduce the prefix by one character from the end
            
            # If the prefix becomes an empty string, there is no common prefix
            if not prefix:
                return ""
    
    return prefix

print(longest_common_prefix(["flower","flow","flight"]))