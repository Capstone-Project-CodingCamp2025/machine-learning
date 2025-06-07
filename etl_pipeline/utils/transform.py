import pandas as pd
import os

def transform_data(dataframe, path='gambar_data/', nama_file='transformed.csv'):
    '''
    Meng-transform dataframe dengan menambahkan path gambar untuk setiap tempat destinasi dalam bentuk list, dan menghapus kolom yang tidak dibutuhkan beserta missing values
    
    dataframe: dataframe dari data hasil extract
    path: path dari folder gambar
    nama_file: nama file.csv yang akan di-export
    
    output: file .csv yang sudah ada kolom gambar beserta tidak ada missing values
    '''
    
    # Membuat Kolom 'gambar' dalam dataframe
    dataframe['gambar'] = None
    
    # Membaca path dan nama files dalam folder yang disimpan gambar
    for root, dirs, files in os.walk(path):
        # Membaca index dan baris dari dataframe
        for index, row in dataframe.iterrows():
            data = []
            if row['nama_tempat'] == root.replace('gambar_data/', ''):
                for i in files:
                    data.append(os.path.join(root, i))
                
                # Menambahkan data gambar sesuai dengan nama tempat ke dalam kolom 'gambar'
                dataframe.at[index, 'gambar'] = data.copy()
    
    # Menghapus missing values dan kolom yang tidak dibutuhkan
    dataframe.dropna(subset='gambar', inplace=True)            
    dataframe.drop(['Unnamed: 0', 'kategori'], axis=1, inplace=True)
    
    description = pd.read_csv('data/description.csv')
    
    add_description = description.merge(dataframe, on='nama_tempat', how='left')
    
    # Export ke dalam file .csv
    add_description.to_csv(nama_file, index=False)    

    print('Data berhasil di-transform')
    
    
def main():
    df = pd.read_csv('all_data.csv')
    
    transform_data(df)
    
if __name__ == '__main__':
    main()