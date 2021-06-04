
def carParkingRoof(cars, k):
    cars.sort()
    m = cars[-1]
    n = len(cars)
    for i in range(n):
        e = i + k - 1
        if e >= n: break
        if m > (c := cars[e] - cars[i] + 1): m = c
    return m


res = carParkingRoof([2, 10, 8, 17], 3)
print(res)
