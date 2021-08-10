import pandas as pd
import numpy as np
import pickle
import os
from difflib import get_close_matches

# Establishing global vars.
city_list = ['Vancouver', 'Burnaby', 'Richmond', 'Coquitlam', 'Surrey']

dir = os.getcwd()
model_path = dir + '/model.pkl'
training_path = dir + '/../filtered-vancouver-training-5-category.json'
testing_path = dir + '/../filtered-vancouver-testing.json'

def main():
    
    # Input & validity
    while True:
        city = input("Enter your current address: ")
        amenity = input("Enter the amenity you're looking for: ")

        if city in city_list:
            break
        else:
            print('Invalid "city" input. Must be in "Vancouver", "Burnaby", "Surrey", "Richmond", "Coquitlam" or "Surrey".\n')
            continue

    # Loading model and JSON files
    model = pickle.load(open(model_path, "rb"))
    training = pd.read_json(training_path, lines= True)
    testing = pd.read_json(testing_path, lines= True)
    name_check = training['name'].unique()

    # Filtration & Combination
    filter_testing = testing[["lat", "lon"]].copy()
    predict = model.predict(filter_testing)
    testing["city"] = predict
    testing = testing[testing["city"] == city].reset_index(drop=True)
    
    training = training[training["city"] == city].reset_index(drop=True)
    dataset = training.append(testing)
    print(dataset.head(10))

    # TODO: Cross-check amenity, implement the two options for the solutions

    return

if __name__ == '__main__':
    main()
