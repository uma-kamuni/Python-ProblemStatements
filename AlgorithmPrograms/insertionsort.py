def insertionSort(my_list):
    for index in range(1, len(my_list)):  # len(list)=5 so index = 1,2,3,4
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos - 1] and pos > 0:
            my_list[pos] = my_list[pos - 1]
            pos = pos - 1
        my_list[pos] = current_element


list1 = [2, 4, 3, 5, 1]
insertionSort(list1)
print(list1)
