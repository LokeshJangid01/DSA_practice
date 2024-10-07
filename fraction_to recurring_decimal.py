"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
"""
def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"
    
    result = []
    
    # Determine the sign
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    
    # Convert to positive
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Append the integer part
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    if remainder == 0:
        return "".join(result)
    
    result.append(".")
    
    # Dictionary to store remainders and their corresponding indices
    remainder_dict = {}
    
    while remainder != 0:
        if remainder in remainder_dict:
            result.insert(remainder_dict[remainder], "(")
            result.append(")")
            break
        
        remainder_dict[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    
    return "".join(result)
        


    # print(Ans_List)

    # elif len()
print(fraction_to_decimal(4,333))