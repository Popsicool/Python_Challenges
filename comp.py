'''Given two arrays a and b write a function comp(a, b) 
(orcompSame(a, b)) that checks whether the two arrays have 
the "same" elements, with the same multiplicities (the multiplicity of a 
member is the number of times it appears). "Same" means, here, that the 
elements in b are the elements in a squared, regardless of the order.'''


def comp(array1, array2):
    # square each of the element in array1 and store in an  ordered list
    squared = []
    for i in array1:
        a = i*i
        squared.append(a)
    # re-arrage array 2
    # compare the 2
    if sorted(squared) == sorted(array2):
        return True
    else:
        return False
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print(comp(a,b))