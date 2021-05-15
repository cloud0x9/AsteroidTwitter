"""
make calls to the NASA API to retrieve astroid data and make sense of it
last update by Ilyass on 5/14/21
"""
import requests
import json
from datetime import date

#get today's date and make an API call to NASA with it to get todays astroid data
todays_date = str(date.today())
URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
params = {
  'api_key': 'DEMO_KEY',
  'start_date': todays_date,
  'end_date': todays_date
}
#read in the JSON response from NASA
response = requests.get(URL_NeoFeed, params=params).json()
rdump = json.dumps(response)
rload = json.loads(rdump)

#extract the total number of asteroids from the NASA JSON
def getNumAstro():
  # get total number of astroiods
  element_count = rload['element_count']
  return element_count

#extract the total number of asteroids that are deemed dangerous from the NASA JSON
def getNumHazAstro():
  ###get number of hazordous astrouous
  counter = 0
  for x in range(getNumAstro()):
    if rload['near_earth_objects'][todays_date][x]['is_potentially_hazardous_asteroid'] == True:
      counter += 1
  return counter

#take the data extracted from NASA and make sense of it by putting it into a sentence so it can be posted to twitter
def getAstroSentence():
  AstroSum = "Today there are a total of "+ str(getNumAstro()) + " asteroids near earth according to @NASA , of those " + str(getNumAstro())  + " asteroids , "+ str(getNumHazAstro()) + " are deemed hazardous"
  return AstroSum


