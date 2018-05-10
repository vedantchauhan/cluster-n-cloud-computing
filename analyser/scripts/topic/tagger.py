import re
from crawler.config import smoke_file,crime_file,cricket_file,afl_file


def loadTopicFiles(param):
    file = open(param, "r")
    topics = []
    for topic in file:
        topics.append(topic.strip())
    topics = set(topics)
    return topics


def containTopic(topics, text):
    # text = text.split(' ')
    text = [word.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
            for word in text.split(' ')]

    for word in text:
        if word.lower() in topics:
            return True
    return False

class Tagger():

    def topic_tagger(self,text):
        topics = loadTopicFiles(smoke_file)  # smoke
        if not containTopic(topics, text):
            topics = loadTopicFiles(crime_file)  # crime
            if not containTopic(topics, text):
                topics = loadTopicFiles(cricket_file)  # cricket
                if not containTopic(topics, text):
                    topics = loadTopicFiles(afl_file)  # footy
                    if not containTopic(topics, text):
                        topic = ""
                    else:
                        topic = "afl"
                else:
                    topic = "cricket"

            else:
                topic = "crime"
        else:
            topic = "tobacco"
        return topic