import json, random
from io import StringIO

try:
    with open("Generator/toGenerate.json", 'r') as f:
        toGenerate = json.load(f)
    with open("Generator/consolidatedGeneratorResource.json", "r") as f:
        generatorData = json.load(f)
except IOError:
    print("You need to use the Better Generator (run that file first)")

####### Load Character file
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup

### TODO give a set of names based on age
#Done: Give a different name list based on gender
#Done: if family is given then ensure first Name is 7 or more characters as Aristocratic? and give a middle name
def namePicker(gender, family = None):
    firstName = ""
    if family == None: #unimportant people
        lastName = random.choice(generatorData["lastNamesCommoner"])
        if gender == "Female":
            while len(firstName) > 7:
                firstName = random.choice(generatorData["femaleNames"])
        elif gender == "Male":
            while len(firstName) > 7:
                firstName = random.choice(generatorData["maleNames"])
        return firstName + " " + lastName
    # else:
    lastName = family
    if gender == "Female":
        while len(firstName) < 7: #TODO come up with better way of class separation than name length maybe name origin? from rome etc
            firstName = random.choice(generatorData["femaleNames"])
    elif gender == "Male":
        while len(firstName) < 7:
            firstName = random.choice(generatorData["maleNames"])

    midNameGetter = family + "MiddleNames"
    if midNameGetter in generatorData:
        listOfMiddleNamesAccordingToFam = generatorData[midNameGetter]
        middleName = random.choice(listOfMiddleNamesAccordingToFam)
    #Can try having variation on parent's names eventually.
    else:
        middleName = random.choice(generatorData["middleNames"])
    s = (firstName + " " + middleName + " " + lastName)
    return s





def doChoooseCharacter():
    currentCharacter = dict()
    for i in toGenerate:
        if i == "name":
            if ("gender" not in currentCharacter):
                # Doesn't contain the gender so give it one
                currentCharacter["gender"] = random.choice(generatorData["gender"])
            family = random.choice(generatorData["familyNames"])
            currentCharacter["name"] = namePicker(currentCharacter["gender"], family)
            # print (currentCharacter["gender"])
            # print (currentCharacter["name"])
        #TODO:
        elif (i not in currentCharacter): #if this key has not already been generated, generate
            try:
                currentCharacter[i] = random.choice(generatorData.get(i))
            except:
                print ("Error")
                print (i)
                print (generatorData.get(i))
    return currentCharacter


######################################################



try:
    with open("characterData.json", 'r') as f:
        characterData = json.load(f)
    #DONE add something so that when list of items to generate by changes, wipe file and start again
    #For new item to generate
    if len(characterData["Pamela"]) != len(toGenerate):
        characterData.clear() # actually this is kinda dangerous, coz if create lore then this happens?
    #TODO: For new len of stuff to generate --- wipe file and start again? OR BETTER: regenerate for that bit (take into account shiz) OR just don't regenerate, can add stuff but don't minus

    print ("This is the current Character data file:")
    print (json.dumps(characterData,  indent = 4))
    ###############################################
    ## Here is the code for choosing Character DATA ------!!!!
    currentCharacter = doChoooseCharacter()
except (ValueError, IOError):
    currentCharacter = dict(name = "Pamela", gender = "female", greeting = "Ciao")
    characterData = Vividict()
###############################
#So characters don't have duplicate names
while currentCharacter.get("name") in characterData:
    currentCharacter = doChoooseCharacter()
characterData[currentCharacter.get("name")] = currentCharacter
################
print ("This is the updated Character data file:")
# pprint.pprint(d)
s = json.dumps(characterData,  indent = 4)
print (s)

with open("characterData.json", 'w') as outfile:
    json.dump(characterData, outfile, ensure_ascii=False)
