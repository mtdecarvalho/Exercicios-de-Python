menor = 0
N = int(input())
stream = input()
T = (stream.split())
for i in range(N):
    if int(T[menor]) > int(T[i]):
        menor = i
print(menor+1)
