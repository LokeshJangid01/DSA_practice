"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""
def min_window(s,t):
    Substrs = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            Substrs.append(s[i:j])
    print(Substrs)
    S = []
        
    for sub in Substrs:
        is_t_in_sub = True
        for c in t:
            if c in sub:
                continue
            else:
                is_t_in_sub = False
        if is_t_in_sub:
            # print(f'{sub}')
            S.append(sub)
    print(S)

    if len(S) == 0:
        return ""
    else:

        return min(S, key=len)

print(min_window("bbaa","aba"))
