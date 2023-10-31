from itertools import permutations

def solution(k, dungeons):
    maxDungeon, cntDungeon = 0, 0
    n = len(dungeons)
    sequence = list(permutations(dungeons, n))
    for seq in sequence:
        # print("=====================")
        fatigue = k
        cntDungeon = 0
        for dungeon in seq:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                cntDungeon += 1
            # print("조합: {0}\n현재 피로도: {1} & 현재 던전: {2}\ncount : {3}\n\n".format(seq, fatigue, dungeon, cntDungeon))
        if maxDungeon < cntDungeon:
            maxDungeon = cntDungeon
            
            
    return maxDungeon