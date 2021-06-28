"""
a = open('dataset.txt', 'r')
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b += a[i]
        a = a[:i] + "!" + a[i+1:]
c = a.split('!')[1:]
for i in range(len(b)):
    print(b[i] * int(c[i]), end="")



inf = open('dataset.txt', 'r')
s1 = inf.readline()
i = 0
d = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
g = ''
l = 0
s = ''

while i < len(s1):
    if s1[i] not in d:
        s = s1[i]
    elif s1[i] in d:
        g += s1[i]
    if s1[i+1] in d:
        i += 1
    continue
else:
    while l < int(g):
        print(s,end='')
        l += 1
        l = 0
        g = ''

        i+=1

inf.close()

"""
with open('dataset.txt', 'r') as (e):
    s1 = e.readline()
f = 0
n = ''
l = []
for i in range(len(s1)):
    # print (s1[i])
    if s1[i].isdigit():
        n += s1[i]
    elif s1[i].isalpha():
        if i >= 1:
            n1 = int(n)
            l.append(n1)
            n = ''
        l.append(s1[i])
if len(n) > 0:
    l.append(int(n))
n = ''
for i in range(0, len(l), 2):
    n += (l[i]*l[i+1])
with open('dataset1.txt', 'w') as (e):
    e.write(n)
