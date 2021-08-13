import pandas as pd
import numpy as np
import pickle
import os
from difflib import get_close_matches
import matplotlib.pyplot as plt
import math
import requests
from PIL import Image
from tqdm import tqdm

# Establishing global vars.
city_list = ["Vancouver", "Burnaby", "Surrey", "Coquitlam", "Richmond"] # ignoring "Abbotsford" cause model data said so
zoom = 12

dir = os.getcwd()
model_path = dir + '/model.pkl'
training_path = dir + '/../filtered-vancouver-training-5-category.json'
testing_path = dir + '/../filtered-vancouver-testing.json'
sample_output_path = dir + '/../sample_output/'


def city_to_num(index):
    """
        Takes in city name to spit out the index number needed to get desired predict_proba() results
    """
    return {"Vancouver": 0, "Burnaby": 1, "Surrey": 2, "Coquitlam": 3, "Richmond": 4}[index]

# the following function is adapted from: https://stackoverflow.com/a/28530369
def degree_to_number(lat, lon, zoom):
    """
        Takes in lat-lon co-ordinates and transforms them into OSM x-y co-ordinates
    """
    r_lat = math.radians(lat)
    n = 2 ** zoom
    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.log(math.tan(r_lat) +
                                 (1 / math.cos(r_lat))) / math.pi) / 2.0 * n)
                                
    return x_tile, y_tile

# the following function is adapted from: https://stackoverflow.com/a/28530369
# modification of the function above not using int for more accurate lon and lat results 
def degree_to_number_float(lat, lon, zoom):
    """
        Takes in lat-lon co-ordinates and transforms them into OSM x-y co-ordinates
    """
    r_lat = math.radians(lat)
    n = 2 ** zoom
    x_tile = ((lon + 180.0) / 360.0 * n)
    y_tile = ((1.0 - math.log(math.tan(r_lat) +
                                 (1 / math.cos(r_lat))) / math.pi) / 2.0 * n)
                                
    return x_tile, y_tile

# the following function is adapted from: https://stackoverflow.com/a/28530369
def map_image(lat, lon, max_lat, max_lon, zoom, amenity):
    """
        Creates an image cluster out of the given lat-lon co-ordinates and a specified "zoom" value
        to determine the zoom on the images being taken
    """
    osm_url = r"http://a.tile.openstreetmap.org/{0}/{1}/{2}.png"
    x_min, y_max = degree_to_number(lat, lon, zoom)
    x_max, y_min = degree_to_number(max_lat, max_lon, zoom)

    cluster = Image.new('RGB', ((x_max-x_min+1)*256-1, (y_max-y_min+1)*256-1))
    print(f'\tGenerating map to show all {amenity} locations...')
    for x_tile in tqdm(range(x_min, x_max+1)):
        for y_tile in range(y_min, y_max+1):
            try:
                img_url = osm_url.format(zoom, x_tile, y_tile)
                tile = Image.open(requests.get(img_url, stream=True).raw)
                cluster.paste(tile, box=(
                    (x_tile - x_min)*256,  (y_tile - y_min)*255))
            except:
                print("Image download failure, instantiating tile as None")
    
    print(f'\tMAP GENERATION - COMPLETE.\n')
    return cluster

def main():
    
    print('\t***\tWELCOME TO PLACEHUNTER!\t***\n')
    # Input & validity
    while True:
        city = input("Enter the city name you're located in: ")
        amenity = input("Enter the name of the place you're looking for: ")
        city_check = get_close_matches(city, city_list, n= 1)

        if not city_check:
            print('Invalid "city" input. Must be in "Vancouver", "Burnaby", "Richmond", "Coquitlam" or "Surrey".\n')
            continue
        else:
            city = city_check[0]
            break
            

    # Loading model and JSON files
    model = pickle.load(open(model_path, "rb"))
    training = pd.read_json(training_path, lines= True)
    testing = pd.read_json(testing_path, lines= True)

    # Filtration & Combination
    filter_testing = testing[["lat", "lon"]].copy()
    predict = model.predict(filter_testing)
    predict_proba = model.predict_proba(filter_testing)[:, city_to_num(city)]
    testing["city"] = predict
    testing["confidence"] = predict_proba
    testing = testing[testing["city"] == city].reset_index(drop=True)
    
    training = training[training["city"] == city].reset_index(drop=True)
    training["confidence"] = 0  # since we only want to focus on the model prediction results
    dataset = training.append(testing)

    # cross checking using get_close_matches(), cause we're all human
    name_list = dataset['name'].unique()
    name_list = [x for x in name_list if x is not None] # apparently this list had none-type objects... who knew
    amenity_check = get_close_matches(amenity, name_list, n=1)
    if not amenity_check:
        print('Could not find name of place in the local database, retry')
        print('\t***\tTHANK YOU!\t***\n')
        return
        
    amenity = amenity_check[0]
    print(f'Found place with closest approximation to given name: {amenity}.\n')
    dataset = dataset[dataset['name'] == amenity]

    # Setting up lat-lon vars to create image from OSM
    min_lat = dataset['lat'].min()
    max_lat = dataset['lat'].max()
    min_lon = dataset['lon'].min()
    max_lon = dataset['lon'].max()
    img_cluster = map_image(min_lat, min_lon, max_lat, max_lon, zoom, amenity)

    # Converting lat-long values in Dataframe to adjust for new scale in the OSM Image
    x_min, y_max = degree_to_number(min_lat, min_lon, zoom)
    x_max, y_min = degree_to_number(max_lat, max_lon, zoom)
    x_tile = []
    y_tile = []
    for index, row in dataset.iterrows():
        x, y = degree_to_number_float(row['lat'], row['lon'], zoom)
        x = (x - x_min) * 256 
        y = (y - y_min) * 255
        x_tile.append(x)
        y_tile.append(y)
    
    fig = plt.figure(figsize=(10, 8))
    plt.imshow(np.asarray(img_cluster))
    plt.scatter(x_tile, y_tile, zorder=1, alpha=0.8, c='b', s=10)
    plt.axis('off')
    plt.title(f'Map of all {amenity} in Lower Mainland around {city}')
    plt.savefig(sample_output_path + 'sample_out.png', bbox_inches='tight')
    plt.show()

    dataset = dataset.sort_values(by=['confidence'], ascending=False)
    print(f'Showing top 5 {amenity} in {city}:\n')
    print(dataset.head(5))
    print('\n')
    
    print('\t***\tTHANK YOU!\t***\n')
    return

if __name__ == '__main__':
    main()
