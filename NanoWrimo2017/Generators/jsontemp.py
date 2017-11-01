from pprint import pprint
import json, random
################### Json from url?json
# try:
#     # For Python 3.0 and later
#     from urllib.request import urlopen
# except ImportError:
#     # Fall back to Python 2's urllib2
#     from urllib2 import urlopen
#
# def get_jsonparsed_data(url):
#     """
#     Receive the content of ``url``, parse it as JSON and return the object.
#
#     Parameters
#     ----------
#     url : str
#
#     Returns
#     -------
#     dict
#     """
#
#
#     response = urlopen(url)
#     try:
#         data = response.read().decode("utf-8")
#         return json.loads(data)
#     except ValueError:
#         return "Error"
#
# url = ("https://www.fanfiction.net/book/Harry-Potter/?&srt=4&lan=1&r=10&len=60&s=2&p=4")
# # print(get_jsonparsed_data(url))
#
# pprint(get_jsonparsed_data(url))
##########################

## Import a Json list


# ################ LOAD json
#prompt the user for a file to import
filename = "Resource/Names/MaleYoung.json"

#Read JSON data into the datastore variable
with open(filename, 'r') as f:
    datastore = json.load(f)

#Use the new datastore datastructure
print (datastore["names"])
# print (random.choice(datastore["names"]))
