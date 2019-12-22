from random import randint

# These functions are the different modes the user selects to practice.
# All of the calculations are done inside of each funtion.

def addition():
    # Allows user to pick a range of numbers to practice in.
    print("\n| Enter a range of numbers you want to work with...")
    
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))

    # Computes two random integers for problem generation.
    int1 = randint(num1, num2)
    int2 = randint(num1, num2)

    # Takes & interprets correct answer.
    correct_answer = int1 + int2        
    answer = float(input(f"\n| What is {int1} + {int2}? "))
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


def subtraction():
    # Allows user to pick a range of numbers to practice in.
    print("\n| Enter a range of numbers you want to work with...")
    
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))

    # Computes two random integers for problem generation.
    int1 = randint(num1, num2)
    int2 = randint(num1, num2)

    # Takes & interprets correct answer.
    correct_answer = int2 - int1        
    answer = float(input(f"\n| What is {int2} - {int1}? "))
    print("| Your answer is:", answer == correct_answer)
    print(f"| The correct answer is {correct_answer}.")

    # Asks user if they want to continue.
    restart = input("\n| Would you like to continue with this mode? yes = 1, no = 0: ")
    if restart == "1":
        subtraction()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def multiplication():
    # Allows user to pick a range of numbers to practice in.
    print("\n| Enter a range of numbers you want to work with...")
    
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))

    # Computes two random integers for problem generation.
    int1 = randint(num1, num2)
    int2 = randint(num1, num2)

    # Takes & interprets correct answer.
    correct_answer = int1 * int2        
    answer = float(input(f"\n| What is {int1} * {int2}? "))
    print("| Your answer is:", answer == correct_answer)
    print(f"| The correct answer is {correct_answer}.")

    # Asks user if they want to continue.
    restart = input("\n| Would you like to continue with this mode? yes = 1, no = 0: ")
    if restart == "1":
        multiplication()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def division():
    # Allows user to pick a range of numbers to practice in.
    print("\n| Enter a range of numbers you want to work with...")
    
    num1 = int(input("| Number 1 (Lower Number): "))
    num2 = int(input("| Number 2 (Upper Number): "))

    # Computes two random integers for problem generation.
    int1 = randint(num1, num2)
    int2 = randint(num1, num2)

    # Takes & interprets correct answer.
    correct_answer = int2 / int1        
    answer = float(input(f"\n| What is {int2} / {int1}? "))
    print("| Your answer is:", answer == correct_answer)
    print(f"| The correct answer is {correct_answer}.")

    # Asks user if they want to continue.
    restart = input("\n| Would you like to continue with this mode? yes = 1, no = 0: ")
    if restart == "1":
        multiplication()
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
main()
        
