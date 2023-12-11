import psycopg2
from psycopg2 import OperationalError

try:
    # Ganti parameter sesuai dengan informasi koneksi Anda
    connection = psycopg2.connect(
        database="defaultdb",
        user="avnadmin",
        password="AVNS_WKCKGD4JC5s0lel9zKD",
        host="pg-dev-dev-101.a.aivencloud.com",
        port="16506"
    )

    # Jika berhasil terkoneksi, cetak pesan sukses
    print("Koneksi berhasil!")

    # Tutup koneksi setelah selesai
    connection.close()

except OperationalError as e:
    # Jika terdapat kesalahan, cetak pesan kesalahan
    print(f"Kesalahan koneksi: {e}")