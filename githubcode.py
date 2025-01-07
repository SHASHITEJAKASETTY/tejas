# import os
# import random
# import math
# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd






# # Basic File Handling
# file_path = "example.txt"

# def write_to_file():
#     with open(file_path, "w") as file:
#         file.write("Hello, this is a sample file.\n")
#         file.write("Python is amazing!\n")

# def read_from_file():
#     if os.path.exists(file_path):
#         with open(file_path, "r") as file:
#             for line in file:
#                 print(line.strip())
#     else:
#         print("File does not exist.")

# write_to_file()
# read_from_file()









# # Basic Calculator

# def calculator():
#     print("Welcome to the Basic Calculator")
#     while True:
#         try:
#             num1 = float(input("Enter first number: "))
#             operator = input("Enter operator (+, -, *, /): ")
#             num2 = float(input("Enter second number: "))

#             if operator == '+':
#                 print(f"Result: {num1 + num2}")
#             elif operator == '-':
#                 print(f"Result: {num1 - num2}")
#             elif operator == '*':
#                 print(f"Result: {num1 * num2}")
#             elif operator == '/':
#                 if num2 != 0:
#                     print(f"Result: {num1 / num2}")
#                 else:
#                     print("Error: Division by zero.")
#             else:
#                 print("Invalid operator.")
#         except ValueError:
#             print("Invalid input. Please enter numbers.")

#         cont = input("Do you want to continue? (yes/no): ").lower()
#         if cont != 'yes':
#             break

# calculator()






# # Data Analysis with NumPy and pandas

# def data_analysis():
#     data = np.random.randint(1, 100, size=(10, 5))
#     df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E"])
#     print("Generated DataFrame:")
#     print(df)
#     print("\nSummary Statistics:")
#     print(df.describe())

# data_analysis()







# # Web Scraping Example

# def web_scraping():
#     url = "https://www.example.com"
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#         print("Title of the webpage:", soup.title.string)
#     except Exception as e:
#         print("Error during web scraping:", e)

# web_scraping()







# # Simple Number Guessing Game

# def number_guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     secret_number = random.randint(1, 100)
#     attempts = 0

#     while True:
#         try:
#             guess = int(input("Guess the number (1-100): "))
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# number_guessing_game()









# # Additional Functionality: Factorial Calculator

# def factorial_calculator():
#     print("Welcome to the Factorial Calculator")
#     while True:
#         try:
#             num = int(input("Enter a non-negative integer: "))
#             if num < 0:
#                 print("Factorial is not defined for negative numbers.")
#             else:
#                 print(f"The factorial of {num} is {math.factorial(num)}")
#         except ValueError:
#             print("Invalid input. Please enter a non-negative integer.")

#         cont = input("Do you want to calculate another factorial? (yes/no): ").lower()
#         if cont != 'yes':
#             break

# factorial_calculator()




# # Random Password Generator
# def generate_password(length=12):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
#     password = ''.join(random.choice(characters) for _ in range(length))
#     print(f"Generated Password: {password}")

# generate_password()





# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# def prime_checker():
#     print("Welcome to the Prime Number Checker")
#     while True:
#         try:
#             num = int(input("Enter a number to check if it's prime: "))
#             if is_prime(num):
#                 print(f"{num} is a prime number.")
#             else:
#                 print(f"{num} is not a prime number.")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

#         cont = input("Do you want to check another number? (yes/no): ").lower()
#         if cont != 'yes':
#             break

# prime_checker()







# def fibonacci_sequence(n):
#     sequence = [0, 1]
#     for _ in range(2, n):
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence

# def fibonacci_program():
#     print("Welcome to the Fibonacci Sequence Generator")
#     while True:
#         try:
#             n = int(input("Enter the number of terms for the sequence: "))
#             if n < 1:
#                 print("Please enter a positive integer.")
#             else:
#                 print(f"Fibonacci Sequence ({n} terms): {fibonacci_sequence(n)}")
#         except ValueError:
#             print("Invalid input. Please enter a positive integer.")

#         cont = input("Do you want to generate another sequence? (yes/no): ").lower()
#         if cont != 'yes':
#             break

# fibonacci_program()






# # Temperature Converter
# def temperature_converter():
#     print("Welcome to the Temperature Converter")
#     while True:
#         try:
#             temp = float(input("Enter the temperature: "))
#             unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

#             if unit == 'C':
#                 converted = (temp * 9/5) + 32
#                 print(f"{temp}C is {converted}F.")
#             elif unit == 'F':
#                 converted = (temp - 32) * 5/9
#                 print(f"{temp}F is {converted}C.")
#             else:
#                 print("Invalid unit. Please enter 'C' or 'F'.")
#         except ValueError:
#             print("Invalid input. Please enter a valid temperature.")

#         cont = input("Do you want to convert another temperature? (yes/no): ").lower()
#         if cont != 'yes':
#             break

# temperature_converter()

# # Final Message
# print("Thank you for exploring this Python demonstration!")











import random
import time


# Function to display game instructions
def display_instructions():
    print("=" * 50)
    print("WELCOME TO THE GUESS THE WORD GAME!")
    print("Instructions:")
    print("1. You will be given a hint about a word.")
    print("2. Guess the word in as few attempts as possible.")
    print("3. You can type 'quit' to exit the game anytime.")
    print("=" * 50)


# Function to get a random word and hint
def get_word_and_hint():
    words = [
        ("python", "A popular programming language."),
        ("keyboard", "An input device used to type."),
        ("ocean", "A large body of saltwater."),
        ("elephant", "The largest land animal."),
        ("mountain", "A large natural elevation of the earth's surface."),
        ("rainbow", "An arc of colors visible in the sky."),
        ("universe", "Everything that exists in space and time."),
        ("book", "A collection of pages with stories or information."),
        ("puzzle", "A problem that tests your ingenuity."),
        ("computer", "A device for processing information.")
    ]
    return random.choice(words)


# Function to display the game menu
def display_menu():
    print("\nGame Menu:")
    print("1. Play the Game")
    print("2. View High Scores")
    print("3. Exit")


# Function to get user input for the menu
def get_menu_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to play the game
def play_game(high_scores):
    word, hint = get_word_and_hint()
    print("\nHint:", hint)
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Your guess: ").lower()
        attempts += 1

        if guess == "quit":
            print("You chose to exit the game. Better luck next time!")
            return None

        if guess == word:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(f"\nCongratulations! You guessed the word '{word}' in {attempts} attempts.")
            print(f"Time taken: {duration} seconds.")
            return {"attempts": attempts, "time": duration}
        else:
            print("Wrong guess. Try again!")


# Function to display high scores
def display_high_scores(high_scores):
    print("\nHIGH SCORES")
    print("-" * 50)
    if not high_scores:
        print("No high scores yet. Be the first to set one!")
    else:
        for i, score in enumerate(high_scores, 1):
            print(f"{i}. Attempts: {score['attempts']}, Time: {score['time']} seconds")
    print("-" * 50)


# Main function
def main():
    high_scores = []
    display_instructions()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:  # Play the game
            result = play_game(high_scores)
            if result:
                high_scores.append(result)
                high_scores = sorted(high_scores, key=lambda x: (x["attempts"], x["time"]))[:5]
        elif choice == 2:  # View high scores
            display_high_scores(high_scores)
        elif choice == 3:  # Exit the game
            print("Thank you for playing! Goodbye!")
            break


# Run the program
if __name__ == "__main__":
    main()
