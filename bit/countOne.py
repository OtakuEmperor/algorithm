def countOne(number):
    counter = 0
    while number:
        counter += (number & 1)
        number >>= 1
    return counter


print(countOne(11))
