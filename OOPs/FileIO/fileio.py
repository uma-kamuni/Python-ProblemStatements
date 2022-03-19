class file_io():  # class 1

    def operation():
        with open('contact.txt', 'r') as file:  # To read the file. Here no need to close
            print("Contact Details Are: \n ", file.read())

            print("------------------------------------")

            for line in file:  # to read data line by line
                print(line, end='')  # printing the contents of the file
            print("\n")

            print("------------------------------------")
        # write operation
        with open('contact.txt', 'a') as new_file:  # a mode to write in same file
            new_file.write("\n Hello! This is Uma \n")

            print("Successfully read and write content in the file")


class main(file_io):  # single inheritance
    if __name__ == '__main__':
        file_io.operation()
        pass


print("\n")
print("------End of program------")
