import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from data_loader import *
from data_validation import *
from utils.design import *
def show():
    print(f''' {'='*31} E-COMMERCE SALES CUSTOMER INTELLIGENCE SYSTEM {'='*31} 
    1. Load Files
    2. Validate files(Missing values , Duplicate value etc) ''')

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
        
        data_validate = {
            'CUSTOMERS' : [customer_missing , duplicate_value(data_customers, subset= 'customer_id')],
            'ORDERS' : [order_missing , duplicate_value(data_orders, subset= 'order_id')],
            'PRODUCTS' : [product_missing,duplicate_value(data_products, subset= 'product_id')]
        }

        for name , missing in data_validate.items():
            print(f'\n{name}')
            print(f'Missing : {missing[0].sum()}')
            print(f'Duplicated : {missing[1].sum()}')

        print('''

        DATA TYPES 
    
        ''')
        datatypes = {
        'customers' : data_customers.dtypes, 
        'orders' : data_orders.dtypes ,
        'products' : data_products.dtypes
        }
        for data , data_types in datatypes.items():
            print(sep())
            print(data , data_types ,sep='\n')
        
        print('''
        
        RELATIONSHIP VALIDATION

        ''')
        print(sep())
        print(f'customer_id' , validate_relationship(data_customers, 'customer_id', data_orders) , sep=' : ')
        
        print(f'product_id' , validate_relationship(data_products, 'product_id', data_orders) , sep=' : ')
        validate_relationship(data_products, 'product_id', data_orders)

    if choice == 3:
        pass 