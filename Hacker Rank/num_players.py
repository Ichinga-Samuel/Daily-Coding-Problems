def numPlayers(k, scores):
    # Write your code here
    s = reversed(sorted(list(set(scores))))
    c = 1
    sc = {i: scores.count(i) for i in s}
    n = 0
    for i in sc:
        if i == 0: break
        c += sc[i]
        n += sc[i]
        if c >= k: break
    return n


res = numPlayers(3, [100, 50, 50, 25])
print(res)
