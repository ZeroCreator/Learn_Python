# Алгоритмы сортировки на Python.
# 1. Сортировка пузырьком
# 2. Сортировка выбором
# 3. Сортировка вставками
# 4. Сортировка Шелла
# 5. Пирамидальная сортировка
# 6. Сортировка слиянием
# 7. Быстрая сортировка
# 8. Сортировка подсчетом
import math
from typing import List

array = [5, 8, 9, 4, 2, 3, 1, 8, 7, 6, 5, 9, 10, 56, 8, 65]
print("1.Сортировка методом пузырька")
#  перебираем наш список и на каждой итерации сравниваем элементы попарно. При необходимости элементы меняются
#  местами, чтобы больший элемент отправлялся в конец списка.
# - нерекурсивный;
# - устойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(n2);
def bubbleSort(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return array

print(bubbleSort(array))

print("2.Сортировка выбором")
# В этом алгоритме мы создаем два сегмента нашего списка: один отсортированный, а другой несортированный.
# В процессе выполнения алгоритма мы каждый раз удаляем самый маленький элемент из несортированного сегмента списка
# и добавляем его в отсортированный сегмент. Мы не меняем местами промежуточные элементы.
# Следовательно, этот алгоритм сортирует массив с минимальным количеством перестановок.
# - нерекурсивный;
# - может быть как устойчивым, так и неустойчивым;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(n2);

def selectionSort(array):
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

print(selectionSort(array))

print("3.Сортировка вставками")
# Подобно алгоритму сортировки выбором, мы делим наш список на две части. Далее мы перебираем неотсортированную часть
# и вставляем каждый элемент из данного сегмента на его правильное место в отсортированной части списка.
# - нерекурсивный;
# - устойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(n2);
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

print(insertionSort(array))

print("4.Сортировка Шелла")
# Сортировка Шелла является оптимизированным вариантом сортировки вставками.
#
# Оптимизация достигается путем сравнения не только соседних элементов, но и элементов на определенном расстоянии,
# которое в течении работы алгоритма уменьшается. На последней итерации это расстояние равно 1. После этого алгоритм
# становится обычным алгоритмом сортировки вставками, что гарантирует правильный результат сортировки.
# - нерекурсивный;
# - устойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(n2), но это также зависит от выбора длины интервала;
def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

print(shellSort(array))

print("5.Пирамидальная сортировка («сортировка кучей»)")
# создаем два сегмента списка: отсортированный и несортированный.
# Метод heapify в примере кода использует рекурсию для получения элемента с максимальным значением на вершине.
# - нерекурсивный;
# - неустойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(nlog(n));
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

print(heapSort(array))

print("6.Сортировка слиянием")
# делим список ровно пополам и продолжаем это делать, пока в нем не останется только один элемент. Затем мы объединяем
# уже упорядоченные части нашего списка. Мы продолжаем это делать, пока не получим отсортированный список со всеми
# элементами несортированного входного списка.
# - рекурсивный;
# - устойчивый;
# - требует дополнительной памяти;
# - имеет сложность O(nlog(n));
nums = [5, 8, 9, 4, 2, 3, 1, 8, 7, 6, 5, 9, 10, 56, 8, 65]
def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSort(nums[:mid+1])
    lst2 = mergeSort(nums[mid+1:])
    result = merge(lst1, lst2)
    return result
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst

print(mergeSort(nums))

print("7.Быстрая сортировка")
# разбиваем список при помощи опорного элемента, сортируя значения вокруг него.
# В нашей реализации мы выбрали опорным элементом последний элемент массива.
# Наилучшая производительность достигается тогда, когда опорный элемент делит список примерно пополам.
# - рекурсивный;
# - неустойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place);
# - имеет сложность O(nlog(n));
def quickSort(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array

print(quickSort(array))

print("8.Сортировка подсчетом")
# Этот алгоритм не производит сравнение элементов. Для сортировки используются математические свойства целых чисел.
# Мы подсчитываем вхождения числа в массиве и сохраняем результат во вспомогательном массиве, где индексу соответствует
# значение ключа.
# - нерекурсивный;
# - устойчивый;
# - преобразует входные данные без использования вспомогательной структуры данных (in place),
# но все же требует дополнительной памяти;
# - имеет сложность O(n);
def sortArray(self, nums: List[int]) -> List[int]:
    i_lower_bound, upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound, upper_bound = min(nums), max(nums)

    counter_nums = [0] * (upper_bound - lower_bound + 1)
    for item in nums:
        counter_nums[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums



