import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("D:/DigitalSkola/project3/source/users_w_postal_code.csv",sep=",")
# host = "pg-dev-dev-101.a.aivencloud.com"
# port = "16506"
# dbname = "defaultdb"
# user = "avnadmin"
# password = "AVNS_WKCKGD4JC5s0lel9zKD"
# engine = create_engine("postgresql://postgres:digitalskola@127.0.0.1:5432/postgres")
engine = create_engine("postgresql://avnadmin:AVNS_WKCKGD4JC5s0lel9zKD@pg-dev-dev-101.a.aivencloud.com:16506/defaultdb")
df.to_sql("syaiful_users_w_postal_code",engine)
print("Berhasil")