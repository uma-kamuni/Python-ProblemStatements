import math

x = int(input("enter the command line argument x:"))
y = int(input("enter the command line argument y:"))

distance = math.sqrt((x * x) + (y * y))
print("The Euclidean distance from the point", (x, y), "to the origin (0, 0)", distance)

# another way of solving this program
...
import math


def euclideandistance(x, y):  # fun defination for calculating edistance
    distance = math.sqrt((x * x) + (y * y))  # formula for calc edistance
    print("The Euclidean distance from the point", (x, y), "to the origin (0, 0)", distance)


x = int(input("enter the command line argument x:"))  # taking user i/p
y = int(input("enter the command line argument y:"))
euclideandistance(x, y)  # callingfunction
...
