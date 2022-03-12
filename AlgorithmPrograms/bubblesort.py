def bubblesort(numbers):
    # looping from (lengthoflist -1) to strat index 0
    for i in range(len(numbers) - 1, 0, -1):  # outer loop for 1st iteration
        for j in range(i):  # inner loop for next iteration
            if numbers[j] > numbers[j + 1]:
                # Swap if 1st number > next number
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# create list
numbers = [5, 3, 8, 6, 7, 2]
print("unsorted numbers are:", numbers)
bubblesort(numbers)  # function calling
print("The sorted numbers are:")
print(numbers)
