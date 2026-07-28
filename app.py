import json
import streamlit as st

# 1. Judul (Sesuaikan dengan contoh dosen)
st.title("📚 Book Search (Scraped via Scrapy)")

# Load Data
with open("data/books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# Input Pencarian
query = st.text_input("Cari..")

# Filter Data berdasarkan pencarian
if query:
    filtered_books = [
        b for b in books if query.lower() in b.get("title", "").lower()
    ]
else:
    filtered_books = books

# 2. Tampilan Jumlah Hasil (Gunakan emoji ✨ dan kata "Ditemukan X hasil")
st.subheader(f"✨ Ditemukan {len(filtered_books)} hasil")

# Tampilkan Daftar Buku
for book in filtered_books:
    st.markdown(f"### [{book['title']}]({book['link']})")
    st.markdown(
        f"**Price:** {book['price']} | **Rating:** {book['rating']} | **Availability:** {book['availability']}"
    )
    st.write("---")