import random

f = open('game.txt', 'r')
file_data = f.read()
if file_data:
    file_data_splitted = file_data.split('\n')
    wins = int(file_data_splitted[0])
    losses = int(file_data_splitted[1])
    message = "Welcome Back\nWins: " + str(wins) + "\nLosses: " + str(losses)
else:
    wins = 0
    losses = 0
    message = "Welome to our awesome game\n"

tries = 0
entered_guesses = []
f.close()
number = random.randrange(1, 100, 1)

print(message)
while tries < 10:
    inpt = input("Enter a guess\n")
    if inpt.isnumeric():
        inpt = int(inpt)
        if inpt > 100 or inpt < 1:
            print("Please input a number from 1 to 100")
        elif inpt in entered_guesses:
            print("You have already entered this guess")
        elif inpt == number:
            print("Congradulations! you guess right.\n")
            wins += 1
            tries += 1
            entered_guesses.clear()
            number = random.randrange(1, 100, 1)
        elif inpt > number:
            print("number is smaller\n")
            entered_guesses.append(inpt)
            tries += 1
        elif inpt < number:
            print("Number is bigger\n")
            entered_guesses.append(inpt)
            tries += 1
    else:
        print("Entery is invalid! Please Enter in the range to 100")
print("Game Over!\nSorry you were not able to guess the number which is:", number)
losses += 1
f = open('game.txt', 'w')
f.write(str(wins) + "\n" + str(losses))
f.close()
