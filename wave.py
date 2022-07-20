'''In this simple Kata your task is to create a function that turns 
a string into a Mexican Wave. You will be passed a string and you 
must return that string in an array where an uppercase letter is a person standing up. 
1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]'''


def wave(people):
    if len(people) < 1:
        return []
    else:
        wave_people = []
        n = 0
        while n < len(people):
            upper_word = list(people)
            upper_word[n] = people[n].upper()
            capital = None
            for i in upper_word:
                if capital == None:
                    capital = i
                else:
                    capital = capital + i
            wave_people.append(capital)
            n += 1
        return wave_people


# print(wave('Two words'))
a= ['s','e','r']
a.append(' ')
a.append('z')
print(a)