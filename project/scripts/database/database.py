import couchdb
from crawler.config import couchdb_uri,db_admin,db_password
from couchdb import Session





class DButils():
    
    couch = None
    
    def __init__(self):
        # connect to couchdb
        try:
            self.couch = couchdb.Server(couchdb_uri)           
        except:
            try:
                auth = Session()
                auth.name = db_admin
                auth.password = db_password
                self.couch = couchdb.Server(couchdb_uri,session=auth)
            except Exception as e:
                print(e)
                return
        
        
    def save(self, database, record):
    
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
                print(record)
                db.save(record)
            except couchdb.HTTPError as e:
                print("ERROR: duplicate")