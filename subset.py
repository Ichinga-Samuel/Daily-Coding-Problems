test = [1, 3, 6, 24]


def subset(array):
    """
    Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either
    i % j = 0 or j % i = 0.
    For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
    :param array:
    :return: the largest subset that satisfy the condition
    """
    d = []
    for i in range(len(array)):
        j = array[i]
        a = [j]
        for k in array[i + 1:]:
            if j % k == 0 or k % j == 0:
                a.append(k)
            else: break
        d.append(a)
    return max(d, key=lambda x: len(x))


result = subset(test)
print(result)
