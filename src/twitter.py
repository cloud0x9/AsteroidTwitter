"""
connect to twitter via the tweepy to makes posts on twitter
last update by Ilyass on 5/14/21
"""
import os
import tweepy as tw
import AstroNASA as an
import PicNASA as pn
import requests

#necessary keys and tokens to validate account identity (keys are REDACTED for safety)
consumer_key= 'REDACTED'
consumer_secret= 'REDACTED'
access_token= 'REDACTED'
access_token_secret= 'REDACTED'

#make the actual connection to twitter by passing keys and tokens to validate account identity
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#post to twitter the number of asteroids near earth and how many are potentially dangerous from NASA
def postAstroInfo():
    api.update_status(an.getAstroSentence())

#post a unique picture of space from NASA
#https://stackoverflow.com/questions/31748444/how-to-update-twitter-status-with-image-using-image-url-in-tweepy
def postAstroPic():
    if pn.checkMediaType():
        filename = 'temporary.jpg'
        request = requests.get(pn.picUrl(), stream=True)
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=pn.picTitle() + " by " + pn.picOwner())
        os.remove(filename)
