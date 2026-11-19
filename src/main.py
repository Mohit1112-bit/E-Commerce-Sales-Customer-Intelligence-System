from data_loader import *
from data_validation import *
def show():
    print(f''' {'='*31} E-COMMERCE SALES CUSTOMER INTELLIGENCE SYSTEM {'='*31} 
    1. Load Files ''')

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

        rows_customers , rows_orders , rows_products = df_info()

        print('*'*100)
        
        print(f'''    {'customers':<10} : {rows_customers}
    {'orders':<10} : {rows_orders}
    {'products':<10} : {rows_products}''')