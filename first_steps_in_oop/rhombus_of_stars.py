def rhombus_creator(n):

    for i in range(1, n + 1):
        spaces = n - i
        symbols = ('*' + " ") * i
        print(spaces * " ", symbols)

    for j in range(n-1, -1, -1):
        spaces = n - j
        symbols = ('*' + " ") * j
        print(spaces * " ", symbols)


rhombus_creator(int(input()))
