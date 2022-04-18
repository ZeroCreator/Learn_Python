# Проверка упорядоченности массива за O(N).
def check_sorted(A, ascending=True):
    """Проверка отсортированности за О(len(A))"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(A)-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag