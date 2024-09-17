class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)  # Convert the string to a list for easy swapping
        left, right = 0, len(s_list) - 1  # Two pointers

        while left < right:
            # Move left pointer until a vowel is found
            if s_list[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            elif s_list[right] not in vowels:
                right -= 1
            else:
                # Swap the vowels
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return ''.join(s_list)  

        