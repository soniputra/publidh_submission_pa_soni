import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Atur layout
st.set_page_config(layout="wide", page_title="Notasonda Soni Putra - Dicoding", page_icon=":shopping_bags:")

# Pertanyaan
with st.container():
    # Section 1
    st.markdown("""<h1 style='text-align:center;margin-bottom:50px'> Notasonda Soni Putra - Dicoding </h1>""", unsafe_allow_html=True)

    # Column 1
    col1, col2, col3 = st.columns((2,2,1.5))
    with col1:
        st.header("Question 1:")
        st.markdown("""<span>
                    Geografis State pembeli terbanyak berada dimana?
                    </span>""", unsafe_allow_html=True)

    with col2:
        st.header("Question 2:")
        st.markdown("""<span>
                    Berapa presentase tingkat kepuasan pembeli dalam total penjualan?
                    </span>""", unsafe_allow_html=True)

    with col3:
        st.header("Additional Question:")
        st.markdown("""<span>Bagaimana persebaran pengguna E-Commerce?</span>""", unsafe_allow_html=True)

with st.container():
    tab1, tab2, tab3 = st.tabs(["Question 1", "Question 2", "Additional Question"])

    # Tab Customer (Question 1)
    with tab1:
        col1, col2 = st.columns((0.5, 0.8))
        df_customer = pd.read_csv("customers_dataset.csv")
        df_customer_baru = df_customer.drop(['customer_id', 'customer_unique_id'], axis=1)
        # Mengambil data sample secara acak sebesar 50% dari jumlah data (Tujuannya agar lebih cepat dikarenakan data lebih dari 400rb data)
        df_customer_baru = df_customer_baru.sample(frac=0.5, replace=True).reset_index()
        with col1:
            customer_state_list = st.multiselect(
            "Select Customer State",
            options = df_customer_baru["customer_state"].unique(),
            default = df_customer_baru["customer_state"].unique()
            )
            df_customer_state_sel = df_customer_baru.query(
                "customer_state == @customer_state_list"
            )
        with col2:
            st.subheader("Visualization")
            geog_state_vis = px.bar(
                df_customer_state_sel,
                x=df_customer_state_sel["customer_state"],
                y = df_customer_state_sel["customer_state"].index,
                title = "Customer State Demographic",
                template="seaborn"
            )
            st.plotly_chart(geog_state_vis)
            
    # Tab Order (Question 2)
    with tab2:
        col1, col2 = st.columns((0.5, 0.8))
        df_order = pd.read_csv("order_reviews_dataset.csv")
        df_order_baru = df_order.drop(['review_id', 'order_id', 'review_comment_title', 'review_comment_message'], axis=1)
        # Mengambil data sample secara acak sebesar 50% dari jumlah data (Tujuannya agar lebih cepat dikarenakan data lebih dari 400rb data)
        df_order_baru = df_order_baru.sample(frac=0.5, replace=True).reset_index()
        with col1:
            review_score_list = st.multiselect(
                "Select Review",
                options = df_order_baru["review_score"].unique(),
                default = df_order_baru["review_score"].unique()
            )
            df_review_score_sel = df_order_baru.query(
                "review_score == @review_score_list"
            )
        with col2:
            st.subheader("Visualization")
            # Total Review
            st.markdown("""<div style='text-align:center;font-size:30px'> Tingkat Kepuasan Pelanggan </div> """, unsafe_allow_html=True)
            total_review = int(df_review_score_sel["review_score"].sum())
            rata_rata = round(df_review_score_sel["review_score"].mean())
            animasi = ":star:" * int(round(rata_rata, 2))

            col_kanan, col_kiri = st.columns(2)
            with col_kanan:
                st.subheader("Total Review :")
                st.markdown(""f" <div style='font-size:25px;font-weight:bolder;font-family:poppins;'> {total_review} Pengguna </div>""", unsafe_allow_html=True)
            with col_kiri:
                st.subheader("Rata - rata Rating :")
                st.subheader(f"{rata_rata} {animasi}")
            
            # Visualisasi Review
            order_rev_vis = px.pie(
                df_customer_state_sel,
                values = df_review_score_sel["review_score"].value_counts(),
            )
            st.plotly_chart(order_rev_vis)
    
    with tab3:
        # Insert Datasets
        st.markdown("""<h3 style='text-align:center;margin-bottom:50px'> Mapping Geolocation Dataset </h3>""", unsafe_allow_html=True)
        df_geo = pd.read_csv("geolocation_dataset.csv")
        # Mengambil data sample secara acak sebesar 50% dari jumlah data (Tujuannya agar lebih cepat dikarenakan data lebih dari 400rb data)
        df_geo = df_geo.sample(frac=0.5, replace=True).reset_index()
        map_list = st.multiselect(
            "Select Geolocation Mapping",
            options = df_geo["geolocation_state"].unique(),
            default = df_geo["geolocation_state"].unique()
        )
        df_map_sel = df_geo.query(
            "geolocation_state == @map_list"
        )
        st.map(df_map_sel,
            latitude= 'geolocation_lat',
            longitude='geolocation_lng',
            zoom = 2,
            size = 100
        )
                    

    # Divider Line
    st.markdown("""<hr style="height:2px;border:none;color:orange;background-color:orange;" /> """, unsafe_allow_html=True)
    

with st.container():
    q1, q2, aq = st.columns(3)

    with q1:
        st.subheader("Conclusion Question 1")
        st.markdown(""" <div style='text-align:justify'>Dari hasil analisa dan visualisasi hasil didapatkan kesimpulan yaitu, pembeli terbanyak di dalam e-commerce berasal dari state SP. Yang dimana hasil dari analisa tersebut dapat digunakan oleh pihak e-commerce untuk melakukan bahan evaluasi diantaranya sebagai berikut:
                    <li>Dapat digunakan sebagai bahan untuk memberikan diskon atau sejenisnya berdasarkan zonasi,
                    </li>
                    <li>Melakukan kegiatan periklanan atau mengadakan event-event di state customer yang terendah dalam hal ini state RR
                    </li>
                    </div> """, unsafe_allow_html=True)
    with q2:
        st.subheader("Conclusion Question 2")
        st.markdown(""" <div style='text-align:justify'>
                    Dari hasil analisa dan visualisasi hasil pada pertanyaan ke-2 diketahui bahwasannya, tingkat kepuasan pelanggan dalam melakukan 
                    pemesanan yang memberikan bintang 5 sebanyak 57.8% dan yang memberikan bintang 1 sebanyak 11.5%. Sehingga dari analisa tersebut 
                    didapatkan sebuah hasil yaitu jumlah costumer yang puas akan barang yang dipesan sangat baik berada di 50% lebih namun diperhatikan 
                    juga bahwasannya costumer yang tidak puas dengan barang yang dipesan berada di 11.5% sehingga perlu dilakukannya evaluasi dari respon para pembeli.
                    </div> """, unsafe_allow_html=True)
    with aq:
        st.subheader("Conclusion Additional Question")
        st.markdown(""" <div style='text-align:justify'>Berdasarkan hasil visualisasi Mapping diketahui bahwa rata-rata pengguna aplikasi E-commerce berasal dari
                    Benua Amerika Selatan khususnya negara Brazil
                    </div> """, unsafe_allow_html=True)

# Footer
st.markdown(""" <footer style='text-align:center; margin-top:50px'>&copy; Notasonda Soni Putra - Dicoding 2023</footer> """, unsafe_allow_html=True)