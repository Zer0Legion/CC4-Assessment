import json
import os
import pandas as pd

OUT = "out/"
IN = "in/"

def create_restaurants_csv(src1="restaurant_data.json", src2="Country-Code.xlsx", dst="restaurants.csv"):
    def get_country_codes() -> dict:
        dataframe = pd.read_excel(IN + src2)
        return dataframe.to_dict('records')

    def get_country_name(c_id: int, country_codes: dict) -> str:
        for item in country_codes:
            if item["Country Code"] == c_id:
                return item["Country"]
        return ValueError()

    def get_restaurant_data() -> list:
        fh = open(IN + src1, "r", encoding="utf-8")
        json_str = fh.read()
        json_obj = json.loads(json_str)
        fh.close()
        return json_obj

    CSV_HEADERS = "restaurant_id,restaurant_name,country,city,user_rating_votes,user_aggregate_rating,cuisines\n"
    COUNTRY_CODES = get_country_codes()

    for obj in get_restaurant_data():
        restaurants_list = obj["restaurants"]
        for restaurant in restaurants_list:
            r = restaurant["restaurant"]

            id = r["R"]["res_id"]
            name = r["name"]
            country = get_country_name(r["location"]["country_id"], COUNTRY_CODES)
            city = r["location"]["city"]
            user_rating_votes = r["user_rating"]["votes"]
            user_aggregate_rating = r["user_rating"]["aggregate_rating"]
            cuisines = r["cuisines"]

            CSV_HEADERS += "{},{},{},{},{},{},{}\n".format(
                id, name, country, city, user_rating_votes, user_aggregate_rating, cuisines)

    if not os.path.exists(OUT):
        os.mkdir(OUT)

    fh_csv = open(OUT + dst, "w", encoding="utf-8")
    fh_csv.write(CSV_HEADERS)
    fh_csv.close()

if __name__ == "__main__":
    create_restaurants_csv()