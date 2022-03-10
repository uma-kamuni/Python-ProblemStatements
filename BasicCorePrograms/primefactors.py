N = int(input("Enter the number you want to calculate prime factor:"))
if N > 1:
    i = 2  # prime no starts from 2 (2,3,5,7,11...n)
    print("factors of", N, "are:")
    while i <= N:
        while N % i == 0:
            print(i)
            N = N / i
        i += 1
else:
    print("please, enter another number")
