'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''
def removeStars(s):

    l = []
    for c in s:
        if c != '*':
            l.append(c)
        else:
            l.pop()

    return ''.join(l)

print(removeStars('leet**cod*e'))