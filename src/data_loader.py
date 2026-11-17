import pandas as pd 
from pathlib import Path

def load_customers():
    csv_file = Path('data/raw/customers.csv')
    if csv_file.is_file():
        data = pd.read_csv(csv_file)
        if data.empty:
            return 'File is empty'
        else : 
            return data 
    else :
        raise FileExistsError(f"Missing file : {csv_file}")    

def load_orders():
    csv_file = Path('data/raw/orders.csv')
    if csv_file.is_file():
        data = pd.read_csv(csv_file)
        if data.empty:
            return 'File is empty'
        else : 
            return data 
    else :
        return 'No file exist '
        
def load_products():
    csv_file = Path('data/raw/products.csv')
    if csv_file.is_file():
        data = pd.read_csv(csv_file)
        if data.empty:
            return 'File is empty'
        else : 
            return data 
    else :
        return 'No file exist '