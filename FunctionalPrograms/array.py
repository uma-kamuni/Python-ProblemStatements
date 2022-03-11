def array(M, N):  # M = rows N = columns
    arr = [[i for i in range(M)] for j in range(N)]  # arr[] = [rows][columns]
    print(arr)


M = int(input("Enter no of rows:"))
N = int(input("Enter no of columns:"))
array(M, N)  # functioncalling
