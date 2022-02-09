print('Welcome to QiuzGame!')
print("Let's begin th game!")
choice = input('Are you ready to play the game? Yes or No:')
choiceL = choice.lower()
if choice == 'yes':
    print("Great! Question 1 will follow.")
    noOfQuestions = 4
    score = 0
    print('What is your favorite programing language?')
    raspunsQ1 = input()
    raspunsQ1L = raspunsQ1.lower()
    if raspunsQ1L == 'python':
            score += 1
            print('Correct answer')
    else:
            print('Wrong')

    print('What library help you generate random numbers?')
    raspunsQ2 = input()
    raspunsQ2L = raspunsQ2.lower()
    if raspunsQ2L == 'random':
            score +=1
            print('Correct answer')
    else:
            print('Wrong')

    print('Did openpyxl help us wotk whith exel?')
    raspunsQ3 = input()
    raspunsQ3L = raspunsQ3.lower()
    if raspunsQ3L == 'yes':
            score += 1
            print('Correct answer')
    else:
            print('Wrong')

    print('It is  Python a scripting language?')
    raspunsQ4 = input()
    raspunsQ4L = raspunsQ4.lower()
    if raspunsQ4L == 'yes':
            score += 1
            print('Correct answer')
    else:
            print('Wrong')

    mark = (score/noOfQuestions)*100
    print('Your mark is: ', mark)
    print('You answered at ', score, 'correct questions')

else:
    print("Ok! Heave a nice day!")