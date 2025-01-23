from random import shuffle 

# Rules

print("\nWELCOME TO GUESS GAME!!!")
print("\n Rules: \n\n  guess the position of 'o'. \n  '0' for 1st. \n  '1' for 2nd. \n  '2' for 3rd." )
print("\nLET'S PLAY!!\n")


mylist = ['','o','']

# Shuffling list

def suffle_mylist(mylist):
    shuffle(mylist)
    return mylist

# Guess of the player

def player_guess():
    guess = int(input("Guess the Position: "))
    return guess
mixed_list = suffle_mylist(mylist)
guess = player_guess()

# Checking results

def result(mixed_list,guess):
    if mixed_list[guess] == 'o':
        print("You Won!!!")
    else:
        print("You Lose!!!")
    print(f"The position was {mixed_list}")

result(mixed_list,guess)
