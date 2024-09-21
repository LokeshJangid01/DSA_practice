# from itertools import permutations

# def find_anagrams(word):
#     # Generate all permutations
#     perm = permutations(word)
#     # Convert each permutation tuple back to a string
#     anagrams = {''.join(p) for p in perm}
#     print(anagrams)

# find_anagrams('eat')

"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            # Sort the string to form the key
            sorted_str = ''.join(sorted(string))
            
            # Append the original string to the list of its anagram group
            anagram_map[sorted_str].append(string)

        # Return the values (grouped anagrams) as a list of lists
        return list(anagram_map.values())
        
