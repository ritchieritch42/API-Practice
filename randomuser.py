#import the requests module
import requests

#make a request to the random user api
response = requests.get('https://randomuser.me/api')

#test that the api is working ~ look for '200' value
print(response.status_code)

#format the api data with json
print(response.json())

#requests and assign variables
gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']

firstname = response.json()['results'][0]['name']['first']

lastname = response.json()['results'][0]['name']['last']

age = response.json()['results'][0]['dob']['age']

#print the variables of the individual
print(f'{title}. {firstname} {lastname}')
print(f'Age: {age}')