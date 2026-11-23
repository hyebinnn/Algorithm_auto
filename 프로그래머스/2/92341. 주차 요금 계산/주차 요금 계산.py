from collections import defaultdict
import math

def to_minute(time):
    hour, minute = map(int, time.split(":"))
    
    return (hour * 60) + minute
    


def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    board = defaultdict(int)     # 차량별 누적주차 시간
    answer = []
    
    for record in records:
        time, car_number, status = record.split(" ")
        time = to_minute(time)
        
        if status == "IN":
            board[car_number] -= time
        else: 
            board[car_number] += time
        
    # 23:59
    final_time = to_minute("23:59")
    
    # 차량 번호가 작은 순으로 정렬
    # 출차 정보가 없는 차
    for cn, t in sorted(board.items()):
        if t <= 0:
            board[cn] += final_time
            
        if board[cn] > basic_time:
            answer.append(basic_fee + math.ceil((board[cn] - basic_time) / unit_time) * unit_fee)
        else:
            answer.append(basic_fee)
    
    
    return answer
            
    