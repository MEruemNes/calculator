import streamlit as st

st.set_page_config(page_title="Modül Seçimi", layout="centered")

st.title("📚 Modül Seçimi Yapınız")

modul = st.radio(
    "Lütfen bir modül seçin:",
    ("1 - A1", "2 - A2", "3 - B1", "4 - B2")
)

linkler = {
    "1 - A1": "https://modals-g7cu5ktfzykprym4cgb6gg.streamlit.app/",
    "2 - A2": "https://modals-auezyp3qed7n9c2x2rdmae.streamlit.app/",
    "3 - B1": "https://modals-6kbg3v67mqrpf3non4ntp3.streamlit.app/",
    "4 - B2": "https://calculator-hfncgbvh6bcf4aeqmbdewf.streamlit.app/"
}

# Seçilen modül için bağlantı göster
secilen_link = linkler[modul]
st.markdown(f"[👉 Seçtiğiniz modüle gitmek için buraya tıklayın]({secilen_link})", unsafe_allow_html=True)
