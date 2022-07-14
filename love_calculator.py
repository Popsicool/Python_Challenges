# 🚨 Love calculator Challenge from replit
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests
true = ["T", "R", "U", "E"]
love = ["L", "O", "V", "E"]
name = (name1 + name2).upper()
count1 = 0
count2 = 0
for i in true:
    no = name.count(i)
    count1 = count1 + no
for i in love:
    no = name.count(i)
    count2 = count2 + no
total = int(str(count1) + str(count2))
if (total < 10 or total > 90):
    print('Your score is %d, you go together like coke and mentos.' % total)
elif (total >= 40 and total <= 50):
    print('Your score is %d, you are alright together.' % total)
else:
    print('Your score is %d.' % total)


# Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
