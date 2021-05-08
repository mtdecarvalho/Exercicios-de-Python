n = int(input())

for i in range(n):
    x = int(input())
    primo = 1
    for k in range(2, x):
        if x % k == 0:
            primo = 0
            break
    if primo:
        print("{} eh primo".format(x))
    else:
        print("{} nao eh primo".format(x))
    