import random
print('Winning rules of the Rock, paper and scissor game as follows:')
print('rock vs paper -> paper wins')
print('rock vs scissor -> rock wins')
print('paper vs scissor -> scissor wins')

print('Enter a choice- 1, 2 or 3:')
print('1. rock')
print('2. paper')
print('3. scissor')
u = 0
c = 0
for i in range(1, 5):
    user_choice = int(input('User turn:'))
    if user_choice == 1:
        choice_str = 'rock'
    elif user_choice == 2:
        choice_str = 'paper'
    elif user_choice == 3:
        choice_str = 'scissor'
    print('User choice is:', choice_str)
    print('Now is computer turn')

    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        choice_stg = 'rock'
    elif computer_choice == 2:
        choice_stg = 'paper'
    elif computer_choice == 3:
        choice_stg = 'scissor'
    print('Computer choice is:', choice_stg)

    if (user_choice==1 and computer_choice==3) or (computer_choice==1 and user_choice==3):
        result = 'rock'
    elif (user_choice==2 and computer_choice==1) or (computer_choice==2 and user_choice==1):
        result = 'paper'
    elif (user_choice==3 and computer_choice==2) or (computer_choice==3 and user_choice==2):
        result = 'scissor'
    elif user_choice == computer_choice:
        result = 'pair'
        print('Pair, please try again')


    if result == choice_str:
        u = u+1
        print('user wins,', u)
    else:
        c = c+1
        print('computer wins, ', c)