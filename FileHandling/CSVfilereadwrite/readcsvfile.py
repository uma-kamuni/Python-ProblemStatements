import csv

with open('employee.csv') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',')
    count = 0
    print("%10s" % "EMPNO", "%20s" % "NAME", "%10s" % "SALARY")
    print('=' * 50)
    for row in myreader:
        print("%10s"% row[0], "%20s" % row[1], "%10s" % row[2])
        count += 1
    print('-' * 50)
    print("%30s"%"Total records=", count)
