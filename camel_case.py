def convert_to_camel_case(s):
    if len(s) == 1:
        return s.lower()
    else:
        L = s.split(' ')
        print(L)
        S = ''
        for w in L[1:]:
            S += w.capitalize()
            print(S)

        return L[0] + S
    
print(convert_to_camel_case("hello world"))