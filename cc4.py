import json

def create_restaurants_csv(src1="restaurant_data.json", src2="Country-Code.xlsx", dst="restaurants.csv"):
    
    fh = open(src1, "r", encoding="utf-8")
    json_str = fh.read()
    json_obj = json.loads(json_str)
    fh.close()

    csv = "restaurant_id,restaurant_name,country,city,user_rating_votes,user_aggregate_rating,cuisines\n"
    for obj in json_obj:
        restaurants_list = obj["restaurants"]
        for restaurant in restaurants_list:
            r = restaurant["restaurant"]

            id = r["R"]["res_id"]
            name = r["name"]
            country = r["location"]["country_id"]
            city = r["location"]["city"]
            user_rating_votes = r["user_rating"]["votes"]
            user_aggregate_rating = r["user_rating"]["aggregate_rating"]
            cuisines = r["cuisines"]

            csv += "{},{},{},{},{},{},{}\n".format(
                id, name, country, city, user_rating_votes, user_aggregate_rating, cuisines)

    fh_csv = open(dst, "w", encoding="utf-8")
    fh_csv.write(csv)
    fh_csv.close()

if __name__ == "__main__":
    create_restaurants_csv()