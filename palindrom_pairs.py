"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a 
palindrome
.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
"""

def pair(words):
    R = []
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            s = words[i]+words[j]
            if s == s[::-1]:
                R.append([i,j])
    print(R)

pair(["abcd","dcba","lls","s","sssll"])

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # R = []
        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         s1 = words[i]+words[j]
        #         s2 = words[j]+words[i]

        #         if i == j:
        #             continue
        #         elif s1 == s1[::-1]:
        #             R.append([i,j])
        #         elif s2 == s2[::-1]:
        #             R.append([j,i])

        # return R
        def is_palindrome(s):
            return s == s[::-1]
        word_map = {word[::-1]: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            # Check for all possible ways to split the word into prefix and suffix
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: Check if prefix is palindrome and suffix reversed exists in the dictionary
                if is_palindrome(prefix) and suffix in word_map and word_map[suffix] != i:
                    result.append([word_map[suffix], i])
                
                # Case 2: Check if suffix is palindrome and prefix reversed exists in the dictionary
                # (To avoid duplicates, check j != len(word) to prevent adding the same word twice)
                if j != len(word) and is_palindrome(suffix) and prefix in word_map and word_map[prefix] != i:
                    result.append([i, word_map[prefix]])

        return result
            