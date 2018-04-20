
import tweepy
import classifier
import database




# setting up listener by override
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        db = database.DButils()
        
        cl = classifier.Baseline()
        
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
        
        polarity, subjectivity, label = cl.get_sent_score(status.text)
        sent = {'polarity':str(polarity), 'subjectiviy':str(subjectivity),'label':label}
        record['sentiment_score'] = sent
        
        
        # save into couchdb
        db.save('tweets',record)
        return True