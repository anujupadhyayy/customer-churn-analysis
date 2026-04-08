import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("Customer-Churn-Records.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

engine = create_engine("mysql+pymysql://root@localhost/churn_db")
df.to_sql("customer_churn", engine, if_exists="replace", index=False)
print("Loaded rows:", len(df))