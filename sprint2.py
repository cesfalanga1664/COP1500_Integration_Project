#Christopher Sfalanga

#This is a program designed to quiz
#the user on information listed in the
#PCEP exam syllabus.

#using three libraries here.
import random, time, os

def greetUser():
    "Greets the user, gets their name, and starts a countdown for the quiz"
    
    print('Welcome to the PCEP exam quiz - Basic Concepts! v2')

    username = input("What should I call you?")

    printHSeparator()
    print('Awesome, welcome to PCEP exam quiz ['+username+'].', end='\n\n')

    printHSeparator()
    print('Beginning quiz...', end='')

    i = 3
    while i > 0:
        print(i, end='')
        time.sleep(1)
        i = i - 1
        
    print(' Begin!\n')

    
def printHSeparator():
    "purely aesthetic purposes to separate each question / section display"
    
    print('-'*10, end='\n\n')
    
def askQuestion(question, answer_choices, correct_answer_index):
    """question asked - a string.
       answer choies - a list of strings.
       correct_answer_index - (int) index of correct answer in answer_choices.

       The function poses the given question with its given answer choices.
       Then it receives user selection and returns 1 (correct) or 0 (incorrect)."""
    
    print(question)

    letter_choices = []
    if len(answer_choices) == 2:
        letter_choices = ['A', 'B']
    elif len(answer_choices) == 4:
        letter_choices = ['A', 'B', 'C', 'D']
    else:
        print('askQuestion: UNEXPECTED NUMBER OF ANSWER CHOICES. EXITING FUNCTION.')

    for i in range(0, 4):
        if i >= len(answer_choices):
            break
        print(letter_choices[i]+')', answer_choices[i])
    print()

    user_selection = ''
    while not (user_selection in letter_choices):
        if user_selection != '':
            print('Invalid answer choice! lower v.s. upper case matters!')
    
        user_selection = input('selection: ')

    if user_selection == letter_choices[correct_answer_index]:
        print('Correct! Good job.')
        return 1
    else:
        print('Incorrect :(')
        return 0

greetUser()

num_correct = 0
total_possible = 6

#MODULUS OPERATOR QUESTION
print('Question 1/6\n')

dividend = random.randint(1, 20)
divisor =  random.randint(1, 20)

correct_answer = dividend % divisor;

answer_choices = [0]*4;
correct_answer_index = random.randint(0, 3)
for i in range(0, 4):
    if i == correct_answer_index:
        answer_choices[i] = correct_answer

    else:
        polarity = 1
        if random.randint(1, 10) > 5:
            polarity *= -1
        answer_choices[i] = correct_answer + polarity * random.randint(1, divisor)

question_str = 'Which of the following is equal to '+str(dividend)+' % '+str(divisor)+' ?\n'
num_correct += askQuestion(question_str, answer_choices, correct_answer_index)

#the sleep function will pause the program for n seconds, here I'm choosing 2 seconds.
#I got this function from: https://www.tutorialspoint.com/python/time_sleep.htm
time.sleep(2)

printHSeparator()

#EXPONENTIATION OPERATOR QUESTION
print('Question 2/6\n')

a = random.randint(1, 5)
b =  random.randint(1, 3)

correct_answer = a ** b;

answer_choices = [0,0,0,0]
correct_answer_index = random.randint(0, 3)
for i in range(0, 4):
    if i == correct_answer_index:
        answer_choices[i] = correct_answer
    else:
        polarity = 1
        if random.randint(1, 10) > 5:
            polarity *= -1
        answer_choices[i] = correct_answer + polarity * random.randint(1, divisor)
question_str = 'Which of the following is equal to '+str(a)+'**'+str(b)+' ?\n'
num_correct += askQuestion(question_str, answer_choices, correct_answer_index)

time.sleep(2)

printHSeparator()

#DIVISION VS FLOOR DIVISION OPERATOR QUESTION

print('Question 3/6\n')

#As the question suggests, a // b computes the floor division of a by b.
#so rounding down a divided by b to the nearest whole number. a / b is classic division, possibly floating point.
#I got help from this website: https://www.informit.com/articles/article.aspx?p=674692&seqNum=4#:~

question_str = 'True or False, 1 // 2 = '+str(1 // 2)+' represents floor division whereas 1/2 = '+str(1/2)+' represents classic division.'
num_correct += askQuestion(question_str, ['True', 'False'], correct_answer_index = 0)

time.sleep(2)

printHSeparator()

#T/F about interpreter
print('Question 4/6', end='\n\n')

question_str = 'True or False, Python is an interpreted language.'
num_correct += askQuestion(question_str, ['True', 'False'], correct_answer_index = 0)

time.sleep(2)
printHSeparator()


#shortcut operator question
print('Question 5/6', end='\n\n')

question_str = 'Which of the following uses a shortcut operator to decrement variable `foo`?';
num_correct += askQuestion(question_str, ['foo = foo - 1', 'foo -- 1', 'foo -= 1', 'decr(foo)'], correct_answer_index = 2)

time.sleep(2)
printHSeparator()

#T/F compilation question
print('Question 6/6', end='\n\n')

question_str = 'True or False: Although Python is an interpreted language, it goes through a compilation stage when you run a script.';
num_correct += askQuestion(question_str, ['True', 'False'], correct_answer_index=0)

time.sleep(2)
printHSeparator();

#The round function will round num_correct/total_possible to two decimal places.
#I got this function from: https://realpython.com/python-rounding/
score = round(num_correct/total_possible, 2)

print('You\'re done! And now for your final score... Drumroll please...', end='\n\n')

#a cute little text-based double-stroke drum roll.
for i in range(0, 5):
    for j in range(0, 16):
        if (j // 2) % 2 == 0:
            print('R', end='')
        else:
            print('L', end='')
        time.sleep(0.1)
    print()

print()

print('Your score is: ', score*100, '%')

if score < 0.700:
    print('You failed :( Please study more.')
elif score >= .7 and score < .800:
    print('You got a C! Better keep studying...')
elif score >= .8 and score < .900:
    print('You got a B! That\'s ok, but you should keep studying...')
elif score > .9 or score == 0.9:
    print('You got an A! That\'s pretty good. Keep in mind the PCEP exam might be harder.')

input('\nPress enter when you\'re ready to leave')
print('exiting...')
