def minusTime(a, b):
    ah, am = map(int, a.split(':'))
    bh, bm = map(int, b.split(':'))
    if am > bm:
        bh -= 1
        bm += 60
    minute = bm - am
    hour = bh - ah
    
    return minute + hour*60


def solution(plans):
    plans.sort(key=lambda x: x[1])
    ing = []
    result = []
    def doing(interval, plan_name, plan_during):
        if interval < plan_during:
            ing.append((plan_name, plan_during - interval))
            return
        else:
            result.append(plan_name)
            interval = interval - plan_during
            if ing:
                pn, pd = ing.pop()
                doing(interval, pn, pd)
                   
    
    for i in range(len(plans)-1):
        interval = minusTime(plans[i][1], plans[i+1][1])
        doing(interval, plans[i][0], int(plans[i][2]))
        
    # 맨 마지막 과제
    result.append(plans[-1][0])
    if ing:
        result.extend(x[0] for x in reversed(ing))
    

    return result