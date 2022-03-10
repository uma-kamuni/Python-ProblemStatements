import math
N = int(input("Enter the power:"))
if 0 <= N <= 31:
    powerOf2 = int(math.pow(2, N))
    print(powerOf2)

else:
    print("enter the power in range 0-31")
