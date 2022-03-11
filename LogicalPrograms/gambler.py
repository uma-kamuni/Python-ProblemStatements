import random

stake = int(input("Enter stake value:"))
goal = int(input("Enter goal value:"))
nooftimes = int(input("Enter number of times player wants to play:"))

bets = 0
wins = 0

for i in range(nooftimes):
    totalCash = stake
    while totalCash > 0 and totalCash < goal:  # while 0 < total-cash < goal
        bets += 1  # simulate 1 bet
        if random.randint(0, 1) > 0.5:
            totalCash += 1
            print("Gambler win $1")
            wins += 1
        else:
            totalCash -= 1
            print("Gambler loose $1")

print(int(wins), int(nooftimes))
percentage = (100 * (int(wins) // nooftimes))
print("percentage of wins:", percentage)
print("percentage of loss:", 100 - percentage)
