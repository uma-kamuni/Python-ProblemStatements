string = "Hello" + " uma" + ", How are you?"    #variable to store string
print(string)

username = input("enter username:")             #new username for replacing
if len(username) >= 2:                           #checking length
    newString = string.replace("uma", username)  #replacing string
    print(newString)
else:
    print("Invalid input")