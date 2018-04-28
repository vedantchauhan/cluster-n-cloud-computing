class Keys:
    """
        CONSUMER_KEY
        CONSUMER_SEC
        ACCESS_TOKEN
        ACCESS_SEC
    """

    def __init__(self, ckey, csec, atoken, asec):
        self.ckey = ckey
        self.csec = csec
        self.atoken = atoken
        self.asec = asec



db_name = 'tweets'                         # name of the database
aurin_db_name = 'aurin'                    # name of aurin database
couchdb_uri = "http://127.0.0.1:5984"      # couchdb address
app_auth = {
    'jiyu': Keys(
        "se7dR9OJzvcJdG9nO6g9VVpKE",
        "0iJSVbUVN2OPOSPy3KJQdQP3Q0iGvyZfHAMQXKwce03tfO5PYk",
        "985778410898124800-kNVBSiLMIWRILWlGR71zk8HCl6IllEo",
        "ttLXW3R5rC3MMXMwbq7irCf9GcAhIOV9i3Pz1VhmS9IaP"
    )
    # add other users access info here n change in harvestMode.py as well
}

MELBOURNE_STR = [144.6550006954,-38.5089967291,145.3498310249,-37.5916213868]  #http://boundingbox.klokantech.com

MELBOURNE_SRC = [-37.8136276, 144.96305759999996, 5]
# geographical centre of search  # geographical centre of search   # search range in kilometres

