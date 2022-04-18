# Сортировка подсчетом (count sort) - O(n). - однопроходный алгоритм.
N = map(int, input().split())
count = [0]*10
for i in N:
    count[i] += 1

p = []
for i in range(10):
    p.extend([i]*count[i])

print(p)

# def count_sort(n):
#     c = []*10
#     d = list(map(int, n))
#     for i in d:
#         c[i] += 1
#
#     p = []
#     for i in range(10):
#         p.extend([i]*c[i])
#
#     return p
#
# p = count_sort([1, 5, 2, 5, 4, 8, 6, 5])
# print(p)

def CountSort(list):
    sortedList = [0] * 101
    for i in list:
        sortedList[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedList[i], end='')


list = [int(i) for i in input().split()]
CountSort(list)


def countSort(a):
    acc=[]
    for i in range(101):
        acc+=[0]
    for i in a:
        acc[i]+=1
    j=0
    for i in range(101):
        if acc[i]>0:
            for k in range(acc[i]):
                a[j]=i
                j+=1
    return a