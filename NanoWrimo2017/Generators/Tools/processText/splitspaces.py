import re, json, string


############# text with just spaces separating to json
# with open("/Users/Caffae/Desktop/processText/flower.json", "r") as f:
#     data = f.read()
# # split oliver
# words = re.split('\W+', data)
#
# myList = []
# for i in words:
#     if (i not in myList and i + "s" not in myList):
#         myList.append(i)
#
#
# with open("/Users/Caffae/Desktop/processText/flowers.json", 'w') as outfile:
#     json.dump(myList, outfile, ensure_ascii=False)

# with open("/Users/Caffae/Desktop/processText/flowers.json", 'r') as f:
#     myList = json.load(f)
#
# ans = []
# for i in myList:
#     if len(i) > 4 and i[-1] != 's' and "\'" not in i:
#         ans.append(string.capwords(i))
#
#
# with open("/Users/Caffae/Desktop/processText/flowers.json", 'w') as outfile:
#     json.dump(ans, outfile, ensure_ascii=False)

filename = "/Users/Caffae/Downloads/fakergem-2ec7c3dc6ab6203766c2a83360afc0dfd897bcdc/data/lorem.json"
with open(filename, 'r') as f:
    myList = json.load(f)

ans = []
for i in myList:
    ans.append(string.capwords(i))
    # if len(i) > 2 and "\'" not in i:
    #     ans.append(string.capwords(i))


with open(filename, 'w') as outfile:
    json.dump(ans, outfile, ensure_ascii=False)
