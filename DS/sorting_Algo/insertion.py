def insertion(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[j]<l[i]:
                l[i],l[j] = l[j],l[i]

    return l

print(insertion([3,5,1,7,23,10]))