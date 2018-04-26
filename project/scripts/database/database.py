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
        
        
    def save(self, database, record):
        
        #implement something to prevent duplication
        #
        #
        #
        print(record)
    
        # locate database
        db = self.couch[database]
        
        #prevent duplication
        if db.get(record["_id"]) is None:
            # save into couchdb
            db.save(record)        