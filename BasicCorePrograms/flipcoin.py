import random
noOfFlips = int(input("Enter how many times you want to flip coin:"))
tail = 0
for i in range(noOfFlips):
    flips = random.uniform(0, 1)   #to get random values bet 0 to 1 & uniform() for floatig numbers
    if flips < 0.5:
        print(" It is tail")
        tail += 1
    else:
        print("It is head")

percentageOfTail = (tail / noOfFlips) * 100
percentageOfHead = 100 - percentageOfTail
print("percentage of tail is:" ,percentageOfTail, "%" )
print("percentage of head is:" , percentageOfHead , "%")


