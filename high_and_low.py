def high_and_low(numbers):
    numbers= numbers.split(" ")
    high = None
    low = None
    for i in numbers:
        i= int(i)
        if high == None:
            high = i
        else:
            if i > high:
                high = i
        if low == None:
            low = i
        else:
            if i < low:
                low = i
    result = str(high)+' '+str(low)

    return (result)
print(high_and_low("42 -9"))
