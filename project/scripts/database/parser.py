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
            "_id":status.id_str,
            "id_str":status.id_str,
            "coordinates":status.coordinates,
            "place":{
                "id":status.place.id,
                "url":status.place.url,
                "place_type":status.place.place_type,
                "name":status.place.name,
                "full_name":status.place.full_name,
                "country_code":status.place.country_code,
                "country":status.place.country
                },
            "lang":status.lang,
            "text":status.text,
            "sentiment":sentiment_score
        }
        return result
    
    
    def query_parse(self,status,sentiment_score):
        
        # filter out retweets
        try:
            if status.retweeted_status:
                return None
        except:
            pass
            
        result = {
            "_id":status["id_str"],
            "id_str":status["id_str"],
            "coordinates":status["coordinates"],
            "place":{
                "id":None,
                "url":None,
                "place_type":None,
                "name":status["location"],
                "full_name":status["location"],
                "country_code":"AU",
                "country":status["location"]
                },
            "lang":status["lang"],
            "text":status["text"],
            "sentiment":sentiment_score
        }
        return result    
        
        
        
        
        


