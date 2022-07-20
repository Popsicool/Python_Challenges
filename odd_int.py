# def old_number(array):
#     for i in array:
#         count = array.count(i)
#         if (count % 2) != 0:
#             return(i)
#             break
# list= [1,1,2,2,2,2,2,2,3,3]
# print(old_number(list))
def find_it(seq):
    for i in seq:
        count = seq.count(i)
        if (count % 2) != 0:
            return(i)
            break


list = [1, 1, 2, 2, 2, 2, 2, 2, 3, 3,0]
print(find_it(list))
