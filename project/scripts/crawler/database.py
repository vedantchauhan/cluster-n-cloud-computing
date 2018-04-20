import couchdb


COUCHDB_ADDR = "http://127.0.0.1:5984"      # change file path during test


class DButils():
    
    couch = None
    
    def __init__(self):
        # connect to couchdb
        self.couch = couchdb.Server(COUCHDB_ADDR)
        
        
    def save(self, database, record):
        print(record)
    
        # locate database
        db = self.couch[database]
    
        # save into couchdb
        db.save(record)        