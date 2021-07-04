from random import choice


def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = choice(arr)
    less = [i for i in arr[1:] if pivot >= i]
    greater = [i for i in arr[1:] if pivot < i]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(arr):
    if (s := len(arr)) <= 1:
        return arr

    k = s // 2
    m, n = arr[:k], arr[k:]
    m = merge_sort(m)
    n = merge_sort(n)
    out = []
    p1 = p2 = 0
    while p1 < len(m) and p2 < len(n):
        if (i := m[p1]) < (j := n[p2]):
            out.append(i)
            p1 += 1
        else:
            out.append(j)
            p2 += 1
    out += m[p1:] + n[p2:]
    return out


def bubble_sort(arr):
    for n in range((k := len(arr) - 1)):
        for i in range(k):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(0, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr


test = [2, 5, 7, 8, 1, 8, 9]
test1 = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(test))
