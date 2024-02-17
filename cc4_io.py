import json
import os
import pandas as pd

def get_country_codes(src) -> dict:
    dataframe = pd.read_excel(src)
    return dataframe.to_dict('records')

def get_restaurant_data(src) -> list:
    fh = open(src, "r", encoding="utf-8")
    json_str = fh.read()
    json_obj = json.loads(json_str)
    fh.close()
    return json_obj

def write_restaurant_csv(dir, filename, header, content):
    if not os.path.exists(dir):
        os.mkdir(dir)

    fh_csv = open(dir + filename, "w", encoding="utf-8")
    fh_csv.write(header + content)
    fh_csv.close()