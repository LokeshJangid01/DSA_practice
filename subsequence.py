# #       find all the subsequence of given string

# def find_subsequences(string):
#     # Base case: If the string is empty, return an empty subsequence
#     if len(string) == 0:
#         return ['']
    
#     # Recursively find subsequences of the rest of the string
#     smaller_subsequences = find_subsequences(string[1:])
    
#     # Append the first character of the current string to each subsequence of the smaller subsequence
#     subsequences_with_first_char = [string[0] + subsequence for subsequence in smaller_subsequences]
    
#     # Return the combination of subsequences with and without the first character
#     return smaller_subsequences + subsequences_with_first_char

# # Example usage:
# string = "ahbgdc"
# subsequences = find_subsequences(string)
# print(subsequences)

def find_subsequences(s: str):
    n = len(s)
    subsequences = []
    
    # Loop over all numbers from 0 to 2^n - 1
    for i in range(1 << n):  # 1 << n is 2^n
        subsequence = ''
        for j in range(n):
            # Check if jth bit in i is set. If it is, include s[j]
            if i & (1 << j):
                subsequence += s[j]
        subsequences.append(subsequence)
    
    return subsequences

# Example usage
s = "ahbgdc"
subsequences = find_subsequences(s)
print(subsequences)

