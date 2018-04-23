
import tweepy
from sentiment import classifier
from database import database

from crawler.config import db_name
from database.parser import Parser




# setting up listener by override
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #setup
        db = database.DButils()
        cl = classifier.MyClassifier()
        parser = Parser()
        
        
        # perform sentiment analysis n store scores to json
        polarity, subjectivity, label = cl.get_sent_score(status.text)
        sent = {
            'polarity':str(polarity), 
            'subjectiviy':str(subjectivity),
            'label':label
        }
      
        
        record = parser.status_parse(status,sent)
        if record is None:
            return
        
        print(record)
        
        """
        
        
        
        
        # save into couchdb
        db.save(db_name,record)
        """
        return True