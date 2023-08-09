#import the requests module
import requests

#make a request to the random fox api
response = requests.get("https://randomfox.ca/floof")

#format the response with json
fox = response.json()

#print the url for the image of the fox
print(fox['image'])