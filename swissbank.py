#import the requests module
import requests

#make a request to the swiss bank api
data = requests.get('https://data.snb.ch/api/cube/amarbma/data/csv/en').text

#ask for the most recent unemployment rate
datatext = str(data).splitlines()[-6].split(';')

#format the unemployment rate to a floating number with the quotations
rate = float(datatext[2].replace('"',''))

#print the unemployment rate
print(rate)