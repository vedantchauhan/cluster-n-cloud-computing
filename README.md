# comp90024 cluster and cloud computing team 49

# our project

A study among cities in Australia by leveraging NECTAR[1] cloud-based solutions,  AURIN[2] and tweets[3]

# Video Link
https://www.youtube.com/watch?v=wCEoxUTgxkg&feature=youtu.be

# web
visit our website
main:
http://115.146.92.98:5002/index
backup:
http://115.146.95.31:5002/index
http://115.146.92.67:5002/index
http://115.146.95.239:5002/index

# project directory
-   ansible
    -   automation scripts
-   analyser
    -   harvester
    -   topic
    -   aurin
    -   database
    -   sentiment
-   couchdb
    -  map/reduce scripts
-   web
    -   UI
    
# run crawler
    go to analyzer/scripts
    >python3 run_crawler.py jiyu
    
# sentiment evaluation
    got to analyzer/scripts/sentiment
    >python3 evaluation.py
    
#   reference
    -[1]   NECTAR: https://nectar.org.au
    -[2]   AURIN: https://aurin.org.au
    -[3]   Twitter API: https://developer.twitter.com








