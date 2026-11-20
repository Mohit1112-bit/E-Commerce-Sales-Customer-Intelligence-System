import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from data_loader import *
from data_validation import *
from utils.design import *
def show():
    print(f''' {'='*31} E-COMMERCE SALES CUSTOMER INTELLIGENCE SYSTEM {'='*31} 
    1. Load Files
    2. Validate files(Missing values , Duplicate value ,Invalid data type etc) ''')

def loading_report (name , data ):
    ok = data is not None
    print(f"[{'OK' if ok else 'ERROR'}] {name} dataset {'Loaded' if ok else 'Not Loaded'}")

customer = order = product = None

while True:
    show()
    choice = int(input('Enter the Choices : '))
    if choice == 1:
        customer = load_customers()
        order = load_orders()
        product = load_products() 

        print(f'''{'-'*31} DATA LOADING MODULE {'-'*31}''')
        
        loading_report('customers' , customer)
        loading_report('orders' , order)
        loading_report('products' , product)
        sep()
        rows_customers , rows_orders , rows_products = df_info()
        
        print(f'''    {'customers':<10} : {rows_customers}
    {'orders':<10} : {rows_orders}
    {'products':<10} : {rows_products}''')
    if choice == 2:
        print(f'''{'-'*31} DATA VALIDATION MODULE {'-'*31}''')
        customer_missing = missing_value(data_customers)
        order_missing = missing_value(data_orders)
        product_missing = missing_value(data_products)
        
        missing_data = {
            'customers' : customer_missing,
            'orders' : order_missing,
            'products' : product_missing
        }

        print(f'''

        Missing Values

        ''')
        for name , missing in missing_data.items():
            print(f'\n{name}')
            print(sep())
            print(missing)

        print('''
        
        Duplicated Values

        ''')
        
        duplicate_data = {
            'customers' : duplicate_value(data_customers, subset= 'customer_id'),
            'orders' : duplicate_value(data_orders, subset= 'order_id'),
            'products' : duplicate_value(data_products, subset= 'product_id')
        }

        for data , duplicated in duplicate_data.items():
            print(data)
            print(duplicated)
            print(sep())