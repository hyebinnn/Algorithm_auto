def after(time):
    hour, minute = map(int, time.split(":"))
    minute += 10
    if minute >= 60:
        minute -= 60
        hour += 1
        
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"

    # if int(time[-2:]) + 10 >= 60:
    #     if int(time[:2])+1 >= 24:
    #         t = str((int(time[:2])+1)%24).zfill(2)+":"+str((int(time[-2:])%60)).zfill(2)
    #     else:
    #         t = str(int(time[:2])+1)+":"+str((int(time[-2:])%60)).zfill(2)
    # else:
    #      t = time[:-2]+str(int(time[-2:])+10)   
    # return t

def solution(book_time):
    book_time.sort(key=lambda x: (x[0], x[1]))
    room = []
    
    for s, e in book_time:
        if room:
            for i in range(len(room)):
                rs, re = room[i][0], room[i][1]
                # print(s, re)
                if s >= re:
                    room.pop(i)
                    break
                    
        e = after(e)
        room.append((s,e))
        room.sort(key=lambda x: x[1])

        # print(room)
        
        
        
    return len(room)