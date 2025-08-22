import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Ambil URL database dari environment
DATABASE_URL = os.getenv("DATABASE_URL")

@pytest.mark.skipif(not DATABASE_URL, reason="DATABASE_URL environment variable not set")
def test_database_connection():
    try:
        # 1. Membuat engine untuk koneksi ke database
        engine = create_engine(DATABASE_URL)

        # 2. Mencoba membuka koneksi dan menjalankan query sederhana
        with engine.connect() as connection:
            print("\n✅ Koneksi ke database berhasil dibuat.")
            
            # 3. Menjalankan query 'SELECT 1' untuk memastikan DB responsif
            result = connection.execute(text("SELECT 1"))
            
            # 4. Memeriksa hasil query
            assert result.scalar() == 1
            print("✅ Query 'SELECT 1' berhasil dieksekusi dan mengembalikan nilai 1.")

    except Exception as e:
        # Jika terjadi error apapun selama proses koneksi atau query,
        # tes akan gagal dan pytest akan menampilkan pesan error ini.
        pytest.fail(f"Gagal terhubung ke database. Error: {e}")