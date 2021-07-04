
def min_(arr):
    a = None
    for i in arr:
        if a is None or i < a:
            a = i
    return a


def max_(arr):
    a = None
    for i in arr:
        if a is None or i > a:
            a = i
    return a


test = [2, 5, 7, 8, 1, 8, 9]
print(min_(test))
print(max_(test))


def sort(arr, asc=True):
    func = min_ if asc else max_
    for i in range(len(arr)):
        arr.remove(r:=func(arr[i:]))
        arr.insert(i, r)
    return arr


print(sort(test, asc=True))
print(sort(test))
