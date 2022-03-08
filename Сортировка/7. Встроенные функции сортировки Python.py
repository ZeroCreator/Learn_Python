# Метод sort()
apples_eaten_a_day = [2, 1, 1, 3, 1, 2, 2]
apples_eaten_a_day.sort()
print(apples_eaten_a_day) # [1, 1, 1, 2, 2, 2, 3]
# Функция sorted()
apples_eaten_a_day_2 = [2, 1, 1, 3, 1, 2, 2]
sorted_apples = sorted(apples_eaten_a_day_2)
print(sorted_apples) # [1, 1, 1, 2, 2, 2, 3]

# В порядке убывания
# Reverse sort the list in-place
apples_eaten_a_day.sort(reverse=True)
print(apples_eaten_a_day) # [3, 2, 2, 2, 1, 1, 1]
# Reverse sort to get a new list
sorted_apples_desc = sorted(apples_eaten_a_day_2, reverse=True)
print(sorted_apples_desc) # [3, 2, 2, 2, 1, 1, 1]

# обе эти функции могут сортировать списки кортежей и классов. Функция sorted() может сортировать любой итеративный
# объект, который включает в себя — списки, строки, кортежи, словари, наборы (set) и пользовательские итераторы.
# Встроенная функция сортировки реализуют алгоритм сортировки Тима. Этот алгоритм, основан на сортировке
# слиянием и сортировке вставкой.
