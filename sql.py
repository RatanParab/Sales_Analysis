from sqlalchemy import create_engine
import pandas as pd

# Read the cleaned CSV file
df = pd.read_csv("sales_cleaned.csv")

# Connect to MySQL
engine = create_engine(
    'mysql+pymysql://root:Ratan%40123@localhost:3306/salesdb'
)

# Load data into MySQL
df.to_sql(
    name='sales_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data loaded successfully into MySQL!")