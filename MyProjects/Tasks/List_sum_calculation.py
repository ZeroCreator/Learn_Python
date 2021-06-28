# Вычисление суммы списка:
"""
def sum_all(*nambers):
    print(nambers, type(nambers))

    result = 0
    for namber in nambers:
        result += namber
    return result

print(sum_all(1, 8, 89, 90, 78, 5))

"""

"""
# Создание списка со значениями:

def input_namber():
    y = []
    x = input("input the namber or 'stop': ")
    while x != 'stop':
        z = int(x)
        y.append(z)
        print(y)
        x = input("input the namber: ")

input_namber()

"""
# окончательный вариант:

def input_namber():
    y = []
    x = input("input the namber or 'stop': ")

    while x != 'stop':
        z = int(x)
        y.append(z)
        print(y)
        x = input("input the namber or 'stop': ")

    if x == 'stop':

        def sum_all(y):

            result = 0
            for namber in y:
                result += namber
            return result

        print(sum_all(y))

input_namber()


print('*' * 30)

