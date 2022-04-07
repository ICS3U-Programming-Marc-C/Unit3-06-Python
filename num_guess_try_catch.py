#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This is a guess the number game

# Importing the random module
import random


def main():
    while True:
        print("This is a number guessing game.")
        # Ask user for input
        user_input = input("Enter a number between 0 and 9: ")
        # Cast user input to a integer

        try:
            user_num = int(user_input)
        except:
            print("Invalid value. Please try again")
            continue

        # Define the random number
        random_number = random.randint(0, 9)
        # Check the numbers and display the output

        if user_num == random_number:
            print("You guessed correctly!")
        else:
            print("You guessed wrong, the correct number is {}".format(random_number))

        break


if __name__ == "__main__":
    main()
