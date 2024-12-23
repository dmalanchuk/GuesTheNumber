import random



def difficulty_level(difficulty_lvl: int):
    random_number = random.randint(1, 100)
    user_number = input("Please enter a number between 1 and 100: ")
    
    try:
        user_number = int(user_number)
    except ValueError:
       print("Please enter a valid number!")
       return
    
    while difficulty_lvl > 0:
            if user_number == random_number:
                print("Congratulations! You guessed the number!")
                break
            elif user_number < random_number:
                print("The number is higher!")
            else:
                print("The number is lower!")
            difficulty_lvl -= 1
            print(f"You have {difficulty_lvl} attempts left!")
            user_number = int(input("Please enter a number between 1 and 100: "))

def guess_the_number():
    print("Welcome to the number guessing game!")
    lvl = input("Please select a difficulty level: easy, medium, hard: ")

    if lvl == "easy":
        difficulty_level(difficulty_lvl=7)
    elif lvl == "medium":
        difficulty_level(difficulty_lvl=5)
    elif lvl == "hard":
        difficulty_level(difficulty_lvl=3)

    
    
if __name__ == "__main__":
    guess_the_number()