import pandas as pd
from sqlalchemy import create_engine

def to_db(dataframe, db_url):
    '''Menambahkan data ke dalam basis data'''
    try:
        
        engine = create_engine(db_url)
        
        with engine.connect() as con:
            dataframe.to_sql('products', con=con, if_exists='append', index=False)
            print('Data berhasil ditambahkan ke dalam basis data')
    
    except Exception as e:
        print(f'Terjadi kesalahan saat menambahkan data ke dalam basis data: {e}')
        return None