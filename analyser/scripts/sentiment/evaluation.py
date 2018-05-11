import nltk

from nltk.corpus import twitter_samples
import classifier as cl
from sklearn import metrics
import re


# accuracy test of our classifier

positive_tweets = twitter_samples.tokenized("positive_tweets.json")   # 5000 labelled postitive tweets
negative_tweets = twitter_samples.tokenized("negative_tweets.json")   # 5000 labelled negative tweets





"""
after testing our method with baseline'
it seems the baseline have an accuracy of 96.32%

Our method result in an accuracy of 98.41%

"""



print(len(positive_tweets))
gold_standard = []
for i in range(5000):
        gold_standard.append("Positive")
for i in range(5000):
        gold_standard.append("Negative")

      
    
def print_metrices(y_test,y_pred_class_nb):
    print("Accuracy:")
    print(metrics.accuracy_score(y_test,y_pred_class_nb))


    print("\nAverage precision:")
    print(metrics.precision_score(y_test,y_pred_class_nb,average='macro'))


    print("\nAverage recall:")
    print(metrics.recall_score(y_test,y_pred_class_nb,average='macro'))

    
    print("\nAverage f1:")
    print(metrics.f1_score(y_test,y_pred_class_nb,average='macro'))


    print("\nClassification report:")
    print(metrics.classification_report(y_test, y_pred_class_nb))
    

def classification(positive_tweets,negative_tweets,classifier):

    predict = []
    for line in positive_tweets:
        
        print(line)
        pol,sub,label = classifier.get_sent_score(line)
        predict.append(label)
    
    for line in negative_tweets:
        
        print(line)
        pol,sub,label = classifier.get_sent_score(line)
        predict.append(label)
        
    print(predict)    
    print_metrices(gold_standard,predict)
    
    
    





baseline = cl.Baseline()
classifier = cl.MyClassifier()


#baseline
print("baseline:")
classification(positive_tweets,negative_tweets,baseline)


#out classifier
print("our classifier:")
classification(positive_tweets,negative_tweets,method)


        
        

    




    
