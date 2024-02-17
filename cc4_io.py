import json
import os
import pandas as pd


def get_country_codes(src) -> dict:
    """
    Creates a pandas dataframe from the country code excel sheet.
    """
    dataframe = pd.read_excel(src)
    return dataframe.to_dict("records")


def get_restaurant_data(src) -> list:
    """
    Gets the data from the restaurant_data.json file and returns it as a list.
    """
    fh = open(src, "r", encoding="utf-8")
    json_str = fh.read()
    json_obj = json.loads(json_str)
    fh.close()
    return json_obj


def write_restaurant_csv(dir, filename, header, content) -> None:
    """
    Writes the relevant data into the final restaurant.csv file.
    """
    if not os.path.exists(dir):
        os.mkdir(dir)

    fh_csv = open(dir + filename, "w", encoding="utf-8")
    fh_csv.write(header + content)
    fh_csv.close()
