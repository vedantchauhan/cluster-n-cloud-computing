from textblob import TextBlob
from preprocess import Preprocess


class Baseline():
    
    def __init__(self):
        pass
    
    def get_sent_score(self,text):
        text = TextBlob(text)
        score = text.sentiment
        polarity = score.polarity
        subjectivity = score.subjectivity
        if polarity > 0:
            label = 'Positive'
        elif polarity == 0:
            label = 'Neutral'
        elif polarity < 0:
            label = 'Negative'
        
        return polarity,subjectivity,label
    
    
    
class MyClassifier():
    
    def __init__(self):
        pass
    
    def get_sent_score(self,text):
        proc = Preprocess()
        text = proc.process(text)
        blob = TextBlob(text)
        score = blob.sentiment
        return score.polarity, score.subjectivity    


       