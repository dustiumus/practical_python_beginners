import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total
def main():
    player1 = input("Enter a player 1's name: ")
    player2 = input("Enter a player 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled a", roll1)
    print(player2, "rolled a", roll2)

    if roll1 > roll2:
        print(player1, "WINS!!")
    elif roll1 < roll2:
        print(player2, "WINS!!")
    else:
        print("It's a TIE!!")

main()


