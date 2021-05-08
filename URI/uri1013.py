a, b, c = [int(x) for x in input().split()]


maiorab = int((a + b + abs(a - b)) / 2)


if maiorab > c:
    print("{} eh o maior".format(maiorab))
else:
    print("{} eh o maior".format(c))
