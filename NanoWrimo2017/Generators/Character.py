import json, random
from io import StringIO

with open("generatorData.txt", 'r') as f:
    generatorData = json.load(f)

# print ("This is the current data file:")
# s = json.dumps(generatorData,  indent = 4)
# print (s)

############################################################ Definitions
#This is where you make the character generator pick from generatorData
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup


def namePicker(gender):
    ans = ""
    if gender == "female":
        ans = random.choice(generatorData["femaleNames"])
        print(ans)
    elif gender == "male":
        ans = random.choice(generatorData["maleNames"])
        print(ans)
    # print (ans)
    return ans


######################################################

try:
    with open("characterData.txt", 'r') as f:
        characterData = json.load(f)
    # characterData.clear()
    print ("This is the current Character data file:")
    s = json.dumps(characterData,  indent = 4)
    print (s)
    ###############################################
    ## Here is the code for choosing Character DATA ------!!!!
    currentCharacter = dict()
    for key, value in generatorData.items():
        if (key == "femaleNames" or key == "maleNames"):
            pass
        if key == "name":
            if ("gender" not in currentCharacter):
                # Doesn't contain the gender so give it one
                currentCharacter["gender"] = random.choice(generatorData["gender"])
            ### TODO give a set of names based on age
            #Done: Give a different name list based on gender
            currentCharacter["name"] = namePicker(currentCharacter["gender"])
            # print (currentCharacter["gender"])
            print (currentCharacter["name"])
        elif (key not in currentCharacter): #if this key has not already been generated, generate
            currentCharacter[key] = random.choice(value)
except ValueError:
    currentCharacter = dict(name = "Pamela", gender = "female", greeting = "Ciao")
    # characterData = collections.defaultdict(dict)
    characterData = Vividict()
###############################
characterData[currentCharacter.get("name")]  = "placeholder"
characterData[currentCharacter.get("name")] = (currentCharacter)
################
print ("This is the updated Character data file:")
# pprint.pprint(d)
s = json.dumps(characterData,  indent = 4)
print (s)

with open("characterData.txt", 'w') as outfile:
    json.dump(characterData, outfile, ensure_ascii=False)
