# Python program to search a string

# Returns index of x if it is present
# in arr[], else return -1
def binarySearch(arr, x):
    left = 0
    right = len(arr)     # right = 4
    while (left <= right):
        mid = left + ((right - left) // 2)  # mid=1

        res = (x == arr[mid])

        # Check if x is present at mid
        if (res == 0):
            return mid - 1

        # If x greater, ignore left half
        if (res > 0):
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            right = mid - 1

    return -1


# Driver Code
if __name__ == "__main__":

    arr = ["uma", "navina",
           "usha", "sachin"];
    x = input("Enter a word you want to search:")
    result = binarySearch(arr, x)

    if (result == -1):
        print("Element not present")
    else:
        print("Element found at index",
              result)
