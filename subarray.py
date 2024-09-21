# Python program to print all
# sublist from a given list
from itertools import combinations

# # function to generate all the sub lists
# def sub_lists (l):
# 	# initializing empty list
# 	comb = []
	
# 	#Iterating till length of list
# 	for i in range(len(l)+1):
# 		# Generating sub list
# 		comb += [list(j) for j in combinations(l, 3)]
# 	# Returning list
# 	return comb

# # driver code
# #Initial list
# l1 = [10, 4, 2, 5, 6 ,3, 8 ,1]

# #Print initial list
# print("Initial list is : " + str(l1))

# # Calling function to generate all sub lists
# print("All sub list is : "+ str(sub_lists(l1)))

def sub_lists (l,k):

    lists = [[]]
    #k = 3
    for i in range(len(l)-k+1):        
        lists.append(l[i:k])
        k+=1

        if len(lists[i]) < 1:
            lists.remove(lists[i])

    print(lists)

    # SUM = []
    # for a in lists:
    #     SUM.append(sum(a))
    
    #print(min(SUM))
    # SUM = [sum(s) for s in lists]
    # print(SUM)
    #return lists[SUM.index(min(SUM))]

    # return min(SUM)
    SS = []
    for l in lists:
        print(sum(l))
        if sum(l) == 0:
            SS.append(l)
    return SS
print(sub_lists([-1,0,1,2,-1,-4],3))

#print(sub_lists([1, -4, 2, 10, -2, 3, 1, 0, -20],4))
    
    
		



	

	




 
# # driver code
# l1 = [10 ,4, 2, 5, 6, 3, 8, 1]
# l2 = [1, -4, 2, 10, -2, 3, 1, 0, -20]
# print(sub_lists(l2,4))

# def subArray(l):
# 	s = [[]]
# 	a = 0
# 	for i in range(len(l)):
# 		k = i+1
# 		while k < (len(l)+1):
# 			s.append(l[i:k])
# 			k += 1
# 		if len(s[i]) < 1:
# 			s.remove(s[i])
# 	return s
# SUB_ARRAY = subArray([10 ,4, 2, 5, 6, 3, 8, 1])

# SUM = []
# for a in SUB_ARRAY:
# 	SUM.append(sum(a))




# print(SUB_ARRAY)
# print(SUM)

# print(SUB_ARRAY[SUM.index(min(SUM))])

def minSubarraySum(arr, n, k):
    S = [[]]

    for i in range(n-k+1):
        S.append(arr[i:k])
        k+=1
        if len(S[i]) < 1:
            S.remove(S[i])    
    SUM = [sum(a) for a in S]
    
    
    return min(SUM)


	# Write your code here


print(minSubarraySum([1, -4, 2, 10, -2, 3, 1, 0, -20],8,4))


