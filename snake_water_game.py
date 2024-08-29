#Making Snake Water Gun Game in python

import random
user = int(input("0 for snake, 1 for water, 2 for gun:\n"))
while user not in [0, 1, 2]:
    user = int(input("0 for snake, 1 for water, 2 for gun:\n"))

computer = random.randint(0, 2)

def check(comp, user):
    if comp == user:
        return "0"
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    return 1

score = check(computer, user)

print("You", user)
print("Computer", computer)

if(score == 0):
    print("It's a tie")
elif (score == -1):
    print("You Loose")
else:
    print("You Win")