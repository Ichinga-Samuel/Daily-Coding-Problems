test = ['R', 'G', 'B', 'G', 'B']


def merge_colors(array):
    """
    For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

            Arrangement       |   Change
    ----------------------------------------
    ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
    ['B', 'B', 'G', 'B']      | (B, G) -> R
    ['B', 'R', 'B']           | (R, B) -> G
    ['B', 'G']                | (B, G) -> R
    ['R']                     |
    :param array: input array containing the colors
    :return: An integer representing the smallest number of elements in the array after reduction
    """
    s = {'R', 'G', 'B'}
    colors = list(array)
    while len(set(colors)) > 1:
        for i in range(0, len(colors)):
            a = set(colors[i:i+2])
            if len(a) == 2:
                colors[i:i+2] = (s - a).pop()
    return len(colors)


result = merge_colors(test)
print(result)
