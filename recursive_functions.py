def recursive_max(arr):
    a = None
    for i in arr:
        if isinstance(i, (list, tuple)):
            r = recursive_max(i)
            i = r
        if a is None or i > a:
            a = i
    return a


test = [2, 5, 7, 8, 1, 8, 9]
test1 = [3, 5, 7, 2, 4, [6, 8, 4, [89, 90, [890, [0, 6, [3, -5]]]]]]

# print(recursive_max(test))
# print(recursive_max(test1))


def recursive_min(arr):
    a = None
    for i in arr:
        if isinstance(i, (list, tuple)):
            r = recursive_min(i)
            i = r
        if a is None or i < a:
            a = i
    return a


# print(recursive_min(test1))
# print(recursive_min(test))


def recursive_sum(arr):
    if len(arr) == 1: return arr[0]
    return arr[0] + recursive_sum(arr[1:])


print(recursive_sum(test))
print(sum(test))
