def change_3_8(amount):
    """ A recursive program to show that any amount greater than 8 can be changed to 3 and 5 coins """

    assert amount >= 8
    if amount == 8:
        return [3, 5]
    if amount == 9:
        return [3, 3, 3]
    if amount == 10:
        return [5, 5]

    coins = change_3_8(amount-3)
    coins.append(3)
    return coins


a = change_3_8(100)
print(a)


def change_5_7(value):

    if value == 24:
        return [5, 5, 7, 7]
    if value == 25:
        return [5, 5, 5, 5, 5]
    if value == 26:
        return [7, 7, 7, 5]
    if value == 27:
        return [5, 5, 5, 5, 7]
    if value == 28:
        return [7, 7, 7, 7]

    coins = change_5_7(value-5)
    coins.append(5)
    return coins


b = change_5_7(49)
print(b)
