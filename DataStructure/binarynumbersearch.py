pos = -1  # global variable normally starts with 0, -1 means not got value


def search(list, n):  # n= number we want to search
    l = 0             # l = lower index/bound
    u = len(list) - 1  # u = upper bound

    while l <= u:  # bcoz lower bound is always less
        mid = (l + u) // 2   # (0+5)/2 i.e m= 2

        if list[mid] == n:
            globals()['pos'] = mid  # to find position of mid
            return True  # true once we get value we are searching
        else:
            if list[mid] < n:
                l = mid + 1  # mid becomes lower bound , +1 for shifting index
            else:
                u = mid - 1  # mid becomes upper bound

    return False


list = [4, 7, 8, 12, 45, 99]
n = 45

if search(list, n):
    print("Number found at", pos)
else:
    print("Not found")