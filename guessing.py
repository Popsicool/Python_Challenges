# Guessing Game that allow players to  guess Alphabets of a randomly selected contry,
# player looses if they make 5 wrong guessing


import random

countries = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Anguilla', 'Antarctica',
             'Macao', 'Madagascar', 'Malawi', 'Nigeria', 'Niue', 'Romania', 'Zambia', 'Zimbabwe']
picked = random.choice(countries).lower()
country = list(picked)
length = len(country)
i = 1
count_dash = []
while i <= length:
    count_dash.append('-')
    i = i + 1


miss = 0
while miss < 5:
    country2 = country
    guess = input("Guess an alphabet: \n").lower()
    if len(guess) != 1:
        print("Guess must be 1 character long. Try again! \n")
        continue
    else:
        if guess.isalpha() is False:
            print("Alphabets only please \n")
            continue
        else:
            print('You guessed ' + guess + ' and...... \n')
            if guess in country2:
                print("Your guess is correct!" + "\U0001F60D \n")
                pos = country2.index(guess)
                count_dash[pos] = guess
                country2[pos] = '*'
                guessed = ''
                for i in count_dash:
                    guessed = guessed + i
                print(guessed)
                if guessed == picked:
                    print("Hurray! You got the country, its " +
                          picked.title() + "\U0001F601 \n")
                    break
            else:
                print('You missed' + "\U0001F612 \n")
                miss += 1
if miss == 5:
    print("You've made 5 wrong guessing. Game Over!" + '\n')
    print("The Country is " + picked.title() + "\U0001F923 \n")
