from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import couchdb
import json

DATABASE = 'aurin'
DATABASE_TWEETS = 'tweets'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'
url = 'http://admin:admin@172.17.0.3:5984'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# sports value
response_sports = {}
response_gamble = {}
response_tot_persons = {}
response_tweet_score = {}

# connecting to couchdb
def connect_db():
    server = couchdb.Server(url)
    return server


def tweets():
    try:
        # variables
        count_pos_melb = 0
        count_neg_melb = 0
        count_pos_syd = 0
        count_neg_syd = 0
        count_pos_dar = 0
        count_neg_dar = 0
        count_pos_per = 0
        count_neg_per = 0
        count_pos_ade = 0
        count_neg_ade = 0
        count_pos_bri = 0
        count_neg_bri = 0
        count_pos_hob = 0
        count_neg_hob = 0
        count_pos_can = 0
        count_neg_can = 0

        server = connect_db()
        db_tweets = server["tweets"]

        for item in db_tweets.view('group49/melb_pos'):
            count_pos_melb = item["value"]
        for item in db_tweets.view('group49/melb_neg'):
            count_neg_melb = item["value"]
        melb_score = count_pos_melb / count_neg_melb

        for item in db_tweets.view('group49/syd_pos'):
            count_pos_syd = item["value"]
        for item in db_tweets.view('group49/syd_neg'):
            count_neg_syd = item["value"]
        syd_score = count_pos_syd / count_neg_syd

        for item in db_tweets.view('group49/bri_pos'):
            count_pos_bri = item["value"]
        for item in db_tweets.view('group49/bri_neg'):
            count_neg_bri = item["value"]
        bri_score = count_pos_bri / count_neg_bri

        for item in db_tweets.view('group49/can_pos'):
            count_pos_can = item["value"]
        for item in db_tweets.view('group49/can_neg'):
            count_neg_can = item["value"]
        can_score = count_pos_can / count_neg_can

        for item in db_tweets.view('group49/ade_pos'):
            count_pos_ade = item["value"]
        for item in db_tweets.view('group49/ade_neg'):
            count_neg_ade = item["value"]
        ade_score = count_pos_ade / count_neg_ade

        for item in db_tweets.view('group49/hob_pos'):
            count_pos_hob = item["value"]
        for item in db_tweets.view('group49/hob_neg'):
            count_neg_hob = item["value"]
        hob_score = count_pos_hob / count_neg_hob

        for item in db_tweets.view('group49/per_pos'):
            count_pos_per = item["value"]
        for item in db_tweets.view('group49/per_neg'):
            count_neg_per = item["value"]
        per_score = count_pos_per / count_neg_per

        for item in db_tweets.view('group49/dar_pos'):
            count_pos_dar = item["value"]
        for item in db_tweets.view('group49/dar_neg'):
            count_neg_dar = item["value"]
        dar_score = count_pos_dar / count_neg_dar

        response_tweet_score.update({
            "Melbourne": melb_score,
            "Sydney": syd_score,
            "Darwin": dar_score,
            "Hobart": hob_score,
            "Adelaide": ade_score,
            "Brisbane": bri_score,
            "Perth": per_score,
            "Canberra": can_score
        })
        #return response_tweet_score
    except Exception as e:
        print(e)

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    db = connect_db()
    rows = db.view('_all_docs', include_docs=True)
    data = [row['doc'] for row in rows]
    # df = pd.DataFrame(data)
    response = {}
    for d in data:
        response.update({d['city']: d['median_income']})
    return render_template('show_entries.html', response=response)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/analysis_one')
def analysis_one():
    try:
        count_pos_melb = 0
        count_neg_melb = 0
        count_pos_syd = 0
        count_neg_syd = 0
        count_pos_dar = 0
        count_neg_dar = 0
        count_pos_per = 0
        count_neg_per = 0
        count_pos_ade = 0
        count_neg_ade = 0
        count_pos_bri = 0
        count_neg_bri = 0
        count_pos_hob = 0
        count_neg_hob = 0
        count_pos_can = 0
        count_neg_can = 0

        server = connect_db()
        db_tweets = server["tweets"]

        for item in db_tweets.view('group49/melb_pos'):
            count_pos_melb = item["value"]
        for item in db_tweets.view('group49/melb_neg'):
            count_neg_melb = item["value"]
        melb_score = count_pos_melb / count_neg_melb

        for item in db_tweets.view('group49/syd_pos'):
            count_pos_syd = item["value"]
        for item in db_tweets.view('group49/syd_neg'):
            count_neg_syd = item["value"]
        syd_score = count_pos_syd / count_neg_syd

        for item in db_tweets.view('group49/bri_pos'):
            count_pos_bri = item["value"]
        for item in db_tweets.view('group49/bri_neg'):
            count_neg_bri = item["value"]
        bri_score = count_pos_bri / count_neg_bri

        for item in db_tweets.view('group49/can_pos'):
            count_pos_can = item["value"]
        for item in db_tweets.view('group49/can_neg'):
            count_neg_can = item["value"]
        can_score = count_pos_can / count_neg_can

        for item in db_tweets.view('group49/ade_pos'):
            count_pos_ade = item["value"]
        for item in db_tweets.view('group49/ade_neg'):
            count_neg_ade = item["value"]
        ade_score = count_pos_ade / count_neg_ade

        for item in db_tweets.view('group49/hob_pos'):
            count_pos_hob = item["value"]
        for item in db_tweets.view('group49/hob_neg'):
            count_neg_hob = item["value"]
        hob_score = count_pos_hob / count_neg_hob

        for item in db_tweets.view('group49/per_pos'):
            count_pos_per = item["value"]
        for item in db_tweets.view('group49/per_neg'):
            count_neg_per = item["value"]
        per_score = count_pos_per / count_neg_per

        for item in db_tweets.view('group49/dar_pos'):
            count_pos_dar = item["value"]
        for item in db_tweets.view('group49/dar_neg'):
            count_neg_dar = item["value"]
        dar_score = count_pos_dar / count_neg_dar

        response_tweet_score.update({
            "Melbourne": melb_score,
            "Sydney": syd_score,
            "Darwin": dar_score,
            "Hobart": hob_score,
            "Adelaide": ade_score,
            "Brisbane": bri_score,
            "Perth": per_score,
            "Canberra": can_score
        })
        return render_template('analysis_one.html')
    except Exception as e:
        print(e)



@app.route('/analysis_two')
def analysis_two():
    try:
        # tweets based on sports
        melb_sports = 0
        syd_sports = 0
        per_sports = 0
        ade_sports = 0
        can_sports = 0
        hob_sports = 0
        bri_sports = 0
        dar_sports = 0
        server = connect_db()
        db_tweets = server["tweets"]

        for item in db_tweets.view('group49/melb_sports'):
            melb_sports = item["value"]

        for item in db_tweets.view('group49/syd_sports'):
            syd_sports = item["value"]

        for item in db_tweets.view('group49/bri_sports'):
            bri_sports = item["value"]

        for item in db_tweets.view('group49/can_sports'):
            can_sports = item["value"]

        for item in db_tweets.view('group49/ade_sports'):
            ade_sports = item["value"]

        for item in db_tweets.view('group49/hob_sports'):
            hob_sports = item["value"]

        for item in db_tweets.view('group49/per_sports'):
            per_sports = item["value"]

        for item in db_tweets.view('group49/dar_sports'):
            dar_sports = item["value"]

        response_sports.update({
            "Melbourne": melb_sports,
            "Sydney": syd_sports,
            "Darwin": dar_sports,
            "Hobart": hob_sports,
            "Adelaide": ade_sports,
            "Brisbane": bri_sports,
            "Perth": per_sports,
            "Canberra": can_sports
        })
        # aurin data for gambling
        db = server["aurin"]
        rows = db.view('_all_docs', include_docs=True)
        data = [row['doc'] for row in rows]
        for d in data:
            response_gamble.update({d['city']: d['gambling_activities']})
        for d1 in data:
            response_tot_persons.update({d1['city']: d1['total_persons']})
        return render_template('analysis_two.html', response_sports=response_sports,
                               response_tot_persons=response_tot_persons, response_gamble=response_gamble)
    except Exception as e:
        print(e)


@app.route('/analysis_three')
def analysis_three():
    return render_template('analysis_three.html')


if __name__ == '__main__':
    app.run(host='115.146.95.94', port=5015)
