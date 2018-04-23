import json


class Parser():
    
    def status_parse(self,status,sentiment_score):
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return None
        except:
            pass
            
        result = {
            "coordinates":status.coordinates,
            "place":status.place,
            "lang":status.lang,
            "text":status.text,
            "sentiment":sentiment_score
        }
        return result
        
        
    
    @staticmethod
    def parse_to_json(self,json_object):
        response = {
            "_id": json_object["id_str"],
                    "user": {
                        "name": json_object["user"]["name"],
                        "screen_name": json_object["user"]["screen_name"],
                        "followers_count": json_object["user"]["followers_count"],
                        "location": json_object["user"]["location"],
                        "description": json_object["user"]["description"],
                        "statuses_count": json_object["user"]["statuses_count"],
                        "friends_count": json_object["user"]["friends_count"],
                        "listed_count": json_object["user"]["listed_count"]
                        },
                    "geo": {
                        "coordinates": json_object["coordinates"]["coordinates"] if json_object["coordinates"] else None
                        },
                    "content": {
                        "text": json_object["text"],
                        "entities": json_object["entities"],
                        "lang": json_object["lang"]
                        },
                    "about": {
                        "retweet_count": json_object["retweet_count"],
                        "source": json_object["source"],
                        "favorite_count": json_object["favorite_count"]
                        },
                    "timestamp": {
                        "created_at_str": json_object["created_at"],
                        "created_at_timestamp": time.mktime(
                            datetime.strptime(json_object["created_at"], "%a %b %d %H:%M:%S +0000 %Y").timetuple())
                    }
        }
        return response        
        
        


