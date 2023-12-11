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
            CREATE TABLE IF NOT EXISTS syaiful_users_using_copy(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
            )
            """)

with open("D:/DigitalSkola/project3/source/users_w_postal_code.csv","r") as f:
    next(f)
    cur.copy_from(f,"syaiful_users_using_copy",sep=",", columns=("email","name","phone","postal_code"))
conn.commit()
print("Berhasil")
