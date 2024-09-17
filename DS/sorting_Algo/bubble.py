def bubble(l):
    i = 0
    j = 0
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j+1]<l[j]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

print(bubble([3,5,1,7,23,10]))
