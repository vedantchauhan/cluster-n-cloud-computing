import couchdb
from crawler.config import couchdb_uri




class DButils():
    
    couch = None
    
    def __init__(self):
        # connect to couchdb
        self.couch = couchdb.Server(couchdb_uri)
        
        
    def save(self, database, record):
        
        #implement something to prevent duplication
        
        
        
        print(record)
    
        # locate database
        db = self.couch[database]
    
        # save into couchdb
        db.save(record)        