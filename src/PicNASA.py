"""
make calls to the NASA API to retrieve a unique picture of space
last update by Ilyass on 5/14/21
"""
import requests
import json

#prepare to make the API call by setting up the parameters
URL_NeoFeed = "https://api.nasa.gov/planetary/apod"
params = {
  'api_key': 'DEMO_KEY',
}
#make the actual API call and read the JSON response in
response = requests.get(URL_NeoFeed, params=params).json()
rdump = json.dumps(response)
rload = json.loads(rdump)

#get the picture description from the NASA JSON API response
def getPicInfo(elementName):
  picInfo = rload[elementName]
  return picInfo

#get the url to the image from the NASA JSON API response
def picUrl():
  return getPicInfo('hdurl')

#get the picture name from the NASA JSON API response
def picTitle():
  return getPicInfo('title')

#get the photographer of the photo from the NASA JSON API response
def picOwner():
  return getPicInfo('copyright')

#make sure that the daily media from the API is a image only (sometimes the API returns videos)
def checkMediaType():
  if getPicInfo('media_type')=="image":
    return True




