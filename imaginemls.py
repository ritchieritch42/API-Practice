#import the requests module
import requests

#make a request to imaginemlsapi
mytoken = '<6i7vrctwatjkc49lrzml2nz9q>'
myurl = '<https://sparkplatform.com>'
head = {'Authorization': 'token {}'.format(mytoken)}
response = requests.get(myurl, headers=head)

print(response)