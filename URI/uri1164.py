n = int(input())

for i in range(0, n):
    x = int(input())
    soma = 0
    for k in range(1, x):
        if x % k == 0:
            soma+=k
    if x == soma:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))
