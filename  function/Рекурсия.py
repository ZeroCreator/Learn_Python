# Алгоритмы на Python 3. Лекция №7. Тимофей Хирьянов
import graphics as gr


def matroshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matroshka(n-1)
        print("Низ матрешки n=", n)


matroshka(5)

# Глубина рекурсии - количество вызовов функции
# Рекурентный случай
# Крайний случай
import graphics as gr

windows = dr.GrapWin("Russian game", 300, 300)




