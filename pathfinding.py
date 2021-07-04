

def path(arr):
    s = 4
    for i in range(s):
        for j in range(s):
            b = arr[i][j]
            r = j+1
            d = i+1
            br = arr[i][r] if r < s else None
            bd = arr[d][j] if d < s else None


def line