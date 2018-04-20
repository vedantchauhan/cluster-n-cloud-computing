import nltk
from nltk.stem import WordNetLemmatizer  
from nltk.corpus import words
import re





def tokenize(text):
    text = text.split()
    return text

def lemmatize(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    text = [x.lower() for x in text]
    text = [rmRepeatCharacters(x) for x in text]
    text = [wordnet_lemmatizer.lemmatize(x) for x in text]
    text = [replaceTags(x) for x in text]
    return text

def rmRepeatCharacters(word):
    # look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", word)

# replace tags such as mentioned tweeters(@), hashtags(#), URL
def replaceTags(text):
        # Convert www.* or https?://* to URL
    text = re.sub('^((www\.[^\s]+)|(https?://[^\s]+))', '<URL>', text)
        # Convert @username to AT_USER
    text = re.sub('^@[^\s]+', '<USER>', text)
        # Replace hashtag #word with the word
    text = re.sub(r'^#([^\s]+)', '<HASHTAG>', text)
        # Remove additional white spaces
    text = re.sub('^[\s]+', ' ', text)
        # trim
    text = text.strip('\'"')
    return text
    


def rmStopword(text,stopwords):
    filtered = []
    for word in text:
        if not stopwords.get(word):
            filtered.append(word)
        
        
    return filtered


def BOW_feature(text):
    bow = []
    for w in text:
        
        # strip puntuations
        w = w.strip('\'"?,.')
        bow.append(w)
        
    parsed_text = ' '.join(bow)
    return parsed_text
           
    
def stop_word_dict(stopwords):
    """construct a look-up dictionary for stopwords
    and decrease the search complexity to O(1)
    para: stopwords: a list of stopwords
    return: d(stopwords): dictionary format stopwords  
    """
    d = {}
    for word in stopwords:
        d[word] = d.get(word,0) + 1
        
    print("stopwords lookup ready")
    return d
    


class Preprocess():
    
    stopwords = {}
    
    def __init__(self):
        print("start preprocess tweets")
        #wordlist = words.words()
        #self.stopwords = stop_word_dict(wordlist)
    
    def process(self,text):
        try:
            text = tokenize(text)
        except:
            pass
        
        text = lemmatize(text)
        
        #text = rmStopword(text, self.stopwords)
        #print(text)
        
        text = BOW_feature(text)
        return text
    