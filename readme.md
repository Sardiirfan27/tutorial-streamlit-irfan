# Langkah-Langkah dalam Pembuatan Project
## Persiapan Environment
- Buatlah folder untuk project anda, misalkan folder `APP_1`.
- Buatlah environment menggunakan perintah berikut ini dan jalankan di terminal:
    ```
    python -m venv env_name
    ```
- Jalankan environment yang telah di buat:
    Mac:
    ```
    source env/bin/activate
    ```
    Windows:
    ```text
    env/Scripts/activate.bat //In CMD
    env/Scripts/Activate.ps1 //In Powershel
    ```
- Setelah environment yang buat sudah aktif, lakukan instalasi library yang dibutuhkan menggunakan perintah berikut:
    ```
    pip install pandas streamlit matplotlib plotly seaborn
    ```
- setelah semua library terinstal, kita dapat menghasilkan list semua depedensi atau libary yang telah di instal dengan menjalankan perintah berikut ini:
    ```
    pip freeze > requirements.txt
    ```

## Pembuatan Streamlit App
Selanjutnya kita akan membuat aplikasi streamlit sederhana.
- Buatlah file dalam project `main.py`
- Pada file `main.py` isi code berikut ini:
    ```
    import streamlit as st
    import pandas as pd

    '''
    ## Magic Commands - Test
    Berikut ini adalah dataframe dari aplikasi saya
    '''

    #tanpa magic command
    st.write('Dataset Sales Superstore:')
    df= pd.read_csv('train.csv')
    st.write(df)
    # st.dataframe(df)

    ```
- Jalankan streamlit :
    ```
    python3 -m streamlit run main.py
    ```

- tambahkan widget checkbox:
    ```python
    # gunakan checkbox untuk show/hide data
    if st.checkbox('Show dataframe'):
        #gunakan multiselect untuk memilih kolom yang ditampilkankan
        options= st.multiselect(label='Kolom yang ditampilkankan:', 
                                options=df.columns, 
                                default=df.columns.tolist()) #nilai defaultnya harus dalam bentuk list
        values = st.slider(
        "Rentang Baris",
        min_value=0, 
        max_value=len(df)-1, 
        value=(9, 14),# Nilai default adalah seluruh rentang dari baris pertama hingga terakhir
        step=1)  
    
        start = values[0]
        end = values[1]
        st.table(df.iloc[start:end+1])  #kita bisa gunakan st.table
    ```

- tambahkan video:
    ```python
    #custom theme
    st.markdown('Custom Theme')
    video_url= 'https://youtu.be/Mz12mlwzbVU?t=212'
    st.video(video_url, start_time= 212)
    ```

- Tambahkan CSS:
    - Buatlah style.css di folder `.streamlit`:
        ```css
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
        }

        .custom-text {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            font-weight: 400;
        }

        ```

    - Tambahkan code berikut di `main.py`:
        ```python
        # ref: https://fonts.google.com/selection
        # memuat file CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        local_css("./.streamlit/style.css")
        st.markdown('<div class="custom-text">This is custom text with Montserrat font!</div>', unsafe_allow_html=True)
        ```

- Tambahkan link referensi dan `link_button`:
```python
st.markdown('Referensi untuk membuat chart: [link_1](https://streamlit.io/components?category=charts)')
st.link_button("Streamlit Widget", "https://docs.streamlit.io/develop/api-reference/widgets")
```
- Tambahkan Bar Chart:
```python
# Mengelompokkan data berdasarkan Sub-Category dan menghitung total Sales
sales_by_sub_category = df.groupby('Sub-Category')['Sales'].sum().reset_index()
# top-5 Sub-Category
sales_by_sub_category = sales_by_sub_category.nlargest(5, 'Sales')

# Menggunakan matplotlib untuk membuat bar chart
fig, ax = plt.subplots()
ax.bar(sales_by_sub_category['Sub-Category'], 
       sales_by_sub_category['Sales'])
ax.set_xlabel('Sub-Category')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales by Sub-Category')
# rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Tampilkan bar chart
st.pyplot(fig)
```
