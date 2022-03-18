"""
JSON.json Inventory Data Management of Rice, Pulses and Wheats
a. Desc > Create a JSON.json file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.
b. Use Library : Java JSON.json Library , For IOS JSON.json Library use
NSJSONSerialization for parsing the JSON.json .
c. I/P> read in JSON.json File
d. Logi> Get cJSON Object in Java or NSDictionary in iOS. Create Inventory
Object from JSON.json. Calculate the value for every Inventory.
e. O/p> Create the JSON.json from Inventory Object and output the JSON.json String
"""
import json

"""
json function is created where data is loaded and inventory value are calculated and 
it file is dumped back as a json str
"""


def json_inventory():
    with open("JSON.json", "r") as f:  # json file is loaded in dict format
        data = json.load(f)

    riceinvent = 0
    wheatinvent = 0
    pulseinvent = 0

    # to file data in each inventory
    for i in data["Rice"]:
        for price in i:
            riceinvent += i["price per kg"]  # data is incremented

    for i in data["wheat"]:
        for price in i:
            wheatinvent += i["price per kg"]  # data is incremented

    for i in data["pulses"]:
        for price in i:
            pulseinvent += i["price per kg"]  # data is incremented

    print("""total value for rice in inventory is {},
total value for wheat in inventory is {},
total value for pulse in inventory is {}""".format(riceinvent, wheatinvent, pulseinvent))
    # .format() insert the calculated values in {} for rice,wheat,flour
    # we don't need to convert int values into str for print it will convert automatically

# write data
    dump = json.dumps(data)
    print(dump)
    with open('output.json', 'w') as outfile:
        json.dump(dump, outfile)
    # print(type(dump))  # then data is dumped in str format in output.json file


"""
main function is created to call json function 
"""
if __name__ == '__main__':
    json_inventory()
