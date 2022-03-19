import json

file = open("student.json", 'r')      # r = read mode
x = file.read()
finaldata = json.loads(x)
print(finaldata)  # it gives data in list format
for a in finaldata:  # to get data 1 by 1
    print(a)  # it gives data in dict format

# write
d = {"name": "Usha", "Profession": "Teacher", "Salary": 30000}
f = open("newfile.json", 'w')
json.dump(d, f)  # dump means it write data into file
f.close()

# to append data to previous file
# f = open("newfile.json", 'a')     # a = append mode
# json.dump(["a", 1, 2, 3], f)  # it will append this data to prev file
# f.close()
