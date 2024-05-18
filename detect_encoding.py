import pandas as pd
import chardet

def read_csv_with_encoding(file_path):
    with open(file_path, 'rb') as f:
        # Baca sebagian data file untuk mendeteksi encoding
        rawdata = f.read()
        # Deteksi encoding
        encoding = chardet.detect(rawdata)['encoding']
    
    # Baca file CSV dengan encoding yang terdeteksi
    df = pd.read_csv(file_path, encoding=encoding)
    return df

# Path file CSV
file_path = 'Sample - Superstore.csv'

try:
    # Membaca file CSV
    df = pd.read_csv(file_path)
    # Jika berhasil, tampilkan DataFrame
    print(df.head())
except UnicodeDecodeError:
    # Jika terjadi UnicodeDecodeError, coba baca file dengan deteksi encoding otomatis
    df = read_csv_with_encoding(file_path)
    # Tampilkan DataFrame
    print(df.head())
