def solution(citations):
    citations.sort()
    for h in range(citations[-1], -1, -1):
        cnt = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= h:
                cnt += 1
            elif citations[i] < h and cnt < h:               # h is so big -> get next h
                break
        if cnt >= h:
            return h