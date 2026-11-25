from collections import Counter
from math import prod

def solution(clothes):
    count = Counter(kind for _, kind in clothes)
    return prod(value+1 for value in count.values()) - 1