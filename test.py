# randint function is needed for generating random problems.
from random import randint

# This uses a main function to loop the program.
def main():
    # This displays a menu for the user to look at.
    print("-" * 78)
    print("|~~~>                  Welcome to Mental Math Practice 1.0!              <~~~|")
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

        # Allows for range & problem loop.
        while True:
            # Allows user to pick a range of numbers to practice in.
            print("\n| Enter a range of numbers you want to work with...")
           
            num1 = int(input("| Number 1 (Lower Number): "))
            num2 = int(input("| Number 2 (Upper Number): "))

            for x in range(5): 
                # Computes two random integers for problem generation.
                int1 = randint(num1, num2)
                int2 = randint(num1, num2)


                # The if, elif statements are the modes the problems are made in.
                # The 'mode' choice gets routed to one of these.
                if mode == "+":
                
                # Calculates the correct answer.
                    correct_answer = int1 + int2

                # Takes the user's answer.
                    answer = int(input(f"\n| What is {int1} + {int2}? "))

                # Assesses whether correct or not, & displays correct answer.
                    print("| Your answer is: ", answer == correct_answer)
                    print(f"| The correct answer is {correct_answer}.\n")

            else:
                # Notifies user of incorrect choice entry.
                print(f"\nThe choice you chose was: {mode}.")
                print("That is not a valid entry. :(")
                print("Please enter a valid choice by using the + - * / symbols.\n")

main()