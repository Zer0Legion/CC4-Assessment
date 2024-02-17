import restaurants

OUT = "out/"
IN = "in/"
CSV_HEADERS = "restaurant_id,restaurant_name,country,city,user_rating_votes,user_aggregate_rating,cuisines\n"

if __name__ == "__main__":
    restaurants.create_csv(CSV_HEADERS, IN, OUT, "restaurant_data.json", "Country-Code.xlsx", "restaurants.csv")