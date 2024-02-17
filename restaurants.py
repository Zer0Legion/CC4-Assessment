import cc4_io

def create_csv(
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

