# def hIndex(citations):
#     max_value = 0
#     max_index = 0
#     if citations.index(max(citations)) == 0:
#         return 0
#     else:
#         for i in range(1,len(citations)+1):
#             max_index = citations.index(max(citations[0:i]))
#             print(max_index)
#         return max_index+1
    
# print(hIndex([1,3,1]))
def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    # print(enumerate(citations))

    for i, c in enumerate(citations):
        print(i,c)

    #     if c >= i + 1:
    #         h = i + 1
    #     else:
    #         break
    # return h
    
print(hIndex([3,0,6,1,5]))