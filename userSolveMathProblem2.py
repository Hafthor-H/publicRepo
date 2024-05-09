import random


def generateTwoNum():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return num1, num2

correct_answers = 0

while True:
    num1, num2 = generateTwoNum()
    answer1 = num1 + num2

    try:
        print('Solve this math problem little boy')
        user_input = int(input(f"What is the sum of {num1} and {num2}? "))
        if user_input == answer1:
            print('Correct! Here is a new problem:')
            correct_answers += 1 
        else:
            print(f'Incorrect, you solved {correct_answers} problems correctly before you failed.')
            break  
    except ValueError:
        print('Please enter a valid integer.')
