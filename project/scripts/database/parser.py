import json


class Parser():

    def status_parse(self, status, sentiment_score):
        # filt out tweets outside aus
        if status.place.country_code != 'AU':
            return None

        result = {
            "_id": status.id_str,
            "id_str": status.id_str,
            "coordinates": status.coordinates,
            "place": {
                "id": status.place.id,
                "url": status.place.url,
                "place_type": status.place.place_type,
                "name": status.place.name,
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
            "sentiment": sentiment_score
        }
        return result

    def parse_aurin(self, id, city, tot_p, tot_m, tot_f, asians, europeans, australians, newzealanders, africans,
                    northamericans, bornelsewhere):
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
            "bornelsewhere": bornelsewhere
        }
        return result
