from streamlit.components.v1 import html
import streamlit as st

# Menambahkan CSS kustom untuk mengubah font header
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
}
</style>
"""

# Menyematkan CSS di aplikasi Streamlit
html(css)

# Contoh penggunaan header di Streamlit
st.header("Ini adalah header dengan font Montserrat")
st.subheader("Ini adalah subheader dengan font Montserrat")
st.write("Ini adalah teks biasa.")