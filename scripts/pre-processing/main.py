# main.py

from pyspark.sql import SparkSession
from clean_column_names import clean_column_names
from rename_column_names import rename_column_names
from drop_columns import drop_columns
from change_column_schema import change_column_schema
from handle_duplicates import handle_duplicates
from handle_missing_values import handle_missing_values

# Step 1: Create Spark session
spark = SparkSession.builder.appName("DataPreprocessing").getOrCreate()

# Step 2: Load data into DataFrame
df = spark.read.csv("/mnt/data/your_data_file.csv", header=True, inferSchema=True)

# Step 3: Clean column names
df = clean_column_names(df)

# Step 4: Drop unnecessary columns
df= drop_columns(df, ['customer_email', 'customer_password', 'customer_fname','customer_lname','product_description', 'product_image','order_zipcode','order_item_profit_ratio','benefit_per_order', 'sales','sales_per_customer', 'delivery_status','order_item_id','latitude', 'longitude','order_country',
    'order_item_profit_ratio', 'order_zipcode',  'late_delivery_risk','customer_street', 'customer_zipcode','product_card_id', 'product_category_id','department_id','department_name','category_id','order_item_cardprod_id','order_profit_per_order','shipping_date','market', 'order_city','order_state','product_status'])

# Step 5: Rename columns
rename_map = {"order_date_(dateorders)": "order_date","shipping_date_(dateorders)":"shipping_date", "days_for_shipping_(real)": "real_shipment_days",'days_for_shipment_(scheduled)':"scheduled_shipment_days",'type': 'payment_mode'}
df = rename_columns(df, rename_map)

# Step 6: Change schema of specific columns
df = change_column_schema(df, {'order_date': TimestampType(), 'shipping_date': TimestampType()})

# Step 7: Handle duplicate rows
df = handle_duplicates(df)

# Step 8: Handle missing values
df = handle_missing_values(df)

# Step 9: Show the final processed DataFrame
df.show()
