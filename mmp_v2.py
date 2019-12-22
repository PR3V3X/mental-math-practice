# randint function is needed for generating random problems.
from random import randint


def addition(amt):
    for i in range(amt):
        # Computes two random integers for problem generation.
        int1 = randint(num1, num2)
        int2 = randint(num1, num2) 

        # Calculates the correct answer.
        correct_answer = int1 + int2

        # Takes the user's answer.
        answer = int(input(f"\n| What is {int1} + {int2}? "))

        # Assesses whether correct or not, & displays correct answer.
        print("| Your answer is: ", answer == correct_answer)
        print(f"| The correct answer is {correct_answer}.\n")


def subtraction(amt):
    for i in range(amt):
        # Computes two random integers for problem generation.
        int1 = randint(num1, num2)
        int2 = randint(num1, num2)

        # Calculates the correct answer.
        correct_answer = int2 - int1

        # Takes the user's answer.
        answer = int(input(f"\n| What is {int2} - {int1}? "))

        # Assesses whether correct or not, & displays correct answer.
        print("| Your answer is: ", answer == correct_answer)
        print(f"| The correct answer is {correct_answer}.\n")


def multiplication(amt):
    for i in range(amt):
        # Computes two random integers for problem generation.
        int1 = randint(num1, num2)
        int2 = randint(num1, num2)

        # Calculates the correct answer.
        correct_answer = int1 * int2        

        # Takes the user's answer.
        answer = int(input(f"\n| What is {int1} * {int2}? "))

        # Assesses whether correct or not, & displays correct answer.
        print("| Your answer is: ", answer == correct_answer)
        print(f"| The correct answer is {correct_answer}.\n")


def divison(amt):
    for i in range(amt):
        # Computes two random integers for problem generation.
        int1 = randint(num1, num2)
        int2 = randint(num1, num2)

        # Calculates the correct answer.
        correct_answer = round(int2 / int1, 4)      

        # Takes the user's answer.
        answer = float(input(f"\n| What is {int2} / {int1}? "))

        # Assesses whether correct or not, & displays correct answer.
        print("| Your answer is: ", answer == correct_answer)
        print(f"| The correct answer is {correct_answer}.\n")


def none():
        # Notifys user of incorrect choice entry.
        print(f"\nThe choice you chose was: {mode}.")
        print("That is not a valid entry. :(")
        print("Please enter a valid choice by using the + - * / symbols.\n")


# This displays a menu for the user to look at.
print("-" * 78)
print("|~~~>                  Welcome to Mental Math Practice 2.0!              <~~~|")
print("|~~~~~~>            A Simple Way to Enhance Mental Math Skills        <~~~~~~|")
print("|~~~~~~~~~>                                                        <~~~~~~~~~|")
print("|~~~~~~~~~~~~>                     Enjoy! :)                    <~~~~~~~~~~~~|")
print("|____________________________________________________________________________|")
print("|_________________________| Arithmetic Operators |___________________________|")
print("| 1.) Addition => +                                2.) Subtraction => -      |")
print("| 3.) Multiplication => *                          4.) Division => /         |")
print("|____________________________________________________________________________|")
print("| Follow the instructions as shown below...                                  |")
print("-" * 78)

# Allows the user to select the mode once, then work with problems.
while True:
    # Allows the user to select a mode they want to practice.
    print("| Select what you want to practice using the symbols: + - * / ...            |")
    mode = input("| Mode: + - * / => ")

    # Amount of problems the user wants to have.
    amt = int(input("| Number of problems => "))

    # Allows user to pick a range of numbers to practice in.
    print("| Enter a range of numbers you want to work with...")           
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))

    # The if, elif statements are for selecting the modes.
    # The 'mode' choice gets routed to one of these.
    if mode == "+":
        addition(amt)

    elif mode == "-":
       subtraction(amt)                           

    elif mode == "*":
        multiplication(amt)

    elif mode == "/":
        divison(amt)

    else:
        none()
