# -*- coding: utf-8 -*-
import json, random, codecs
from io import StringIO

# try:
#     with open("Generator/toGenerate.json", 'r') as f:
#         toGenerate = json.load(f)
#     with open("Generator/consolidatedGeneratorResource.json", "r") as f:
#         generatorData = json.load(f)
#     # print ("This is the list to generate")
#     # print (json.dumps(toGenerate,  indent = 4))
#     # print ("This is the current data file:")
#     # print (json.dumps(generatorData,  indent = 4))
# except IOError:
#     # generatorData.clear()
#     generatorData = dict()
#     toGenerate = []

generatorData = dict()
toGenerate = []

############# Actual Generating field imports
listOfStuffToGen = ['gender', 'name', 'greeting']
toGenerate = listOfStuffToGen
# TODO: physical appearance, personality types (tie to traits), childhood, family (have some sort of ability to tweak traits possibility of appearance? or add according to family / event)



############# Resource Imports

#Read JSON data into the datastore variable
with open("Resource/Names/FemaleYoung.json", 'r') as f:
    femaleNamesResource = json.load(f)

#Read JSON data into the datastore variable
with open("Resource/Names/MaleYoung.json", 'r') as f:
    maleNamesResource = json.load(f)

#Read JSON data into the datastore variable
with open("Resource/Names/lastNamesCommoner.json", 'r') as f:
    lastNamesCommoner = json.load(f)


#Read JSON data into the datastore variable
with open("Resource/Names/middleNames.json", 'r') as f:
    middleNames = json.load(f)

#Read JSON data into the datastore variable-------- families
with open("Resource/Names/SouMiddleNames.json", 'r') as f:
    SouMiddleNames = json.load(f)

with open("Resource/Names/BlackwoodMiddleNames.json", 'r') as f:
    BlackwoodMiddleNames = json.load(f)

# with open("Resource/Names/HazelineMiddleNames.json", 'r') as f:
#     HazelineMiddleNames = json.load(f)
#
# with open("Resource/Names/AquariusMiddleNames.json", 'r') as f:
#     AquariusMiddleNames = json.load(f)

with open("Resource/Names/ConstelliaMiddleNames.json", 'r') as f:
    ConstelliaMiddleNames = json.load(f)
#
# with open("Resource/Names/EvergreenMiddleNames.json", 'r') as f:
#     EvergreenMiddleNames = json.load(f)
#
# with open("Resource/Names/BearonMiddleNames.json", 'r') as f:
#     BearonMiddleNames = json.load(f)


############# Actual Resource Imports
generatorData['lastNamesCommoner'] = lastNamesCommoner
generatorData['middleNames'] = middleNames
generatorData['SouMiddleNames'] = SouMiddleNames
generatorData['BlackwoodMiddleNames'] = BlackwoodMiddleNames
generatorData['ConstelliaMiddleNames'] = ConstelliaMiddleNames





generatorData['femaleNames'] = femaleNamesResource["names"]
generatorData['maleNames'] = maleNamesResource["names"]
generatorData["familyNames"] = ["Blackwood", "Constellia", "Sou", None]
generatorData.update(gender = ["Female", "Male"])
generatorData['greeting'] = ['Hey', "Hi", "Hello", "Good Morning", "May Sou shine upon you", "Oh it's you", "Morning!", "Mornin\'", "Ciao", "Hello luv'", "Hey Pumpkin", "Morning Sweetheart", "Hi Dearie"]

 ############################################################## So it can be kept updated in file
# print ("###################")
# print ("This is the updated data file:")
# print ("This is the updated list to generate")
# print (json.dumps(toGenerate,  indent = 4))
# print ("This is the updated current data file:")
# print (json.dumps(generatorData,  indent = 4))

with open("Generator/toGenerate.json", 'w') as outfile:
    json.dump(toGenerate, outfile, ensure_ascii=False)

with codecs.open("Generator/consolidatedGeneratorResource.json", 'w', encoding="utf-8") as outfile:
    json.dump(generatorData, outfile, ensure_ascii=False)
