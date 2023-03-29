from itertools import permutations


def possible_permutations(items):
    for el in list(permutations(items)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3, 4])]