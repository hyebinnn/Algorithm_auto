from itertools import combinations, permutations, product, combinations_with_replacement

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        dictionary.extend(list(product(alphabet, repeat=i)))

    dictionary.sort()
    tupleWord = tuple(word)
    
    return dictionary.index(tupleWord)+1