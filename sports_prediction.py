#Step 2: import the necessary libraries
import requests
import pandas as pd
import json

#Step 3: store the api key in a private folder

#Step 4: retrieve the api key from the private folder
# Function to retrieve api_key
def get_keys(path):
    with open(path) as f:
        return json.load(f)
# Retrieve api_key from local stored location
keys = get_keys("/Users/chirag/Downloads/Grind/Python/PythonProjects/api_football.json")
api_key = keys['api_key']

#Step 5: Determine which endpoint URL you need, and make a “GET” request
#determine URL endpoint
url = "https://api-football-v1.p.rapidapi.com/v2/leagues/seasonsAvailable/524"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }
resp = requests.request("GET", url, headers=headers)
#check if the request was successful
resp.status_code == requests.codes.ok
#check raw data response
print(resp.text)

#Step 6: Convert json to Pandas Dataframe
resp.json().keys() #checks the keys of the reponse
resp.json()['api'].keys() # Check keys at next level of response
leagues_dict = resp.json()['api']['leagues'] # Create dictionary of results for 'leagues' key
leagues_df = pd.DataFrame.from_dict(leagues_dict) # Visualize df for all English Premier league seasons available
leagues_df.head(10) #prints the first x lines of the dataframe



