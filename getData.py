#Author : Arunava Pal.

#Main file to get data from Open Sky Network.

#Import required libraries
import requests
import json

#Define the URL to download the file
url = "https://opensky-network.org/api/states/all?lamin=7.9655&lomin=7.9655&lamax=35.4940&lomax=97.4025"
traffic_data = json.loads(requests.get(url).text)


print("Data succesfully retrieved.")
print(traffic_data)
