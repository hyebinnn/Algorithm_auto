def solution(today, terms, privacies):
    answer = [] 
    
    ty, tm, td = map(int, today.split("."))
    # 오늘 날짜를 N일차 정수로 바꿔서 계산하기
    today = ty * 12 * 28 + tm*28 + td
    term = dict(t.split(" ") for t in terms)
    
    for i, p in enumerate(privacies):
        date, kind = p.split(" ")
        y,m,d = map(int, date.split("."))
        agree_date = y*12*28 + m*28 + d
        
        end_date = agree_date + int(term[kind]) * 28 - 1
        
        if end_date < today:
            answer.append(i+1)
    
    return answer
    
    
    
    
    
    
#     answer = []
    
#     term = dict(t.split(" ") for t in terms)
    
#     for i, p in enumerate(privacies):
#         date, kind = p.split(" ")
        
#         if check_end(date, int(term[kind]), today):
#             answer.append(i+1)
    
#     return answer


# def check_end(date, t, today):
#     year, month, date = map(int, date.split("."))
#     year = year + (month + t) // 12
#     month = (month + t) % 12
#     date = 31 if date == 1 else date - 1
    
#     return today > f"{year:02}.{month:02}.{date:02}"