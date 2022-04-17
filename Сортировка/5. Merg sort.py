#Сортировка слиянием (Merge sort).
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    # Мы будет часто используем длины списков, поэтому удобно сразу создавать переменные для этого
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Мы проверяем, какое значение с начала каждого списка меньше
            # Если элемент в начале левого списка меньше, добавляем его в отсортированный список
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если элемент в начале правого списка меньше, добавляем его в отсортированный список
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # Если мы достигли конца левого списка, добавляем элементы из правого списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если мы достигли конца правого списка, добавляем элементы из левого списка
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list
def merge_sort(nums):
    # Если список представляет собой один элемент, возвращаем его
    if len(nums) <= 1:
        return nums
    # Используем деление с округленим по наименьшему целому для получения средней точки, индексы должны быть целыми числами
    mid = len(nums) // 2
    # Сортируем и объединяем каждую половину
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    # Объединить отсортированные списки в новый
    return merge(left_list, right_list)
# Проверяем, что все работает
random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)


# # Слияние двух упорядоченных массивов
# print("Слияние двух упорядоченных массивов")
# def merge(A:list, B:list):
#     C = [0]*(len(A) + len(B))
#     i = k = n = 0
#     while i < len(A) and k < len(B):
#         if A[i] <= B[k]:
#             C[n] = A[i]
#             i += 1
#             n += 1
#         else:
#             C[n] = B[k]
#             k += 1
#             n += 1
#     while i < len(A):
#         C[n] = A[i]
#         i += 1
#         n += 1
#     while k < len(B):
#         C[n] = B[k]
#         k += 1
#         n += 1
#
#     return C
#
#
# # Рекурентная функция
# print("Рекурентная функция")
# def merg_sort(A):
#     if len(A) <= 1:
#         return
#     middle = len(A)//2
#     L = [A[i] for i in range(0, middle)]
#     R = [A[i] for i in range(middle, len(A))]
#     merge_sort(L)
#     merge_sort(R)
#     C = merge(L, R)
#
#     for i in range(len(A)):
#         A[i] = C[i]
#
# B = [5, 2, 7, 3, 1]
# merg_sort(B)
# print(*B)