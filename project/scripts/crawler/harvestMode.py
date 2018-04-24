
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
from crawler import streamHarvest
from database.parser import Parser
from crawler.config import app_auth,couchdb_uri,MELBOURNE_STR,MELBOURNE_SRC,db_name



class HarvestSys():
    def __init__(self):
        pass
    
    
    def StreamMode(self):
        print("on stream...")
        #default
        user = 'jiyu'
        
        # set up
        auth = tweepy.OAuthHandler(app_auth[user].ckey, app_auth[user].csec)
        auth.set_access_token(app_auth[user].atoken, app_auth[user].asec)
        
        # create an api object to pull data from twitter
        api = tweepy.API(auth)
        stream_listener = streamHarvest.MyStreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
        
        # start with streamMode filter by city
        stream.filter(locations=MELBOURNE_STR,languages=["en"])    
        
            
    def SearchMode(self):
        print("on search...")
        
        #connect to couchdb
        db = database.DButils()
        
        # create sentiment analyser
        cl = classifier.Baseline()
        
        # tweets parser
        parser = Parser()
        
        #set up
        user = 'jiyu'
        geotag = MELBOURNE_SRC
        
        # create an api object to pull data from twitter
        twitter = Twitter(auth = OAuth(app_auth[user].atoken, app_auth[user].asec,app_auth[user].ckey, app_auth[user].csec))
        # query 100 tweets at a time
        while True: 
            query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (geotag[0], geotag[1], geotag[2]), count = 100)


            
            for result in query["statuses"]:
                
                print(result)
                
                # store tweets in json
                record = {}
    
                try:
                        
                    # filter out retweets
                    if result["retweeted_status"]:
                        continue
                except:
                    pass
                
                # perform sentiment analysis n store scores to json
                polarity, subjectivity, label = cl.get_sent_score(result["text"])
                sent = {
                    'polarity':str(polarity), 
                    'subjectiviy':str(subjectivity),
                    'label':label
                }
              
                #result = json.dumps(result)
                record = parser.query_parse(result,sent)
                if record is None:
                    return
                
                # save into couchdb
                db.save(db_name,record)                
                
        
        

        