import restaurants

OUT = "out/"
IN = "in/"
CSV_INFO_HEADER = "restaurant_id,restaurant_name,country,city,user_rating_votes,user_aggregate_rating,cuisines\n"
CSV_EVENTS_HEADER = "event_id,restaurant_id,restaurant_name,photo_url,event_title,event_start_date,event_end_date\n"


if __name__ == "__main__":
    restaurants.create_restaurants_csv(CSV_INFO_HEADER, IN, OUT, "restaurant_data.json", "Country-Code.xlsx", "restaurants.csv")
    restaurants.create_restaurant_events_csv(CSV_EVENTS_HEADER, "2019-04-[0-3][0-9]", IN, OUT, "restaurant_data.json", "restaurant_events.csv")