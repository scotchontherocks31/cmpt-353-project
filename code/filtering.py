import sys
import pandas as pd
from pandas.io.json import json_normalize

def main():
    f1 = sys.argv[1]
    d1 = pd.read_json(f1, lines=True)

    # we are probably not interested in things that do not have a name (toilets, post boxes, ...)
    remove_no_name = d1[d1["name"].notna()]

    # group by the amenity names => gives a bunch of "resturants"...
    # groups = remove_no_name["amenity"].value_counts(ascending=True)

    # group by the name => gives a bunch of chain "McDonalds"
    # groups = remove_no_name["name"].value_counts(ascending=True)

    df = remove_no_name
    # adding a "City" column to the df by extracting the information from the tags
    df["city"] = json_normalize(remove_no_name["tags"])["addr:city"]

    df.to_json("filtered-vancouver.json", orient="records", lines=True)


if __name__ == '__main__':
    main()