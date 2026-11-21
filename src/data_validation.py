import data_loader

data_customers = data_loader.load_customers()
data_orders = data_loader.load_orders()
data_products = data_loader.load_products()

def column_validation():
    column_customers = ['customer_id','customer_name','age','gender','city','state','registration_date']
    column_orders = ['order_id','customer_id','product_id','order_date','quantity','discount_percent',
    'payment_method','order_status']
    column_products = ['product_id','product_name','category','brand','selling_price','cost_price']
    data = [data_customers,data_orders,data_products]
    columns = [column_customers,column_orders,column_products]
    df = ['customers' , 'orders' , 'products']
    for columns , data , df in zip(columns, data ,df):
        actual = data.columns.tolist()
        missing_column = set(columns) - set(data)
        unexpected_column = set(data) -set(columns)
        if missing_column or unexpected_column:
            print(f'{df} file has validation failure !!')
            print(f'Missing columns : {missing_column}')
            print(f'Unexpected columns : {unexpected_column}')
        elif columns != actual :
            print(f'{df} : order is not correct')

        else :
            print(f'{df} : columns are valid')
    return f'Column Validation completed'

def df_info():
    rows_customers = data_customers.shape[0]
    rows_orders = data_orders.shape[0]
    rows_products = data_products.shape[0]
    return rows_customers , rows_orders , rows_products

def missing_value(data):
    missing_count = data.isnull().sum()
    return missing_count 

def duplicate_value (data , subset = None):
    dup_row = data[data.duplicated(subset = subset)]
    dup_count = data.duplicated(subset = subset).sum()
    return dup_count

def validate_relationship(data,column,other_data ):
    invalid = data[~data[column].isin(other_data[column])]
    if invalid.empty :
        return f'NO INVALID DATA'
    else :
        return f'INVALID ROWS : \n{invalid}'