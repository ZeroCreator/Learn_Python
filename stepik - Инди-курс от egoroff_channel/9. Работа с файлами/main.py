#with open('numbers.txt', 'r') as f:
#    for line in f:
#        n = int(f.readline())
#        print(n, type(n))

with open('numbers.txt') as inf:
    s = inf.read().strip().split()


count = 0
sum = 0

for i in s:
    if len(i) == 3:
        count += 1
    if len(i) == 2:
        sum += int(i)

print(count, sum)