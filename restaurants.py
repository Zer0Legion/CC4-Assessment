import re
import cc4_io

def create_restaurants_csv(
        header: str,
        dir_in="in/",
        dir_out="out/",
        src_restaurant_data="restaurant_data.json",
        src_country_code="Country-Code.xlsx",
        dst="restaurants.csv",
        ) -> None:

    """
    Extracts the following fields and stores the data as restaurants.csv: 
    - Restaurant Id
    - Restaurant Name
    - Country
    - City
    - User Rating Votes
    - User Aggregate Rating
    - Cuisines
    """

    def get_country_name(c_id: int, country_codes: dict) -> str:
        """
        Looks up the mappings for the country ids and their names.
        """
        for item in country_codes:
            if item["Country Code"] == c_id:
                return item["Country"]
        return ValueError()

    country_codes = cc4_io.get_country_codes(dir_in + src_country_code)
    restaurant_data = cc4_io.get_restaurant_data(dir_in + src_restaurant_data)
    content = ""

    for obj in restaurant_data:
        restaurants_list = obj["restaurants"]
        for restaurant in restaurants_list:
            r = restaurant["restaurant"]

            id = r["R"]["res_id"]
            name = r["name"]
            country = get_country_name(r["location"]["country_id"], country_codes)
            city = r["location"]["city"]
            user_rating_votes = r["user_rating"]["votes"]
            user_aggregate_rating = r["user_rating"]["aggregate_rating"]
            cuisines = r["cuisines"]

            content += "{},{},{},{},{},{},{}\n".format(
                id, name, country, city, user_rating_votes, user_aggregate_rating, cuisines)

    cc4_io.write_restaurant_csv(dir_out, dst, header, content)

def create_restaurant_events_csv(
        header: str,
        date="2019-04-[0-3][0-9]",
        dir_in="in/",
        dir_out="out/",
        src_restaurant_data="restaurant_data.json",
        dst="restaurant_events.csv"
):
    """
    Extracts the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv:
    - Event Id
    - Restaurant Id
    - Restaurant Name
    - Photo URL
    - Event Title
    - Event Start Date
    - Event End Date

    Note: Populates empty values with NA.
    """

    restaurant_data = cc4_io.get_restaurant_data(dir_in + src_restaurant_data)
    content = ""
    for obj in restaurant_data:
        restaurants_list = obj["restaurants"]
        for r in restaurants_list:
            restaurant = r["restaurant"]
            if not restaurant.get("zomato_events") == None:
                events = restaurant["zomato_events"]
                for event in events:
                    e = event["event"]
                    if re.match("date", e["start_date"]) or re.match(date, e["end_date"]):
                        # Capture info about restaurant
                        event_id = e["event_id"]
                        restaurant_id = restaurant["id"]
                        restaurant_name = restaurant["name"]
                        photo_url = e["photos"][0]["photo"]["url"] if len(e["photos"]) > 0 else "NA"
                        event_title = e["title"]
                        event_start_date = e["start_date"]
                        event_end_date = e["end_date"]

                        content += "{},{},{},{},{},{},{}\n".format(
                            event_id, restaurant_id, restaurant_name, photo_url, event_title, event_start_date, event_end_date)
                        
    cc4_io.write_restaurant_csv(dir_out, dst, header, content)

def determine_ratings_threshold(
        header: str,
        dir_in="in/",
        dir_out="out/",
        src_restaurant_data="restaurant_data.json",
        dst="restaurant_rating_threshold.csv"
):
    """
    From the dataset (restaurant_data.json), determine the threshold for the different rating text based on aggregate rating.
    Return aggregates for the following ratings only:
    - Excellent
    - Very Good
    - Good
    - Average
    - Poor

    As the lowest rating in the dataset is 2.2, but it is likely
    that a lower score constitutes as "Poor", I decided to
    set the threshold for "Poor" to 0.

    The output method was not specified. I chose to print the
    output to stdout as well as writing to csv similar to
    the previous subtasks.
    """
    restaurant_data = cc4_io.get_restaurant_data(dir_in + src_restaurant_data)

    thresholds = {
        "excellent" : (None, None),
        "very_good" : (None, None),
        "good" : (None, None),
        "average" : (None, None),
        "poor" : (0.0, None)
    }

    def adjust_min_max(score, key) -> None:
        low, high = thresholds[key]
        new_threshold: tuple = (None, None)
        if low == None or low > score:
            new_threshold = (score, high)
            low = score
        else:
            new_threshold = (low, high)
        
        if high == None or high < score:
            new_threshold = (low, score)
        else:
            new_threshold = (low, high)
        
        thresholds.update([(key, new_threshold)])

    def adjust_threshold(score: float, text: str) -> tuple:
        if text == "Excellent":
            adjust_min_max(score, "excellent")
        elif text == "Very Good":
            adjust_min_max(score, "very_good")
        elif text == "Good":
            adjust_min_max(score, "good")
        elif text == "Average":
            adjust_min_max(score, "average")

    for obj in restaurant_data:
        restaurants_list = obj["restaurants"]
        for restaurant in restaurants_list:
            r = restaurant["restaurant"]

            score = float(r["user_rating"]["aggregate_rating"])
            text = r["user_rating"]["rating_text"]
            adjust_threshold(score, text)
            
    res = ""
    for o in thresholds:
        res += o + "," + str(thresholds[o][0]) + "\n"

    print("Thresholds are:\n" + res)
    cc4_io.write_restaurant_csv(dir_out, dst, header, res)
