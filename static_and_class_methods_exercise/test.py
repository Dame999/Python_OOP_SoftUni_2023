lst = [1, 2, 3, 4, 5]

try:
    abv = lst[4]
    print("yes")
except IndexError:
    print("no")