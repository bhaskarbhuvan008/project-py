import pandas as pd
from sqlalchemy import text
from config import get_engine


engine = get_engine()

query = text("select *  from vessels where Status = :status")

df = pd.read_sql(query,engine,params={"status": "In Service"})

print(df)