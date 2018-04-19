
#fred
#comp90024


# change stream_output_file path before run
# python: 3.6.3
# run > python tweets_crawler.py


import tweepy
from twitter import *

TWITTER_KEY = "985778410898124800-kNVBSiLMIWRILWlGR71zk8HCl6IllEo"
TWITTER_SECRET = "ttLXW3R5rC3MMXMwbq7irCf9GcAhIOV9i3Pz1VhmS9IaP"
TWITTER_APP_KEY = "se7dR9OJzvcJdG9nO6g9VVpKE"
TWITTER_APP_SECRET = "0iJSVbUVN2OPOSPy3KJQdQP3Q0iGvyZfHAMQXKwce03tfO5PYk"

stream_output_file = "/Users/alfredgordon/Documents/cluster/tweets/stream.json"      # change file path during test


# Melbourne
# geo coordinates are fetched through http://boundingbox.klokantech.com  format: CSV RAW
MELBOURNE = [144.6550006954,-38.5089967291,145.3498310249,-37.5916213868]      # streamAPI(box)

latitude = -37.8136276	        # geographical centre of search                # searchAPI(circle)
longitude = 144.96305759999996	# geographical centre of search
max_range = 5 			# search range in kilometres






# setting up listener by override
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        # change this code to store data into CouchDB
        file = open(stream_output_file,"a")
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return 
        except:
            pass
        
        # filter out location
        print(status.text)
        
        # store data into database
        file.write(str(status.text.encode('utf-8')).strip())
        file.close()
        return True
        
    # error: disconnect stream and start using SearchAPI    
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
    while True: 
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100)
        for result in query["statuses"]:
            #-----------------------------------------------------------------------
            # only process a result if it has a geolocation
            #-----------------------------------------------------------------------
            #if result["geo"]:
                try:
                    
                    # filter out retweets
                    if result["retweeted_status"]:
                        continue
                except:
                    pass
                
                user = result["user"]["screen_name"]
                text = result["text"]
                
                #latitude = result["geo"]["coordinates"][0]
                #longitude = result["geo"]["coordinates"][1]
    
                #-----------------------------------------------------------------------
                # now write this row to json file (connect to couchDB)
                #-----------------------------------------------------------------------
                file = open(stream_output_file,"a")
                file.write(str(text.encode('utf-8')).strip())
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
        SearchMode()