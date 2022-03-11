import math
def quadraticDistance(a, b, c):
    delta = (b * b) - (4 * a * c)
    delta2 = math.sqrt(abs(delta))
    if delta > 0:
        Root1ofx = (-b + delta2) / (2 * a)
        Root2ofx = (-b - delta2) / (2 * a)
        print("The roots are:", Root1ofx, Root2ofx)
    elif delta == 0:
        print("Root is : ", (-b) / (2 * a))
    else:
        print("Roots are not real")

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
quadraticDistance(a, b, c)
