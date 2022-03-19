import csv

with open('file.csv', 'a') as csvfile:  # a = append mode
    mywriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')  # lineterminator=\n to remove blank line
    ans = 'y'
    while ans.lower() == 'y':
        # userinputs
        empno = int(input("Enter employee number:"))
        name = (input("Enter employee name:"))
        salary = int(input("Enter employee salary:"))
        # write data to csv
        mywriter.writerow([empno, name, salary])  # row = pass as single list
        print("##Data Saved...##")
        ans = input("Enter y if u want to Add more?")
