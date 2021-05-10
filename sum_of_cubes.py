
def soc(n):
    """
    This problem shows how hash tables can be used to reduce O(n) time by increasing O(n) for space
    Find the solutions to a^3 + b^3 = c^3 + d^3 for all positive integers from 1 to n
    :param n:
    :return:
    """
    res = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i**3 + j**3] = (i, j)

    for k, m in res.items():
        for p in m:
            for q in m:
                print(p, q)
