import psycopg2
host = "pg-dev-dev-101.a.aivencloud.com"
port = "16506"
dbname = "defaultdb"
user = "avnadmin"
password = "AVNS_WKCKGD4JC5s0lel9zKD"

conn =  psycopg2.connect(("host={host} dbname={dbname} user={user} password={password} port={port}").format(host=host,dbname=dbname,user=user,password=password,port=port))
cur = conn.cursor()
# conn = psycopg2.connect(
#     "host=127.0.0.1 dbname=postgres user=postgres password=digitalskola")
# cur = conn.cursor()

cur.execute("""
            CREATE TABLE syaiful_latihan_user(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
            )
            """)
conn.commit()
print("Berhasil")