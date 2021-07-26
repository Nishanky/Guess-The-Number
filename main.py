# GUESS THE NUMBER



import random

def check_num(a, b, random_number):
    num = int(input(f"Guess a number between {a} and {b} :"))
    number_of_turns = 1

    while True:
        if num >= a and num <= b:
            if num == random_number:
                print("Congratulations!! You entered a correct number")
                break
            elif num > random_number:
                num = int(input(f"OOPs!! You guessed a larger number..Guess a smaller number between {a} and {b} :"))
                number_of_turns += 1
            elif num < random_number:
                num = int(input(f"OOPs!! You guessed a smaller number..Guess a larger number between {a} and {b} :"))
                number_of_turns += 1
            else:
                print("OOPs!!Something went wrong..")
                exit()

        else:
            num = int(input(f"You entered some wrong number...Guess a number between {a} and {b} :"))
            number_of_turns += 1

    print(f"You guessed a number in {number_of_turns} trials..\n")

    return number_of_turns



if __name__ == '__main__':
    a = 0
    b = 0
    try:
        a = int(input("Enter the value of a:"))
        b = int(input("Enter the value of b:"))

        if a > b:
            print("a must be greater than b..")
            exit()
    except ValueError:
        print("Please enter only interger value..")
        exit()

    random_number1 = random.randint(a, b)
    print("Player 1:\n")
    p1 = check_num(a, b, random_number1)

    random_number2 = random.randint(a, b)
    print("Player 2:\n")
    p2 = check_num(a, b, random_number2)

    if p1 > p2:
        print("Player 2 is winner")
    elif p2 > p1:
        print("Player 1 is winner")
    else:
        print("You both guessed the number in same number of trials...Match Tie!!")

    print(f"Random number for Player 1 was '{random_number1}' and for Player 2 was '{random_number2}'")




