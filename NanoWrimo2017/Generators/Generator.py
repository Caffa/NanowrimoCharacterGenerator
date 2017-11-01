import json, random
from io import StringIO
# import pprint


############# Write Json to a file
# namesList = ["Everlyn", "Cassiopeia", "Augusta"]
# genderPossibilities = ["Male", "Female"]
# data = {"namesList": namesList, "genderPossibilities" : genderPossibilities}
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)

################### Convert Json from string to data type (so can use)
# json_string = json.dumps(data)
# data = json.loads(json_string)
# print data


# ################ LOAD json
# #prompt the user for a file to import
# #Read JSON data into the datastore variable
# with open("data.txt", 'r') as f:
#     datastore = json.load(f)
#
# #Use the new datastore datastructure
# print datastore.get("namesList")

######################################
#Dictionary
# d['mynewkey'] = 'mynewvalue'

### Creating an empty dictionary ###

# data = {}
# # OR
# data = dict()

### Creating a dictionary with initial values ###
#
# data = {'a':1,'b':2,'c':3}
# # OR
# data = dict(a=1, b=2, c=3)
# # OR
# data = {k: v for k, v in (('a', 1),('b',2),('c',3))}

### Inserting/Updating a single value ###
#
# data['a']=1  # Updates if 'a' exists, else adds 'a'
# # OR
# data.update({'a':1})
# # OR
# data.update(dict(a=1))
# # OR
# data.update(a=1)

### Inserting/Updating multiple values ###
#
# data.update({'c':3,'d':4})  # Updates 'c' and adds 'd'

### Creating a merged dictionary without modifying originals
#
# data3 = {}
# data3.update(data)  # Modifies data3, not data
# data3.update(data2)  # Modifies data3, not data2

### Deleting items in dictionary ###
#
# del data[key]  # Removes specific element in a dictionary
# data.pop(key)  # Removes the key & returns the value
# data.clear()  # Clears entire dictionary

### Check if a key is already in dictionary
# key in data
#
# ### Iterate through pairs in a dictionary
# for key in data: # Iterates just through the keys, ignoring the values
# for key, value in d.items(): # Iterates through the pairs


########################

with open("generatorData.txt", 'r') as f:
    generatorData = json.load(f)

############# Resource Imports

#Read JSON data into the datastore variable
with open("Resource/Names/FemaleYoung.json", 'r') as f:
    femaleNamesResource = json.load(f)


#Read JSON data into the datastore variable
with open("Resource/Names/MaleYoung.json", 'r') as f:
    maleNamesResource = json.load(f)
############# Name imports

print ("This is the current data file:")
s = json.dumps(generatorData,  indent = 4)
print (s)
############################################################## Generator Data place between
# generatorData.clear()
generatorData.update(name = ["placeholders"])

generatorData.update(gender = ["Female", "Male"])

generatorData['greeting'] = ['Hey', "Hi", "Hello", "Good Morning", "May Sou shine upon you", "Oh it's you", "Morning!", "Mornin\'", "Ciao", "Hello luv'", "Hey Pumpkin", "Morning Sweetheart", "Hi Dearie"]

generatorData['femaleNames'] = femaleNamesResource["names"]

generatorData['maleNames'] = maleNamesResource["names"]
 ############################################################## So it can be kept updated in file
print ("This is the updated data file:")
s = json.dumps(generatorData,  indent = 4)
print (s)

with open("generatorData.txt", 'w') as outfile:
    json.dump(generatorData, outfile, ensure_ascii=False)
