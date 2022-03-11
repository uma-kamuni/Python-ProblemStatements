import math


def windchill(v, t):
    if t < 50 and 120 > v > 3:
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
        print("The Windchill value is:", w)
    else:
        print("Please enter valid values.")


v = float(input("Enter wind speed in miles per hour:"))
t = float(input("Enter temperature in Fahrenheit:"))
windchill(v, t)
