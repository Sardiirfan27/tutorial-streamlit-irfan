import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import state_abb

#st.set_page_config(layout="wide")

'''
## Magic Commands - Dataframe
Berikut ini adalah dataframe dari aplikasi saya
'''

#tanpa magic command
st.write('Dataset Sales Superstore:')
df= pd.read_csv('Sample - Superstore.csv',encoding='cp1252')
st.write(df)
# st.dataframe(df)

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
    

#custom theme
st.markdown('# Custom Theme')
video_url= 'https://youtu.be/Mz12mlwzbVU?t=212'
st.video(video_url, start_time= 212)

# memuat file CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("./.streamlit/style.css")
st.markdown('<div class="custom-text">This is custom text with Montserrat font!</div>', unsafe_allow_html=True)

#Membuat Chart
st.markdown('# Membuat Chart')
st.markdown('Referensi untuk membuat chart: [link_1](https://streamlit.io/components?category=charts)')
st.link_button("Streamlit Widget", "https://docs.streamlit.io/develop/api-reference/widgets")

# Membuat bar chart
# Mengelompokkan data berdasarkan Sub-Category dan menghitung total Sales
sales_by_sub_category = df.groupby('Sub-Category')['Sales'].sum().reset_index()
# top-5 Sub-Category
top_sales_by_sub_category = sales_by_sub_category.nlargest(5, 'Sales')

# Menggunakan matplotlib untuk membuat bar chart
fig, ax = plt.subplots()
ax.bar(top_sales_by_sub_category['Sub-Category'], 
       top_sales_by_sub_category['Sales'])
ax.set_xlabel('Sub-Category')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales by Sub-Category')
# rotate x-axis labels
ax.tick_params(axis='x', labelrotation=90)
st.pyplot(fig) # Tampilkan bar chart


# Mengelompokkan data berdasarkan Sub-Category dan menghitung total Sales
sales_by_sub_category = df.groupby('Sub-Category')['Sales'].sum().reset_index()

# Memilih jumlah top sub-categories menggunakan slider
top_n = st.slider('Pilih jumlah top Sub-Category:', min_value=1, max_value=10, value=5)
top_sales_by_sub_category = sales_by_sub_category.nlargest(top_n, 'Sales')

# Menggunakan Plotly untuk membuat bar chart
fig = px.bar(top_sales_by_sub_category, 
             x='Sub-Category', 
             y='Sales', 
             title='Total Sales by Sub-Category',
             labels={'Sub-Category': 'Sub-Category', 'Sales': 'Total Sales'},
             template='plotly_white')

# Rotate x-axis labels
fig.update_layout(xaxis_tickangle=-90)

# Tampilkan bar chart di Streamlit
st.plotly_chart(fig)

# Menghitung jumlah setiap Kategori Produk
category_counts = df['Category'].value_counts()

# Membuat pie chart dengan Plotly dan mengatur ukuran fig
fig = px.pie(category_counts, 
             values=category_counts.values, 
             names=category_counts.index, 
             title='Persentase Kategori Produk',
             width=800,  # Atur lebar figure
             height=600) # Atur tinggi figure

# Tampilkan pie chart di Streamlit
st.plotly_chart(fig)


# Create new column with State Abbreviations
df['State_abb'] = df['State'].replace(state_abb.us_state_to_abbrev)
# Plot

fig = go.Figure(data=go.Choropleth(
    locations= df['State_abb'].value_counts().index, # Spatial coordinates
    z = df['State_abb'].value_counts(), # Data to be color-coded
    locationmode = 'USA-states',
    colorscale = 'teal', zmin = 1, zmax = 1000
))

fig.update_layout(
    font = dict(
            size = 14
            ),    
    title={
        'text': "Number of Customers by State Map",
        'y':0.95,
        'x':0.5
        },
    geo_scope='usa', # limite map scope to USA
)

# Tampilkan peta di Streamlit
st.plotly_chart(fig)





# Grouping data berdasarkan negara (Country), kota (City), dan negara bagian (State) dan menjumlahkan kuantitas penjualan (Quantity)
location_sales = df.groupby(['Country', 'State_abb', 'City'])['Quantity'].sum().reset_index()

# Membuat peta dengan Plotly dan mengatur jenis peta serta menentukan data yang ditampilkan
fig = px.scatter_geo(location_sales, 
                     locationmode='USA-states',  # Menentukan mode lokasi (negara)
                     locations='State_abb',           # Kolom yang berisi nama negara
                     color='City',                 # Warna titik 
                     size='Quantity',               # Ukuran titik berdasarkan jumlah penjualan
                     hover_name='State_abb',             # Informasi yang muncul saat hover
                     title='Jumlah Penjualan berdasarkan Lokasi', 
                     projection='natural earth')   # Proyeksi peta

# Tampilkan peta di Streamlit
st.plotly_chart(fig)


