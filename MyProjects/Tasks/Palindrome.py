# Проект Эйлера: Условие
# Самое большое число-палиндром, полученное умножением двухзначных чисел - 9009 = 91 * 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
# Решение1:

import time
start = time.time()

def comput():
    ans = max(i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[ : : -1])
    return str(ans)



if __name__ == '__main__':
    print(comput())
    end = time.time()
    print('time: ', end - start)


# Решение2:
import time
start = time.time()

def polindrome(number):
    l = str(number)
    for i in range(len(l)):
        if l == l[::-1]:
            return True
        else:
            return False

pol_max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if polindrome(j*i) and j*i > pol_max:
            pol_max = j*i
print(pol_max)

end = time.time()
print('time: ', end - start)