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


db_name = 'tweets'
aurin_db_name = 'aurin'
# name of the database
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
SYD_STR = [150.9786666445,-34.0173030936,151.3082564883,-33.7048428499]
BRIS_STR = [152.6685227,-27.7674409,153.3178702,-26.9968449]
HOB_STR = [147.258116931,-42.9114151424,147.406089038,-42.8136762823]
PER_STR = []
CAN_STR = []
DAR_STR = []
ADE_STR = []


# geographical centre of search  # geographical centre of search   # search range in kilometres

