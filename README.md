#   A study among cities in Australia by leveraging NECTAR (AWS like cloud) cloud-based solutions, AURIN and tweets   #

#   Description
A study among cities in Australia by leveraging NECTAR[1] cloud-based solutions,  AURIN[2] and tweets[3]

#   Video Link
https://www.youtube.com/watch?v=wCEoxUTgxkg&feature=youtu.be

#   Website
-   visit our website
-   main:
    -   http://115.146.92.98:5002/index
-   backup:
    -   http://115.146.95.31:5002/index
    -   http://115.146.92.67:5002/index
    -   http://115.146.95.239:5002/index
49
#   Source Code Directory
-   ansible
    -   automation scripts
-   analyser
    -   scripts
        -   harvester
        -   topic
        -   aurin
        -   database
        -   sentiment
    -   corpora
        -   nltk twitter sample
        -   sent140
        -   stopwords
    -   sample
        -  sample couchDB document 
-   couchdb
    -  map/reduce scripts
-   web
    -   app.py
    
#   Test Embedded Analyser
    go to analyzer/scripts
    >python3 run_crawler.py jiyu
    
#   Sentiment Classification Evaluation
    got to analyzer/scripts/sentiment
    >python3 evaluation.py
    this will show a demo evaluation of baseline and our classifier on nltk twitter sample
    
#   Contributors
-   Jiyu Chen: https://github.com/freddieMe
    -   tweet crawler, duplication prevention, sentiment analysis, tweet analyser, scenario creation

-   Siddharth Malhotra: https://github.com/SiddharthMalhotra
    -   Contribution: ansible, boto, cloud architecture design, scenario creation

-   Vedant Chauhan: https://github.com/vedantchauhan
    -   Contribution: web, UI, leveraging aurin, scenario creation and implementation

-   Shashank Parab: https://github.com/Shashank830132
    -   Contribution: leveraging aurin, scenario creation

-   Nikhil Chitale: https://github.com/NikhilChitale
    -   Contribution: couchDB map/reduce as view creation, scenario creation
    
#   Reference
    [1]   NECTAR: https://nectar.org.au
    [2]   AURIN: https://aurin.org.au
    [3]   Twitter API: https://developer.twitter.com
    [3]   Sent140. Twitter Sentiment Corpus by Niek Sanders http://help.sentiment140.com/for-students/
    [4]   Klokan Technologies. http://boundingbox.klokantech.com.
    [5]   Textblob. http://textblob.readthedocs.io/en/dev.
    [6]   CouchDB. http://docs.couchdb.org/en/2.1.1.
    [8]   ANSIBLE. http://docs.ansible.com.
    [9]   BOTO. https://boto3.readthedocs.io/en/latest.
    [10]  Docker. https://github.com/redgeoff/docker-ce-vagrant.
    [11]  CouchDB in Docker Container. https://github.com/redgeoff/redgeoff-couchdb-docker.

    
    








