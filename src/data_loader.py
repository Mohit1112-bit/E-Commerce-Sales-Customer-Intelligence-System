import pandas as pd 

def load_customers():
    return pd.read_csv('data/raw/customers.csv') 

def load_orders():
    return pd.read_csv('data/raw/orders.csv') 

def load_products():
    return pd.read_csv('data/raw/products.csv') 
