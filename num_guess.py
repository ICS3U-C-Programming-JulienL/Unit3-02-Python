#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 13, 2023
# This program is a number guessing for whole number between 0 and 9
import constants


def main():
    # get the user guess
    print(
        "In this game, a correct integer has been chosen from 0 to 9. Try to guess the correct integer."
    )
    user_guess = int(input("What is your guess for the correct integer: "))

    # if the user gets the number right, tell them they were right
    if user_guess == constants.CORRECT_GUESS:
        print("Your guess was right!")

    # if the user gets the number wrong, tell them they were wrong
    if user_guess != constants.CORRECT_GUESS:
        print("Your guess was wrong!")


if __name__ == "__main__":
    main()
