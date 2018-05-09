import json
import couchdb


server = couchdb.Server('http://admin:admin@172.17.0.3:5984')
db = server["tweets"]

with open('mapreduce.json', 'r') as f:
    db.save(json.load(f))