The orders in which this code runs assuming we are in the CMPT-353-Project folder

# Filter the amenities-vancouver file to extract some information we need 
# This outputs 
# 1. filtered-vancouver-training.json that can be used for training
# 2. filtered-vancouver-testing.json that can be used for testing
# 3. filtered-vancouver-all.json that can be used for the final search
1. run all the code in filtering.ipynb

# Learn about the cities of the data points
2. python3 code/learn_city.py filtered-vancouver.json

Note: 
helper script that we can maybe use for plotting data
- to_gpx.py reads a json file and outputs a gpx file 