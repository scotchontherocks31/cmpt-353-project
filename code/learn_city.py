import sys
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline

def city_to_num(value):
    d = {
        "Vancouver": 1,
        "Burnaby": 2,
        "Surrey": 3,
        "Richmond": 4,
        "Langley": 5,
        "Maple Ridge": 6,
        "North Vancouver": 7,
        "Coquitlam": 8,
        "Delta": 9,
        "Port Coquitlam": 10,
        "District of North Vancouver": 11,
        "New Westminster": 12,
        "West Vancouver": 13,
        "Port Moody": 14,
        "White Rock": 15,
        "Township of Langley": 16,
        "North Vancouver City": 17,
        "Abbotsford": 18,
        "Aldergrove": 19,
        "Mission": 20,
        "City of Langley/Township of Langley Border": 21,
        "Vancovuer": 22,
        "Bowen Island": 23,
        "Fort Langley": 24,
        "Langley Township": 25,
        "Pitt Meadows": 26,
        "Hatzic": 27,
        "vancouver": 28,
        "Deroche": 29,
        "Chilliwack": 30,
    }
    return d[value]

def main():
    f1 = sys.argv[1]
    d1 = pd.read_json(f1, lines=True)

    training_data = d1[d1["city"].notna()]
    x_train = training_data[["lat", "lon"]]
    y_train = training_data["city"]

    testing_data = d1[d1["city"].notna() == False]
    x_test = testing_data[["lat", "lon"]]

    model = make_pipeline(
        KNeighborsClassifier(n_neighbors=20)
    )

    print(y_train.value_counts())
    model.fit(x_train, y_train)
    print("Score train : {}".format(model.score(x_train, y_train)))
    testing_data["city"] = model.predict(x_test)

    # combine the test and train data
    df = pd.concat([training_data, testing_data])

    print(df)
    df["colour"] = df["city"].apply(city_to_num)
    plt.scatter(df["lat"], df["lon"], c=df["colour"])
    plt.show()


if __name__ == '__main__':
    main()