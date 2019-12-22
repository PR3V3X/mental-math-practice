from random import randint

'''
def add(int1, int2):
    return int1 + int2


def subtract(int1, int2):
    return int2 - int1


def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    return(int2 / int1)
'''


def range(int1, int2):
    # Computes two random integers for problem generation.
    lower = randint(int1, int2)
    upper = randint(int1, int2)


def addition():
    # Takes & interprets correct answer.
    correct_answer = lower + upper        
    answer = float(input(f"\n| What is {lower} + {upper}? "))
    print("| Your answer is:", answer == correct_answer)
    print(f"| The correct answer is {correct_answer}.")


    # Asks user if they want to continue.
    restart = input("\n| Would you like to continue with this mode? yes = 1, no = 0: ")
    if restart == "1":
        addition()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def main():
    # This prints the main menu of the program.
    print("-" * 78)
    print("|                  Welcome to Mental Math Practice 1.0!                      |")
    print("|                A Simple Way to Enhance Mental Math Skills                  |")
    print("|                                                                            |")
    print("|                                 Enjoy! :)                                  |")
    print("|____________________________________________________________________________|")
    print("|_________________________| Arithmetic Operators |___________________________|")
    print("| 1.) Addition => +                     2.) Subtraction => -                 |")
    print("| 3.) Multiplication => *               4.) Division => /                    |")
    print("|____________________________________________________________________________|")
    print("| Follow the instructions below...                                           |")
    print("-" * 78)

    # Takes interval of 2 #'s for random integer generation.
    print("\n| Enter a range of numbers you want to work with...")
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))
    range(num1, num2)

    # Allows the user to select a mode they want to practice.
    print("| Select what you want to practice using the symbols +-*/...")
    mode = input("| Mode: ")

    # This routes the user input to the proper selection.
    if mode == "+":
            addition()

    if mode == "-":
            subtraction()
                
    if mode == "*":
            multiplication()
                
    if mode == "/":
            division()

# Displays the main menu.
main()

