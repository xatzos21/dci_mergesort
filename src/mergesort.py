# TODO implement mergesort
def mergesort(list, left=0, right=None):
    if right is None:
        right = len(list)

    if right > left + 1:
        middle = (left + right) // 2
        mergesort(list, left, middle)
        mergesort(list, middle, right)
        merge(list, left, middle, right)

    return list


def merge(list, left, middle, right):
    n1 = middle - left
    n2 = right - middle

    Left = [0] * n1
    Right = [0] * n2

    for i in range(n1):
        Left[i] = list[left + i]

    for j in range(n2):
        Right[j] = list[middle + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            list[k] = Left[i]
            i += 1
        else:
            list[k] = Right[j]
            j += 1
        k += 1

    while i < n1:
        list[k] = Left[i]
        i += 1
        k += 1

    while j < n2:
        list[k] = Right[j]
        j += 1
        k += 1
