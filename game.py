import random

player = input("Please enter Player Name:")
print("Welcome to the Game", player)
print(player, "I'm Thinking of a number between 1 and 100\n")
print("Try to Guess the right number\n")
computer_number = random.randint(1,100)
count = 1

def main():
    guess = int(input("Your Guess?:"))
    global count
    if guess == computer_number:
        print("Congratz! You figued me out in", count, "turns!")
    elif guess < computer_number:
        print("Your Guess is too Low, Try Again!")
        count+=1
        main()
    elif guess > computer_number:
        print("Your Guess is too High, Try Again!")
        count+=1
        main()

main()   


