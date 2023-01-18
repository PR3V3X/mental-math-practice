# randint function is needed for generating random problems.
from random import randint

# This uses a main function to loop the program.
def main():
    # This displays a menu for the user to look at.
    print("-" * 78)
    print("|~~~>                  Welcome to Mental Math Practice 1.1!              <~~~|")
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


    # Allows for range & problem loop.
    while True:
        # Allows the user to select a mode they want to practice.
        print("| Select what you want to practice using the symbols: + - * / ...            |")
        mode = input("| Mode: + - * / => ")

        # Allows user to pick a range of numbers.

        print("\n| Enter a range of numbers you want to work with...")
           
        num1 = int(input("| Number 1 (Lower Number): "))
        num2 = int(input("| Number 2 (Upper Number): "))

        # Allows user to set amount of problems.
        amount = int(input("| Enter the amount of problems you want to solve: "))

        for x in range(amount):

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


            elif mode == "-":
                # Calculates the correct answer.
                correct_answer = int2 - int1

                # Takes the user's answer.
                answer = int(input(f"\n| What is {int2} - {int1}? "))

                # Assesses whether correct or not, & displays correct answer.
                print("| Your answer is: ", answer == correct_answer)
                print(f"| The correct answer is {correct_answer}.\n")
                    

            elif mode == "*":
                # Calculates the correct answer.
                correct_answer = int1 * int2        

                # Takes the user's answer.
                answer = int(input(f"\n| What is {int1} * {int2}? "))

                # Assesses whether correct or not, & displays correct answer.
                print("| Your answer is: ", answer == correct_answer)
                print(f"| The correct answer is {correct_answer}.\n")
                    

            elif mode == "/":
                # Calculates the correct answer.
                correct_answer = round(int2 / int1, 4)      

                # Takes the user's answer.
                answer = float(input(f"\n| What is {int2} / {int1}? "))

                # Assesses whether correct or not, & displays correct answer.
                print("| Your answer is: ", answer == correct_answer)
                print(f"| The correct answer is {correct_answer}.\n")


            else:
                # Notifies user of incorrect choice entry.
                print(f"\nThe mode you selected was: {mode}.")
                print("That is not a valid entry. :(")
                print("Please enter a valid mode by using the + - * / symbols.\n")

            print("You have finished!")
main()
