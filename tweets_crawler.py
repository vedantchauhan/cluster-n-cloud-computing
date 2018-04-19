
#fred
#comp90024


# change couchdb ip address before running
# python: 3.6.3
# run > python tweets_crawler.py


import tweepy
from twitter import *
from textblob import TextBlob
import json
import couchdb

TWITTER_KEY = "985778410898124800-kNVBSiLMIWRILWlGR71zk8HCl6IllEo"
TWITTER_SECRET = "ttLXW3R5rC3MMXMwbq7irCf9GcAhIOV9i3Pz1VhmS9IaP"
TWITTER_APP_KEY = "se7dR9OJzvcJdG9nO6g9VVpKE"
TWITTER_APP_SECRET = "0iJSVbUVN2OPOSPy3KJQdQP3Q0iGvyZfHAMQXKwce03tfO5PYk"

COUCHDB_ADDR = "http://127.0.0.1:5984"      # change file path during test


# Melbourne
# geo coordinates are fetched through http://boundingbox.klokantech.com  format: CSV RAW
MELBOURNE = [144.6550006954,-38.5089967291,145.3498310249,-37.5916213868]      # streamAPI(box)

latitude = -37.8136276	        # geographical centre of search                # searchAPI(circle)
longitude = 144.96305759999996	# geographical centre of search
max_range = 5 			# search range in kilometres






# setting up listener by override
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        # store tweets in json format
        record = {}
        
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return 
        except:
            pass
        
        # store text in json
        record['text'] = status.text
        print(status.text)
        
        
        # perform sentiment analysis n store scores to json
        blob = TextBlob(status.text)
        score = blob.sentiment
        sent = {'polarity':str(score.polarity), 'subjectiviy':str(score.subjectivity)}
        print(score)
        record['sentiment_score'] = sent
        
        
        # connect to couchdb
        couch = couchdb.Server(COUCHDB_ADDR)
        print(record)
        
        # locate database
        db = couch['tweets']
        
        # save into couchdb
        db.save(record)
        return True
        
    # error: disconnect stream   
    def on_error(self, status_code):
        return False
        
        
def StreamMode():
    # set up
    auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
    auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
    
    # create an api object to pull data from twitter
    api = tweepy.API(auth)
    
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    
    # start with streamMode
    stream.filter(locations=MELBOURNE,languages=["en"])    
    
        
def SearchMode():
    latitude = -37.8136276	        # geographical centre of search                # searchAPI(circle)
    longitude = 144.96305759999996	# geographical centre of search
    max_range = 5 			# search range in kilometres    
    
    
    # create an api object to pull data from twitter
    twitter = Twitter(auth = OAuth(TWITTER_KEY,TWITTER_SECRET,TWITTER_APP_KEY,TWITTER_APP_SECRET))
    
    # query 100 tweets at a time
    while True: 
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100)
        for result in query["statuses"]:
            # store tweets in json
            record = {}

            try:
                    
                # filter out retweets
                if result["retweeted_status"]:
                    continue
            except:
                pass
                
            user = result["user"]["screen_name"]
            text = result["text"]
                
            
                
            # store text in json
            record['text'] = text
            print(text)
            
            # perform sentiment analysis n store scores to json
            blob = TextBlob(text)
            score = blob.sentiment
            sent = {'polarity':str(score.polarity), 'subjectiviy':str(score.subjectivity)}
            print(score)
            record['sentiment_score'] = sent
            
            
            # connect to couchdb
            couch = couchdb.Server(COUCHDB_ADDR)
            print(record)
            
            # locate database
            db = couch['tweets']
            
            # save into couchdb
            db.save(record)                
            print(text)
            

    
if __name__ == '__main__':
    """
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    
    # start with streamMode
    stream.filter(locations=MELBOURNE,languages=["en"])
    """
    try:
        StreamMode()
        #SearchMode()
    except:
        #print("Start SearchMode")
        SearchMode()
        