import time
print('Object of the game: Get a higher average dice roll than the computer')
number_dice = input('Enter number of dice you want to roll:')
number_dice = int(number_dice)
ready = input('Ready to start? hit any key to continue')
import random
def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice


user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls)
time.sleep(3)
print('Computers turn')
time.sleep(3)
computer_rolls = roll_dice(number_dice)
print('Computer first roll: ', computer_rolls)

def find_winner(cdice_list, udice_list):
    computer_average = sum(cdice_list) / len(cdice_list)
    user_average = sum(udice_list) / len(cdice_list)
    print('Computer average', computer_average)
    print('User average',user_average)
    if user_average > computer_average:
        print('User wins')
    elif user_average < computer_average:
        print('Computer wins')
    else:
        print('It is a tie!')

find_winner(computer_rolls,user_rolls)

user_choices = input('Enter - to hold or r to roll again :')
while len(user_choices) != number_dice:
    print('You must enter', number_dice, 'choices')
    user_choices =input('Enter - to hold or r to roll again:')

def roll_again(choices, dice_list):
    print('Rolling again...')
    time.sleep(3)
    for i in range (len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
    time.sleep(3)

roll_again(user_choices, user_rolls)
print('Player new roll: ', user_rolls)

def computer_strategy1(n):
    print('Computer is thinking...')
    time.sleep(3)
    choices=''
    for i in range(n):
        choices=choices + 'r'
    return choices

def computer_strategy2(n):
    print('Comptuer is thinking...')
    time.sleep(3)
    choices=''
    for i in range(n):
        if computer_rolls[i] < 5:
            choices=choices + 'r'
        else:
            choices = choices + '-'
    return choices

computer_choices = computer_strategy2(number_dice)
print('Computer Choice: ', computer_choices)

roll_again(computer_choices, computer_rolls)
print('Computer new roll: ', computer_rolls)
find_winner(computer_rolls,user_rolls)
