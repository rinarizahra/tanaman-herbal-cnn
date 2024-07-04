import streamlit as st
from utils import df_manfaat, example_names
st.set_page_config(
    page_title="Tanaman Herbal",
    page_icon="",
)
import os

st.markdown(
    f"""# 🌿 **Tanaman Herbal**

*Tanaman herbal adalah tumbuhan yang dipercaya memiliki berbagai kandungan vitamin dan mineral. Tujuannya yakni membantu mengatasi berbagai keluhan kesehatan. Ada berbagai bagian tanaman yang bisa digunakan sebagai obat herbal, mulai dari daun, akar, hingga bunganya.*

## 👉🏻 **Manfaat Tanaman Herbal**

"""
)
st.dataframe(df_manfaat)

st.header("👇🏻 Contoh Tanaman Herbal")
images = [os.path.join("./contoh_tanaman_herbal",i) for i in os.listdir("contoh_tanaman_herbal")]

st.image(images,width=200,caption=example_names)

