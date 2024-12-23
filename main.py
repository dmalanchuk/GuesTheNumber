import random

def guess_the_number():
    print("Welcome to the number guessing game!")
    random_number = random.randint(1, 100)
    user_number = input("Please enter a number between 1 and 100: ")

    try:
        user_number = int(user_number)
    except ValueError:
       print("Please enter a valid number!")
       return

    while True:

    
    
if __name__ == "__main__":
    guess_the_number()