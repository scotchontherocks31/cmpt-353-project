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

## **License**
[**MIT**](https://choosealicense.com/licenses/mit/)
