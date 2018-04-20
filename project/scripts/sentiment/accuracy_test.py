from nltk.corpus import twitter_samples
from sentAnalyse import SentAnalyse
from textblob import TextBlob

# accuracy test of our classifier

positive_tweets = twitter_samples.tokenized("positive_tweets.json")   # 5000 labelled postitive tweets
negative_tweets = twitter_samples.tokenized("negative_tweets.json")   # 5000 labelled negative tweets



"""
after testing our method with baseline'
it seems the baseline have a higher accuracy of 98% in classifying positive and 94% in classifying negative

Therefore, we will take baseline as sentiment analyzer
"""


print(len(positive_tweets))


analyser = SentAnalyse()

# our method


pos = 0
neg = 0

false_positive = 0


for line in positive_tweets:
    polarity, subjectivity = analyser.get_sent_score(line)
    if polarity > 0:
        pos += 1
    else:
        false_positive += 1
        
        
for line in negative_tweets:
    polarity, subjectivity = analyser.get_sent_score(line)
    if polarity < 0:
        neg +=1
    else:
        false_positive += 1
        
        
#neg = 0
acc_pos = pos / 5000
acc_neg = neg / 5000

precision = false_positive / 10000

print("accuracy of classifying positive:")
print(acc_pos)

print("accuracy of classifying negative:")
print(acc_neg)

print("precision")
print(precision)


# baseline


pos = 0
neg = 0

false_positive = 0

for line in positive_tweets:
    line = ' '.join(line)
    text = TextBlob(line)
    score = text.sentiment
    polarity = score.polarity
    if polarity > 0:
        pos += 1
    else:
        false_positive += 1
     
        
for line in negative_tweets:
    line = ' '.join(line)
    text = TextBlob(line)
    score = text.sentiment
    polarity = score.polarity
    if polarity < 0:
        neg += 1
    else:
        false_positive += 1
        
        


        
    
        
acc_pos = pos / 5000
acc_neg = neg / 5000

precision = 1 - false_positive / 10000

print("accuracy of classifying positive:")
print(acc_pos)

print("accuracy of classifying negative:")
print(acc_neg)

print("precision")
print(precision)
    
