def solution(citations):
    citations.sort()
    # print(citations)
    maxH = citations[-1]
    hIndex = 0
    # cnt = 0
    for maxH in range(citations[-1], -1, -1):
        cnt = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= maxH:
                cnt += 1
            elif citations[i] < maxH and cnt < maxH:
                break
        if cnt >= maxH:
            return maxH
            
        
#         quoteMore = len(citations[i:])
#         if quoteMore >= citations[i]:
#             hIndex = citations[i]
            
#     return hIndex