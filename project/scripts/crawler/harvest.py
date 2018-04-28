
#fred
#comp90024


# change couchdb ip address before running
# python: 3.6.3
# run > python tweets_crawler.py


import tweepy
from twitter import *
import sentiment.classifier as classifier
import json
from database import database
from crawler import harvestUtil
from database.parser import Parser
from crawler.config import app_auth,couchdb_uri,AUS_STR,db_name




class HarvestSys():
    def __init__(self):
        pass
    
    
    def harvest(self):
        print("harvester started...")
        #default
        user = 'jiyu'
        
        # set up
        auth = tweepy.OAuthHandler(app_auth[user].ckey, app_auth[user].csec)
        auth.set_access_token(app_auth[user].atoken, app_auth[user].asec)
        
        # create an api object to pull data from twitter
        api = tweepy.API(auth)
        stream_listener = harvestUtil.MyStreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        
        # start with streamMode filter by city
        try:
            stream.filter(track=['north korea','nuclear','donald trump','donald','trump'],locations=AUS_STR)
        except ConnectionRefusedError:
            print("ERROR: couchDB is not running")
            return
        
 
        

        