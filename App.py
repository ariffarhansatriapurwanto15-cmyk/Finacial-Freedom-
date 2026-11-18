
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Financial Freedom",
    page_icon="💰",
    layout="wide"
)

st.title("💰 FINANCIAL FREEDOM")
st.subheader("Personal Finance Dashboard")

st.divider()

st.header("📝 Input Keuangan")

pemasukan = st.number_input(
    "Pemasukan (Rp)",
    min_value=0,
    value=1000000,
    step=50000
)

makanan = st.number_input("Pengeluaran Makanan", min_value=0, value=200000)
transportasi = st.number_input("Pengeluaran Transportasi", min_value=0, value=100000)
hiburan = st.number_input("Pengeluaran Hiburan", min_value=0, value=100000)
lainnya = st.number_input("Pengeluaran Lainnya", min_value=0, value=50000)

total = makanan + transportasi + hiburan + lainnya
sisa = pemasukan - total

st.divider()
st.header("📊 Ringkasan Keuangan")

col1, col2, col3 = st.columns(3)

col1.metric("Pemasukan", f"Rp{pemasukan:,}")
col2.metric("Pengeluaran", f"Rp{total:,}")
col3.metric("Sisa Uang", f"Rp{sisa:,}")

st.header("🎯 Target Tabungan")

if sisa >= 250000:
    st.success("Target tabungan tercapai!")
else:
    st.warning("Ayo hemat pengeluaran!")

data = {
    "Kategori": ["Makanan", "Transportasi", "Hiburan", "Lainnya"],
    "Jumlah": [makanan, transportasi, hiburan, lainnya]
}

fig = px.pie(
    data,
    names="Kategori",
    values="Jumlah",
    title="Grafik Pengeluaran",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)
