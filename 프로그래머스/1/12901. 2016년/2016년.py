def solution(a, b):
    year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = {0:"SUN", 1:"MON", 2:"TUE", 3:"WED", 4:"THU", 5:"FRI", 6:"SAT"}
    
    # 각 월의 1일은 무슨 요일?  1월 = 금요일
    start = 5 # friday (0~6)
    # ex) +2일 -> 7 (일요일 - 0이어야함) 즉 7로 나눈 나머지를 보기
    
    for month, days in year.items():
        if month >= a:
            break
        # next month's first day
        start = (start + days) % 7
        
    # target month's first day
    return day[(start + b - 1) % 7]