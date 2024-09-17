def selection(l):
    i = 0
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index = j
        if i!= min_index:
            l[i],l[min_index] = l[min_index],l[i]

    return l

print(selection([3,5,1,7,23,10]))
