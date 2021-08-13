# CMPT 353 Project

Group Project by **Shahriar kabir Nooh (snooh), Ting wei Chiu (twc10) & Albert Lam (ala161)**. All work is up to date, and meets code requirements for the group project.

## **Requirements**

Must have the following libraries installed in order to run scripts/ notebooks:
 - Pandas
 - Jupyter Notebooks
 - tqdm
 - sklearn
 - imblearn
 - matplotlib

```bash
pip install pandas
pip install jupyter
pip install tqdm
pip install sklearn
pip install imblearn
pip install matplotlib
```

## **Usage**

To access and run the code written for the project, please access the `code` folder, where all the Python scripts and Jupyter
notebooks are stored.

The notebooks can be opened by running the following in terminal:
```bash
jupyter notebook
```

## **Code Running Process**

The order in which the code runs, assuming the directory is in `cmpt-353-project/code`

### **Filtration**
Run `filtering.ipynb` to filter "amenities-vancouver.json" to extract information required. This outputs: 
 - `filtered-vancouver-training.json` , `filtered-vancouver-training-5-category.json` , `filtered-vancouver-training-amenity-removed.json` that can be used for training
 - `filtered-vancouver-testing.json` that can be used for testing
 - `filtered-vancouver-all.json` that can be used for the final search

Note: Used as an early experiment, we ran the json file agaisnt simple ML model in `learn_city.py` with:
```bash
python3 learn_city.py filtered-vancouver.json
```

### **Model building, fine tuning and export**
Run `model.ipynb`

### **User Interface**
To use the application that addresses our problem specified in the report, simply run:
```bash
python3 user_interface.py
```

### **Sample Input/Output**
$ python3 user-interface.py  
***	WELCOME TO PLACEHUNTER!	***

Enter the city name you're located in: vancouver  
Enter the name of the place you're looking for: mcdonalds  
Found place with closest approximation to given name: McDonald's.  

Generating map to show all McDonald's locations...
100%|████████████████████████████████████████████████████████████████| 11/11 [00:08<00:00,  1.30it/s]
MAP GENERATION - COMPLETE.

Showing top 5 McDonald's in Vancouver:

```
            lon        lat    amenity        name       city postcode street  confidence
689 -123.030512  49.280836  fast_food  McDonald's  Vancouver     None   None    0.340000
604 -123.101513  49.245151  fast_food  McDonald's  Vancouver     None   None    0.206667
539 -122.292177  49.036602  fast_food  McDonald's  Vancouver     None   None    0.140000
367 -123.065729  49.233088  fast_food  McDonald's  Vancouver     None   None    0.126667
567 -123.036516  49.306677  fast_food  McDonald's  Vancouver     None   None    0.120000
```

***	THANK YOU!	***



## **License**
[**MIT**](https://choosealicense.com/licenses/mit/)
