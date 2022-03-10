N = int(input("Enter the harmonic value:"))
harmonicvalue = 0
for i in range(1,n N + 1):  # adding 1/1 + 1/2 + 1/3 + ....+ 1/N
    harmonicvalue += 1 / i
    print("the Nth harmonic value is:" , harmonicvalue)
