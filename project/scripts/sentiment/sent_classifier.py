
from textblob import TextBlob
from preprocess import Preprocess



class SentAnalyse():
    
    proc = None
    
    def __init__(self):
        self.proc = Preprocess()
        pass
    
    def get_sent_score(self,text):
        
        text = self.proc.process(text)
        blob = TextBlob(text)
        score = blob.sentiment
        
        return score.polarity, score.subjectivity