import restaurants

IN = "in/"
OUT = "out/"

CSV_INFO_HEADER = "restaurant_id,restaurant_name,country,city,user_rating_votes,user_aggregate_rating,cuisines\n"
CSV_EVENTS_HEADER = "event_id,restaurant_id,restaurant_name,photo_url,event_title,event_start_date,event_end_date\n"
CSV_THRESHOLDS_HEADER = "rating_text,aggregate\n"

SRC_RESTAURANT_DATA = "restaurant_data.json"
SRC_COUNTRY_CODE = "Country-Code.xlsx"

OUT_RESTAURANTS = "restaurants.csv"
OUT_RESTAURANT_EVENTS = "restaurant_events.csv"
OUT_RESTAURANT_RATING = "restaurant_rating_threshold.csv"

REGEX_DATE = "2019-04-[0-3][0-9]"

if __name__ == "__main__":
    restaurants.create_restaurants_csv(CSV_INFO_HEADER, IN, OUT, SRC_RESTAURANT_DATA, SRC_COUNTRY_CODE, OUT_RESTAURANTS)
    restaurants.create_restaurant_events_csv(CSV_EVENTS_HEADER, REGEX_DATE, IN, OUT, SRC_RESTAURANT_DATA, OUT_RESTAURANT_EVENTS)
    restaurants.determine_ratings_threshold(CSV_THRESHOLDS_HEADER, IN, OUT, SRC_RESTAURANT_DATA, OUT_RESTAURANT_RATING)