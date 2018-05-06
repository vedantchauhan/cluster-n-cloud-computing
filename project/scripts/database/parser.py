import json
import re


class Parser():

    def status_parse(self, status, sentiment_score,topic):
        # filt out tweets outside aus
        try:
            if status.place.country_code != 'AU':
                return None
        except AttributeError:
            return None

        hashtag = [part[1:] for part in status.text.split() if part.startswith('#')]

        result = {
            "_id": status.id_str,
            "id_str": status.id_str,
            "coordinates": status.coordinates,
            "place": {
                "place_type": status.place.place_type,
                "name": status.place.name,
                "bounding_box":{"coordinates":status.place.bounding_box.coordinates,
                                "type":status.place.bounding_box.type
                },
                "full_name": status.place.full_name,
                "country_code": status.place.country_code,
                "country": status.place.country
            },
            "user": {
                "id": status.user.id,
                "id_str": status.user.id_str,
                "name": status.user.name,
                "description": status.user.description
            },
            "lang": status.lang,
            "text": status.text,
            "sentiment": sentiment_score,
            "topic":topic,
            "hashtag":hashtag
        }
        return result

    def parse_aurin(self, id, city, tot_p, tot_m, tot_f, asians, europeans, australians, newzealanders, africans,
                    northamericans, bornelsewhere, median_age, median_income,gambling_activities):
        result = {
            "_id": id,
            "city": city,
            "total_persons": tot_p,
            "total_males": tot_m,
            "total_females": tot_f,
            "asians": asians,
            "europeans": europeans,
            "australians": australians,
            "newzealanders": newzealanders,
            "africans": africans,
            "northamericans": northamericans,
            "bornelsewhere": bornelsewhere,
            "median_age": median_age,
            "median_income": median_income,
            "gambling_activities":gambling_activities
        }
        return result
