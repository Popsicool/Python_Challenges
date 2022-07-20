#convers binary to decimal

def binary_array_to_number(arr):
    decimal = 0
    power = 0
    n = len(arr) - 1
    while n >= 0:
        decimal = decimal + (arr[n] * (2 ** power))
        power += 1
        n -= 1
    return decimal


print(binary_array_to_number([1, 0, 1, 1]))
