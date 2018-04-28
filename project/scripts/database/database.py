import couchdb
from crawler.config import couchdb_uri




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
<<<<<<< HEAD
            db = self.couch[database]
        except couchdb.http.ResourceNotFound:
            print("No database: "+database)
            print("try to create database on: "+str(couchdb_uri))
            try:
                self.couch.create(database)
                db = self.couch[database]
            except couchdb.http.Unauthorized as e:
                print("ERROR: unauthorized")
                return
              
               
        
=======
            if database not in self.couch:
                self.couch.create(database)
                db = self.couch[database]
            else:
                db = self.couch[database]
        except:
            print("Error: Finding the database")

>>>>>>> 352408415b8c713092f8724124d340b6b7fa904f
        #prevent duplication
        if db.get(record["_id"]) is None:
            # save into couchdb
            try:
                db.save(record)
            except couchdb.HTTPError as e:
                print("ERROR: duplicate")