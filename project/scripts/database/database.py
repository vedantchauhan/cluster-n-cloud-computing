import couchdb
from crawler.config import couchdb_uri
from couchdb import Session





class DButils():
    
    couch = None
    
    def __init__(self):
        # connect to couchdb
        try:
            self.couch = couchdb.Server(couchdb_uri)
        except:
            print("ERROR: couchDB is not running")
            return
        
        
    def save(self, database, record):
        
        #implement something to prevent duplication
        #
        #
        #
        print(record)
    
        # locate database
        try:
            db = self.couch[database]
        except couchdb.http.ResourceNotFound:
            print("No database: "+database)
            print("try to create database on: "+str(couchdb_uri))
            try:
                auth = Session()
                auth.name = input("Enter your couchdb username: ")
                print(auth.name)
                auth.password = input("Enter your couchdb password: ") 
                self.couch = couchdb.Server(couchdb_uri,session=auth)           
                self.couch.create(database)
                db = self.couch[database]                
            except couchdb.http.Unauthorized as e:
                print("ERROR: unauthorized")
                return
        
        #prevent duplication
        if db.get(record["_id"]) is None:
            # save into couchdb
            try:
                db.save(record)
            except couchdb.HTTPError as e:
                print("ERROR: duplicate")