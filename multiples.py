def solution(number):
    # check if its a number
    if isnum(number) is False:
        return("Not a number")
    else:
        # check if its greater than o
        sum = 0
        if is_positive(number) is False:
            sum = 0
        else:
            n = 1
            while n < number:
                if (n % 3) == 0 or (n % 5) == 0:
                    sum = sum + n
                    n = n+1
                else:
                    n = n+1
        return sum


def isnum(number):
    try:
        number = int(number)
        return(True)
    except:
        return(False)


def is_positive(number):
    if number >= 0:
        return True
    else:
        return False


print(solution('y'))
