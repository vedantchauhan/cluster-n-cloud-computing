# vedant & shashank
# comp90024

import json
from database import database
from database.parser import Parser
from crawler.config import aurin_db_name
import aurin
import sys

class AurinData():

    def __init__(self):
        pass

    def aurin(self):

        # melbourne values
        total_females_melb = 0
        total_males_melb = 0
        total_persons_melb = 0
        north_america_melb = 0
        africa_melb = 0
        europe_melb = 0
        asia_melb = 0
        australia_melb = 0
        new_zealand_melb = 0
        born_elsewhere_melb = 0
        median_age_melb = 0
        median_household_income_melb = 0
        gambling_activities_melb=0
        married_males_melb=0
        married_females_melb=0
        unmarried_males_melb=0
        unmarried_females_melb=0
        married_persons_melb = 0
        unmarried_persons_melb = 0

        # sydney values
        total_females_syd = 0
        total_males_syd = 0
        total_persons_syd = 0
        north_america_syd = 0
        africa_syd = 0
        europe_syd = 0
        asia_syd = 0
        australia_syd = 0
        new_zealand_syd = 0
        born_elsewhere_syd = 0
        median_age_syd = 0
        median_household_income_syd = 0
        gambling_activities_syd = 0
        married_males_syd = 0
        married_females_syd = 0
        unmarried_males_syd = 0
        unmarried_females_syd = 0
        married_persons_syd = 0
        unmarried_persons_syd = 0

        # brisbane values
        total_females_bris = 0
        total_males_bris = 0
        total_persons_bris = 0
        north_america_bris = 0
        africa_bris = 0
        europe_bris = 0
        asia_bris = 0
        australia_bris = 0
        new_zealand_bris = 0
        born_elsewhere_bris = 0
        median_age_bris = 0
        median_household_income_bris = 0
        gambling_activities_bris = 0
        married_males_bris = 0
        married_females_bris = 0
        unmarried_males_bris = 0
        unmarried_females_bris = 0
        married_persons_bris = 0
        unmarried_persons_bris = 0

        # hobart values
        total_females_hob = 0
        total_males_hob = 0
        total_persons_hob = 0
        north_america_hob = 0
        africa_hob = 0
        europe_hob = 0
        asia_hob = 0
        australia_hob = 0
        new_zealand_hob = 0
        born_elsewhere_hob = 0
        median_age_hob = 0
        median_household_income_hob = 0
        gambling_activities_hob = 0
        married_males_hob = 0
        married_females_hob = 0
        unmarried_males_hob = 0
        unmarried_females_hob = 0
        married_persons_hob = 0
        unmarried_persons_hob = 0

        # perth values
        total_females_per = 0
        total_males_per = 0
        total_persons_per = 0
        north_america_per = 0
        africa_per = 0
        europe_per = 0
        asia_per = 0
        australia_per = 0
        new_zealand_per = 0
        born_elsewhere_per = 0
        median_age_per = 0
        median_household_income_per = 0
        gambling_activities_per = 0
        married_males_per = 0
        married_females_per = 0
        unmarried_males_per = 0
        unmarried_females_per = 0
        married_persons_per = 0
        unmarried_persons_per = 0

        # canberra values
        total_females_can = 0
        total_males_can = 0
        total_persons_can = 0
        north_america_can = 0
        africa_can = 0
        europe_can = 0
        asia_can = 0
        australia_can = 0
        new_zealand_can = 0
        born_elsewhere_can = 0
        median_age_can = 0
        median_household_income_can = 0
        gambling_activities_can = 0
        married_males_can = 0
        married_females_can = 0
        unmarried_males_can = 0
        unmarried_females_can = 0
        married_persons_can = 0
        unmarried_persons_can = 0

        # darwin values
        total_females_dar = 0
        total_males_dar = 0
        total_persons_dar = 0
        north_america_dar = 0
        africa_dar = 0
        europe_dar = 0
        asia_dar = 0
        australia_dar = 0
        new_zealand_dar = 0
        born_elsewhere_dar = 0
        median_age_dar = 0
        median_household_income_dar = 0
        gambling_activities_dar = 0
        married_males_dar = 0
        married_females_dar = 0
        unmarried_males_dar = 0
        unmarried_females_dar = 0
        married_persons_dar = 0
        unmarried_persons_dar = 0

        # adelaide values
        total_females_ade = 0
        total_males_ade = 0
        total_persons_ade = 0
        north_america_ade = 0
        africa_ade = 0
        europe_ade = 0
        asia_ade = 0
        australia_ade = 0
        new_zealand_ade = 0
        born_elsewhere_ade = 0
        median_age_ade = 0
        median_household_income_ade = 0
        gambling_activities_ade = 0
        married_males_ade = 0
        married_females_ade = 0
        unmarried_males_ade = 0
        unmarried_females_ade = 0
        married_persons_ade=0
        unmarried_persons_ade=0

        try:

            filejson_marital_status=open("../scripts/aurin/citydata_maritalstatus.json", "r")
            data_marital_status=json.load(filejson_marital_status)

            city_list_marital_status=data_marital_status["features"]

            for city in city_list_marital_status:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        married_females_melb = city["properties"]["f_tot_married"]
                        unmarried_females_melb = city["properties"]["f_tot_never_married"]
                        married_males_melb = city["properties"]["m_tot_married"]
                        unmarried_males_melb = city["properties"]["m_tot_never_married"]
                        married_persons_melb=city["properties"]["p_tot_married"]
                        unmarried_persons_melb = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):
                        married_females_syd = city["properties"]["f_tot_married"]
                        unmarried_females_syd = city["properties"]["f_tot_never_married"]
                        married_males_syd = city["properties"]["m_tot_married"]
                        unmarried_males_syd = city["properties"]["m_tot_never_married"]
                        married_persons_syd = city["properties"]["p_tot_married"]
                        unmarried_persons_syd = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):
                        married_females_hob = city["properties"]["f_tot_married"]
                        unmarried_females_hob = city["properties"]["f_tot_never_married"]
                        married_males_hob = city["properties"]["m_tot_married"]
                        unmarried_males_hob = city["properties"]["m_tot_never_married"]
                        married_persons_hob = city["properties"]["p_tot_married"]
                        unmarried_persons_hob = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):
                        married_females_per = city["properties"]["f_tot_married"]
                        unmarried_females_per = city["properties"]["f_tot_never_married"]
                        married_males_per = city["properties"]["m_tot_married"]
                        unmarried_males_per = city["properties"]["m_tot_never_married"]
                        married_persons_per = city["properties"]["p_tot_married"]
                        unmarried_persons_per = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):
                        married_females_bris = city["properties"]["f_tot_married"]
                        unmarried_females_bris = city["properties"]["f_tot_never_married"]
                        married_males_bris = city["properties"]["m_tot_married"]
                        unmarried_males_bris = city["properties"]["m_tot_never_married"]
                        married_persons_bris = city["properties"]["p_tot_married"]
                        unmarried_persons_bris = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):
                        married_females_dar = city["properties"]["f_tot_married"]
                        unmarried_females_dar = city["properties"]["f_tot_never_married"]
                        married_males_dar = city["properties"]["m_tot_married"]
                        unmarried_males_dar = city["properties"]["m_tot_never_married"]
                        married_persons_dar = city["properties"]["p_tot_married"]
                        unmarried_persons_dar = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):
                        married_females_ade = city["properties"]["f_tot_married"]
                        unmarried_females_ade = city["properties"]["f_tot_never_married"]
                        married_males_ade = city["properties"]["m_tot_married"]
                        unmarried_males_ade = city["properties"]["m_tot_never_married"]
                        married_persons_ade = city["properties"]["p_tot_married"]
                        unmarried_persons_ade = city["properties"]["p_tot_never_married"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):
                        married_females_can = city["properties"]["f_tot_married"]
                        unmarried_females_can = city["properties"]["f_tot_never_married"]
                        married_males_can = city["properties"]["m_tot_married"]
                        unmarried_males_can = city["properties"]["m_tot_never_married"]
                        married_persons_can = city["properties"]["p_tot_married"]
                        unmarried_persons_can = city["properties"]["p_tot_never_married"]

            filejson_gambling = open("../scripts/aurin/citydata_gambling.json", "r")
            data_gambling = json.load(filejson_gambling)

            city_list_gambling = data_gambling["features"]

            for city in city_list_gambling:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        gambling_activities_melb = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):
                        gambling_activities_syd = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):
                        gambling_activities_hob = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):
                        gambling_activities_per = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):
                        gambling_activities_bris = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):
                        gambling_activities_dar = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):
                        gambling_activities_ade = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):
                        gambling_activities_can = city["properties"]["artsr_gambling_ac_p"]


            city_list_gambling = data_gambling["features"]
            for city in city_list_gambling:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        gambling_activities_melb = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):
                        gambling_activities_syd = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):
                        gambling_activities_hob = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):
                        gambling_activities_per = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):
                        gambling_activities_bris = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):
                        gambling_activities_dar = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):
                        gambling_activities_ade = city["properties"]["artsr_gambling_ac_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):
                        gambling_activities_can = city["properties"]["artsr_gambling_ac_p"]

            filejson = open("../scripts/aurin/citydata_incomeage.json","r")
            data_incomeage = json.load(filejson)

            city_list_age = data_incomeage["features"]
            for city in city_list_age:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        median_age_melb = city["properties"]["med_age_psns_tot"]
                        median_household_income_melb = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):
                        median_age_syd = city["properties"]["med_age_psns_tot"]
                        median_household_income_syd = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):
                        median_age_hob = city["properties"]["med_age_psns_tot"]
                        median_household_income_hob = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):
                        median_age_per = city["properties"]["med_age_psns_tot"]
                        median_household_income_per = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):
                        median_age_bris = city["properties"]["med_age_psns_tot"]
                        median_household_income_bris = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):
                        median_age_dar = city["properties"]["med_age_psns_tot"]
                        median_household_income_dar = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):
                        median_age_ade = city["properties"]["med_age_psns_tot"]
                        median_household_income_ade = city["properties"]["med_hhd_inc_wk_tot"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):
                        median_age_can = city["properties"]["med_age_psns_tot"]
                        median_household_income_can = city["properties"]["med_hhd_inc_wk_tot"]

            file = open("../scripts/aurin/citydata_birthcountries.json","r")
            data = json.load(file)

            city_list = data["features"]
            for city in city_list:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_melb += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_melb += africa
                        australia_melb = city["properties"]["australia_p"]
                        new_zealand_melb = city["properties"]["new_zealand_p"]
                        born_elsewhere_melb = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_melb += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"]["sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_melb += asia
                        total_females_melb = city["properties"]["tot_f"]
                        total_males_melb = city["properties"]["tot_m"]
                        total_persons_melb = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_syd += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_syd += africa
                        australia_syd = city["properties"]["australia_p"]
                        new_zealand_syd = city["properties"]["new_zealand_p"]
                        born_elsewhere_syd = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_syd += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_syd += asia
                        total_females_syd = city["properties"]["tot_f"]
                        total_males_syd = city["properties"]["tot_m"]
                        total_persons_syd = city["properties"]["tot_p"]
                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_hob += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_hob += africa
                        australia_hob = city["properties"]["australia_p"]
                        new_zealand_hob = city["properties"]["new_zealand_p"]
                        born_elsewhere_hob = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_hob += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_hob += asia
                        total_females_hob = city["properties"]["tot_f"]
                        total_males_hob = city["properties"]["tot_m"]
                        total_persons_hob = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_per += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_per += africa
                        australia_per = city["properties"]["australia_p"]
                        new_zealand_per = city["properties"]["new_zealand_p"]
                        born_elsewhere_per = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_per += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_per += asia
                        total_females_per = city["properties"]["tot_f"]
                        total_males_per = city["properties"]["tot_m"]
                        total_persons_per = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_bris += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_bris += africa
                        australia_bris = city["properties"]["australia_p"]
                        new_zealand_bris = city["properties"]["new_zealand_p"]
                        born_elsewhere_bris = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_bris += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_bris += asia
                        total_females_bris = city["properties"]["tot_f"]
                        total_males_bris = city["properties"]["tot_m"]
                        total_persons_bris = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_dar += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_dar += africa
                        australia_dar = city["properties"]["australia_p"]
                        new_zealand_dar = city["properties"]["new_zealand_p"]
                        born_elsewhere_dar = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_dar += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_dar += asia
                        total_females_dar = city["properties"]["tot_f"]
                        total_males_dar = city["properties"]["tot_m"]
                        total_persons_dar = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_ade += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_ade += africa
                        australia_ade = city["properties"]["australia_p"]
                        new_zealand_ade = city["properties"]["new_zealand_p"]
                        born_elsewhere_ade = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_ade += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_ade += asia
                        total_females_ade = city["properties"]["tot_f"]
                        total_males_ade = city["properties"]["tot_m"]
                        total_persons_ade = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_can += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + \
                                 city["properties"][
                                     "zimbabwe_p"]
                        africa_can += africa
                        australia_can = city["properties"]["australia_p"]
                        new_zealand_can = city["properties"]["new_zealand_p"]
                        born_elsewhere_can = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + \
                                 city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"][
                                     "poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_can += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"]["sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + \
                               city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_can += asia
                        total_females_can = city["properties"]["tot_f"]
                        total_males_can = city["properties"]["tot_m"]
                        total_persons_can = city["properties"]["tot_p"]



            try:
                db = database.DButils()
                parser = Parser()
                # parse aurin data
                record = parser.parse_aurin("aurin1", "Melbourne", total_persons_melb, total_males_melb,
                                            total_females_melb, asia_melb, europe_melb, australia_melb,
                                            new_zealand_melb, africa_melb, north_america_melb, born_elsewhere_melb,
                                            median_age_melb, median_household_income_melb,gambling_activities_melb,
                                            married_females_melb,unmarried_females_melb,married_males_melb,unmarried_males_melb,
                                            married_persons_melb,unmarried_persons_melb)
                record1 = parser.parse_aurin("aurin2", "Sydney", total_persons_syd, total_males_syd, total_females_syd,
                                             asia_syd, europe_syd, australia_syd, new_zealand_syd, africa_syd,
                                             north_america_syd, born_elsewhere_syd, median_age_syd,
                                             median_household_income_syd,gambling_activities_syd,
                                             married_females_syd,unmarried_females_syd,married_males_syd,unmarried_males_syd,
                                            married_persons_syd,unmarried_persons_syd)
                record2 = parser.parse_aurin("aurin3", "Brisbane", total_persons_bris, total_males_bris,
                                             total_females_bris,asia_bris, europe_bris, australia_bris, new_zealand_bris, africa_bris,
                                             north_america_bris, born_elsewhere_bris, median_age_bris,
                                             median_household_income_bris,gambling_activities_bris,
                                             married_females_bris, unmarried_females_bris, married_males_bris,
                                             unmarried_males_bris,married_persons_bris, unmarried_persons_bris)
                record3 = parser.parse_aurin("aurin4", "Darwin", total_persons_dar, total_males_dar, total_females_dar,
                                             asia_dar, europe_dar, australia_dar, new_zealand_dar, africa_dar,
                                             north_america_dar, born_elsewhere_dar, median_age_dar,
                                             median_household_income_dar,gambling_activities_dar,
                                             married_females_dar, unmarried_females_dar, married_males_dar, unmarried_males_dar,
                                             married_persons_dar, unmarried_persons_dar)
                record4 = parser.parse_aurin("aurin5", "Adelaide", total_persons_ade, total_males_ade,
                                             total_females_ade,asia_ade, europe_ade, australia_ade, new_zealand_ade, africa_ade,
                                             north_america_ade, born_elsewhere_ade, median_age_ade,
                                             median_household_income_ade,gambling_activities_ade,married_females_ade,
                                             unmarried_females_ade,married_males_ade,unmarried_males_ade,
                                            married_persons_ade,unmarried_persons_ade)
                record5 = parser.parse_aurin("aurin6", "Hobart", total_persons_hob, total_males_hob, total_females_hob,
                                             asia_hob, europe_hob, australia_hob, new_zealand_hob, africa_hob,
                                             north_america_hob, born_elsewhere_hob, median_age_hob,
                                             median_household_income_hob,gambling_activities_hob,married_females_hob,
                                             unmarried_females_hob,married_males_hob,unmarried_males_hob,
                                            married_persons_hob,unmarried_persons_hob)
                record6 = parser.parse_aurin("aurin7", "Canberra", total_persons_can, total_males_can,
                                             total_females_can,
                                             asia_can, europe_can, australia_can, new_zealand_can, africa_can,
                                             north_america_can, born_elsewhere_can, median_age_can,
                                             median_household_income_can,gambling_activities_can,married_females_can,
                                             unmarried_females_can,married_males_can,unmarried_males_can,
                                            married_persons_can,unmarried_persons_can)
                record7 = parser.parse_aurin("aurin8", "Perth", total_persons_per, total_males_per, total_females_per,
                                             asia_per, europe_per, australia_per, new_zealand_per, africa_per,
                                             north_america_per, born_elsewhere_per, median_age_per,
                                             median_household_income_per,gambling_activities_per,married_females_per,
                                             unmarried_females_per,married_males_per,unmarried_males_per,
                                            married_persons_per,unmarried_persons_per)

                # save into couchdb
                db.save(aurin_db_name, record)
                db.save(aurin_db_name, record1)
                db.save(aurin_db_name, record2)
                db.save(aurin_db_name, record3)
                db.save(aurin_db_name, record4)
                db.save(aurin_db_name, record5)
                db.save(aurin_db_name, record6)
                db.save(aurin_db_name, record7)

            except Exception as e:
                print(e)


        except Exception as e:
            print(e)
