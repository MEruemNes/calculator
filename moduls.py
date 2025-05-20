import streamlit as st

st.set_page_config(page_title="Modül Seçimi", layout="centered")

st.title("📚 Modül Seçimi Yapınız")

modul = st.radio(
    "Lütfen bir modül seçin:",
    ("1 - A1", "2 - A2", "3 - B1", "4 - B2")
)

linkler = {
    "1 - A1": "https://calculator-zgkkmd8uwzx7opoph6p9af.streamlit.app/",
    "2 - A2": "https://modals-3h6eb69pkbcyk63hgxux98.streamlit.app/",
    "3 - B1": "https://calculator-spsxvhcsbgr9fj4v9f8mmg.streamlit.app/",
    "4 - B2": "https://calculator-jctqjn5zjrrasjtf2jw5wi.streamlit.app/"
}

if st.button("Devam Et"):
    secilen_link = linkler.get(modul)
    js = f"""
    <meta http-equiv="refresh" content="0; url={secilen_link}">
    <p>Yönlendiriliyorsunuz... Eğer yönlendirilmezseniz <a href="{secilen_link}">buraya tıklayın</a>.</p>
    """
    st.markdown(js, unsafe_allow_html=True)
