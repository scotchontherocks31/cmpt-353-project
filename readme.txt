The orders in which this code runs assuming we are in the CMPT-353-Project folder

# Filter the amenities-vancouver file to extract some information we need 
# This outputs filtered-vancouver.json that can be later used 
1. python3 code/filtering.py amenities-vancouver.json

# Learn about the cities of the data points
2. python3 code/learn_city.py filtered-vancouver.json