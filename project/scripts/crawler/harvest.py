
#fred
#comp90024


# change couchdb ip address before running
# python: 3.6.3
# run > python tweets_crawler.py


import tweepy
import sentiment.classifier as classifier
import json
from database import database
from crawler import harvestUtil
from database.parser import Parser
from crawler.config import app_auth,couchdb_uri,AUS_STR,db_name
import time
import sys
import nltk




class HarvestSys():
    def __init__(self):
        nltk.download('words')
        nltk.download('twitter_samples')

    
    
    def harvest(self):

        print("harvester started...")
        #default
        user = sys.argv[1]
        # set up
        try:
            auth = tweepy.OAuthHandler(app_auth[user].ckey, app_auth[user].csec)
        #auth = tweepy.AppAuthHandler(app_auth[user].ckey, app_auth[user].csec)
            auth.set_access_token(app_auth[user].atoken, app_auth[user].asec)
            print("connection started...")
            print(sys.argv[1]+" start crawling")
        except KeyError as e:
            print("ERROR: wrong admin name: "+sys.argv[1])
            exit(-1)
        
        # create an api object to pull data from twitter
        api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        stream_listener = harvestUtil.MyStreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

        
        # start with streamMode filter by city
        try:
            stream.filter(locations=AUS_STR,languages=["en"])  #location
        except ConnectionRefusedError:
            print("ERROR: stream connection failed")
            exit(-1)
        except FileNotFoundError as e:
            print(e)
            exit(-1)
        except Exception as e:
            # access time limit handling
            print(e)
            time.sleep(20)
        
 
        

        