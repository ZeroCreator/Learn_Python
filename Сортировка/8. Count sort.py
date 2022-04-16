# Сортировка подсчетом (count sort) - O(n). - однопроходный алгоритм.
N = list(map(int, input().split()))
count = [0]*10
for i in N:
    count[i] += 1

for i in range(10):
    if count[i] > 0:
        print(str(i)*count[i], end='')


