
import streamlit as st

st.set_page_config(page_title="COS 101 Group Dictionary", page_icon="📖", layout="wide")

# Custom CSS for polished interface
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .translation-card {
        padding: 30px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-left: 8px solid #ff4b4b;
        margin-top: 20px;
    }
    .word-label { color: #666; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
    .english-word { color: #222; font-size: 32px; font-weight: bold; margin-bottom: 10px; }
    .native-word { color: #ff4b4b; font-size: 45px; font-weight: 800; margin-top: 0; }
    </style>
    """, unsafe_allow_html=True)

dictionary = {
    "Yoruba": {
        "Man": "Ọkùnrin", "Woman": "Obìnrin", "Father": "Bàbá", "Mother": "Ìyá",
        "Water": "Omi", "Bread": "Búrẹ́dì", "Sun": "Òòrùn", "Moon": "Òṣùpá",
        "Head": "Orí", "Hand": "Ọwọ́", "Leg": "Ẹsẹ̀", "House": "Ilé",
        "Road": "Ọ̀nà", "King": "Ọba", "God": "Ọlọ́run", "Love": "Ìfẹ́",
        "Money": "Owó", "Work": "Iṣẹ́", "School": "Ilé-ẹ̀kọ́", "Book": "Ìwé"
    },
    "Hausa": {
        "Man": "Namiji", "Woman": "Mace", "Father": "Uba", "Mother": "Uwa",
        "Water": "Ruwa", "Bread": "Burodi", "Sun": "Rana", "Moon": "Wata",
        "Head": "Kai", "Hand": "Hannu", "Leg": "Kafa", "House": "Gida",
        "Road": "Hanya", "King": "Sarki", "God": "Allah", "Love": "Soyayya",
        "Money": "Kudi", "Work": "Aiki", "School": "Makarantar", "Book": "Littafi"
    },
    "Idoma": {
        "Man": "Onyecho", "Woman": "Onyanyi", "Father": "Ada", "Mother": "Ene",
        "Water": "Enkpo", "Bread": "Eburedi", "Sun": "Eñu", "Moon": "Ọda",
        "Head": "Echi", "Hand": "Abọ", "Leg": "Ofu", "House": "Ole",
        "Road": "Ipue", "King": "Och'Idoma", "God": "Owoicho", "Love": "Ihotu",
        "Money": "Ije", "Work": "Ilo", "School": "Sukulu", "Book": "Ukpa"
    },
    "Khana": {
        "Man": "Nom", "Woman": "Wa", "Father": "Teè", "Mother": "Kà",
        "Water": "Mmuù", "Bread": "Beredi", "Sun": "Dee", "Moon": "Ẹ̀en",
        "Head": "Tọ", "Hand": "Bọ̀", "Leg": "Tè", "House": "Beè",
        "Road": "Kpò", "King": "Mene", "God": "Bari", "Love": "Whala",
        "Money": "Kpègè", "Work": "Tom", "School": "Sukul", "Book": "Kpá"
    },
    "Igala": {
        "Man": "Onẹ-kele", "Woman": "Onẹ-obulẹ", "Father": "Atá", "Mother": "Iyé",
        "Water": "Omi", "Bread": "Eburedi", "Sun": "Ólu", "Moon": "Óchu",
        "Head": "Éjú", "Hand": "Ọwọ́", "Leg": "Akwu", "House": "Unyi",
        "Road": "Ofu", "King": "Onu", "God": "Ọjọ", "Love": "Ífẹ́",
        "Money": "Ẹyọ", "Work": "Uchẹ", "School": "Isukulu", "Book": "Otakada"
    }
}


def main():
    st.title("📚 COS 101 Group Dictionary")
    st.markdown("### English to Nigerian Tribal Languages")
    st.divider()

    st.sidebar.header("Navigation")
    tribe = st.sidebar.selectbox("Select Tribe", list(dictionary.keys()))
    view_mode = st.sidebar.radio("View Mode", ["Search Word", "Full Dictionary"])

    st.sidebar.markdown("---")
    st.sidebar.info("Project: COS 101 Assignment")

    if view_mode == "Search Word":
        st.subheader(f"Translate to {tribe}")
        options = list(dictionary[tribe].keys())
        query = st.selectbox("Select English Word:", [""] + options)

        if query:
            translation = dictionary[tribe][query]
            st.markdown(f"""
                <div class="translation-card">
                    <div class="word-label">English Word</div>
                    <div class="english-word">{query}</div>
                    <hr style="border: 0.5px solid #eee; margin: 20px 0;">
                    <div class="word-label">{tribe} Translation</div>
                    <div class="native-word">{translation}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Select a word above to see the translation results.")

    else:
        st.subheader(f"{tribe} Lexicon (20 Words)")
        table_data = [{"English Word": eng, f"{tribe} Translation": nat} for eng, nat in dictionary[tribe].items()]
        st.table(table_data)


if __name__ == "__main__":
    main()