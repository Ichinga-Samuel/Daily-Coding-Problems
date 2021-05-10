"""This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains. """

def rounds(n):
    r = 0
    while n > 1:
        # 0 heads 1 for tails
        p = [random.randint(0,1) for i in range(n)]
        h = [i for i in p if i==0]
        n = len(h)
        r += 1
    return r

rounds(5)

