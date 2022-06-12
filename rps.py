# Wrote this from scratch while helping someone with a Python homework assignment
# Play Rock, Paper, Scissors with the computer and get a readout at the end

# Used to generate computer choice
import random

# Initialize all variables to zero or blank
numrounds = 0
userresult = []
computerresult = []
userscore = 0
computerscore = 0
tiedscore = 0

# Input and validate number of rounds to play
while numrounds < 3 or numrounds > 7 or numrounds % 2 == 0:
    numrounds = int(
        input("How many rounds would you like to play (odd number between 3 and 7)? "))

# Start with round one and loop rounds until done
i = 1
while i <= numrounds:
    print("\nPlaying round " + str(i))
    # Computers turn
    # Pick random number 1=rock, 2=paper, 3=scissor
    random_number = random.randint(1, 3)
    if random_number == 1:
        computerresult.append("rock")
    elif random_number == 2:
        computerresult.append("paper")
    elif random_number == 3:
        computerresult.append("scissor")

    # Users turn
    hinput = "x"
    while hinput != 'R' and hinput != 'P' and hinput != 'S':
        hinput = input("Selec Rock, Paper, or Scissor (R,P,S): ")[0]
        hinput = hinput.upper()
    if hinput == "R":
        userresult.append("rock")
    elif hinput == "P":
        userresult.append("paper")
    elif hinput == "S":
        userresult.append("scissor")

    print("Computer picked: " + computerresult[i-1])
    print("You picked: " + userresult[i-1])

    # Main logic to figure out who won
    if computerresult[i-1] == userresult[i-1]:
        print("It's a tie!")
        tiedscore += 1
    elif computerresult[i-1] == "rock" and userresult[i-1] == "paper":
        print("You won!")
        userscore += 1
    elif computerresult[i-1] == "paper" and userresult[i-1] == "scissor":
        print("You won!")
        userscore += 1
    elif computerresult[i-1] == "scissor" and userresult[i-1] == "rock":
        print("You won!")
        userscore += 1
    elif userresult[i-1] == "rock" and computerresult[i-1] == "paper":
        print("The computer won!")
        computerscore += 1
    elif userresult[i-1] == "paper" and computerresult[i-1] == "scissor":
        print("The computer won!")
        computerscore += 1
    elif userresult[i-1] == "scissor" and computerresult[i-1] == "rock":
        print("The computer won!")
        computerscore += 1
    else:
        print("Something went very wrong")
    i += 1

print("\nAll done!\n")
print("The computers choices for each round were: ", *computerresult, sep=", ")
print("Your personal choices for each round were: ", *userresult, sep=", ")

print("Number of games you won: " + str(userscore))
print("Number of games the computer won: " + str(computerscore))
print("Number of tied games: " + str(tiedscore))

if userscore > computerscore:
    print("\nCongrats you won!")
elif computerscore > userscore:
    print("\nSorry the computer got you!")
else:
    print("\nYou were tied, maybe try another round.\n")

print("\nThank you for playing!\n")
