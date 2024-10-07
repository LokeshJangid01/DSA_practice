x = "abc"
y = "pqr"
S = []
for i in range(len(x)):
    print(x[i])
    print(y[i])
    S.append(x[i])
    S.append(y[i])

print("".join(S))

#    OR
r = list(map(lambda s1,s2:s1+s2,x,y))
print(r)

# z =  x[1] + y[2]
# print(z)
