'''Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []'''


def anagrams(word, words):
    word = sorted(list(word.lower()))
    ana= []
    for i in words:
        if word == sorted(list(i.lower())):
            ana.append(i)
    return ana


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

# a = "Anang"
# a= sorted(list(a.lower()))
# print(a)