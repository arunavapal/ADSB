#Code by Arunava Pal.
#Main file to get data from Open Sky Network.

#Import required libraries
import requests
import json
from opensky_api import OpenSkyApi

url = "https://opensky-network.org/api/states/all?lamin=7.9655&lomin=7.9655&lamax=35.4940&lomax=97.4025"  #Define the URL to download the file
#traffic_data = requests.get(url)                    #Download file
#error = traffic_data.status_code                    #Check Status of download
traffic_data = json.loads(requests.get(url).text)
#Check whether page correctly downloaded
#if (error == 200):
print("Data succesfully retrieved.")
print(traffic_data)
#else:
    #print("The data could not be retrieved.")


#api = OpenSkyApi()
#s = api.get_states()
#print(s)
