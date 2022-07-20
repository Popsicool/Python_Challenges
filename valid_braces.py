'''Write a function that takes a string of braces, and determines if the order of the 
braces is valid. It should return true if the string is valid, 
and false if it's invalid.'''


def valid_braces(string):
    par1 = []
    bra1 = []
    cur1 = []
    par2 = []
    bra2 = []
    cur2 = []
    for i in string:
        if i == "[":
            par1.append(string.index(i))
        elif i == "]":
            par2.append(string.index(i))
        elif i == "{":
            cur1.append(string.index(i))
        elif i == "}":
            cur2.append(string.index(i))
        elif i == "(":
            bra1.append(string.index(i))
        elif i == ")":
            bra2.append(string.index(i))
    if len(par1) != len(par2) or len(bra1) != len(bra2) or len(cur1) != len(cur2):
        return False
    index = 0
    while index < len(par1):
        if par1[index] > par2[index]:
            return False
        index = index + 1

    index = 0
    while index < len(bra1):
        if bra1[index] > bra2[index]:
            return False
        index = index + 1
    index = 0
    while index < len(cur1):
        if cur1[index] > cur2[index]:
            return False
        index = index + 1
    return True


print(valid_braces("[(])"))

# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False
