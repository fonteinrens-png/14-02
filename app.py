import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. CONFIGURATIE & CSS (Compacte weergave)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Rens & Rens Quiz", page_icon="❤️", layout="wide")

st.markdown("""
    <style>
    /* 1. Verwijder de standaard enorme witruimte van Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100%;
    }
    
    /* 2. Achtergrondkleur */
    .stApp {
        background-color: #fce4ec;
        color: #880e4f;
    }

    /* 3. Knoppen styling */
    div.stButton > button {
        background-color: #e91e63;
        color: white;
        border-radius: 15px;
        border: none;
        padding: 8px 16px;
        font-weight: bold;
        width: 100%;
        margin-top: 5px;
    }
    div.stButton > button:hover {
        background-color: #c2185b;
        color: white;
        border-color: #c2185b;
    }

    /* 4. Titel styling compact maken */
    h1 {
        color: #d81b60;
        text-align: center;
        margin-bottom: 0px;
        font-size: 2rem;
        padding: 0;
    }
    h3 {
        margin-top: 0;
        padding-top: 0;
    }

    /* 5. Input veld centreren */
    .stTextInput > div > div > input {
        text-align: center;
        border: 2px solid #f48fb1;
    }
    
    /* 6. Footer verbergen */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DE VRAGENLIJST
# -----------------------------------------------------------------------------
vragen_lijst = [
    {
        "foto": "foto1.jpeg",
        "vraag": "Wat is Rens💪 zijn favoriete broodje van Nonna?",
        "keuzes": ["SALAME FINOCCHIONA", "SALAME TOSCANE", "COPPA DI PARMA", "Broodje duivenstront"],
        "antwoord": "COPPA DI PARMA"
    },
    {
        "foto": "foto2.jpeg",
        "vraag": "Hoeveel mensen waren er op dit feest?",
        "keuzes": ["<20", "20-50", "weet ik veel - te weinig"],
        "antwoord": "weet ik veel - te weinig"
    },
    {
        "foto": "foto3.jpeg",
        "vraag": "Hoeveel slokken nam Renske van dit drankje?",
        "keuzes": ["ze vond het heerlijk en dronk het helemaal op", "ze vond het smerig nam 1 slok en gaf Rens💪 de rest"],
        "antwoord": "ze vond het smerig nam 1 slok en gaf Rens💪 de rest"
    },
    {
        "foto": "foto4.jpeg",
        "vraag": "Hoevaak heeft RensKE gewonnen van Rens💪 met keer op keer?",
        "keuzes": ["Een paar keer", "Altijd!", "nog nooit"],
        "antwoord": "nog nooit"
    },
    {
        "foto": "foto5.jpeg",
        "vraag": "Wat was de leukste date?",
        "keuzes": ["Doolhof", "Kaarslicht", "Schilderen", "Allemaal"],
        "antwoord": "allemaal"
    },
    {
        "foto": "foto6.jpeg",
        "vraag": "Wat kreeg Renske na het bezoek aan de vlindertuin?",
        "keuzes": ["Vlinders in haar buik", "Rode wangen van het blozen", "Een les over kruisbestuiving"],
        "antwoord": "Vlinders in haar buik"
    },
    {
        "foto": "foto7.jpeg",
        "vraag": "Wat is Rens💪 zijn favoriete Calzone?",
        "keuzes": ["Die van RensKE", "Normale", "Pollo"],
        "antwoord": "Normale"
    },
    {
        "foto": "foto8.jpeg",
        "vraag": "Wat is de mooiste stad van Nederland?",
        "keuzes": ["Roffa", "Utje", "Gouda", "Duiven"],
        "antwoord": "Utje"
    },
    {
        "foto": "foto9.jpeg",
        "vraag": "Waarom trekt RensKE haren uit Rens💪 zijn hoofd?",
        "keuzes": ["Dat vindt Rens💪 fijn", "RensKE doet aan sadisme"],
        "antwoord": "RensKE doet aan sadisme"
    },
    {
        "foto": "foto10.jpeg",
        "vraag": "Wie is de leukste?",
        "antwoord": "rens" 
    }
]

# -----------------------------------------------------------------------------
# 3. SESSIE STATUS
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

# -----------------------------------------------------------------------------
# 4. LOGICA
# -----------------------------------------------------------------------------
def check_answer(user_input):
    current_q = vragen_lijst[st.session_state.q_index]
    
    if user_input.strip().lower() == current_q['antwoord'].lower():
        st.toast("Goedzo! 🎉", icon="✅") # Toast is subtieler dan success bericht
        time.sleep(0.5)
        
        if st.session_state.q_index < len(vragen_lijst) - 1:
            st.session_state.q_index += 1
            st.rerun()
        else:
            st.session_state.stage = 'end'
            st.rerun()
    else:
        st.toast("Helaas, fout! ❤️", icon="❌")

# -----------------------------------------------------------------------------
# 5. UI OPBOUW
# -----------------------------------------------------------------------------

# --- START SCHERM ---
if st.session_state.stage == 'start':
    st.markdown("<br><br>", unsafe_allow_html=True) # Beetje witruimte om te centreren
    st.title("Valentijns Quiz 💌")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("10 vragen over ons. Weet jij alles nog?")
        st.write("**Er staat veel op het spel...**")
        if st.button("Start de Quiz", use_container_width=True):
            st.session_state.stage = 'quiz'
            st.rerun()

# --- QUIZ SCHERM ---
elif st.session_state.stage == 'quiz':
    q_data = vragen_lijst[st.session_state.q_index]
    
    # Progress bar heel dun bovenaan
    st.progress((st.session_state.q_index) / len(vragen_lijst))
    
    # Twee kolommen: Links Foto, Rechts Vraag
    col_img, col_txt = st.columns([1, 1], gap="medium")
    
    with col_img:
        # Foto tonen met vaste hoogte zodat pagina niet verspringt
        try:
            # We gebruiken HTML om de hoogte te forceren (max 60% van schermhoogte)
            st.image(q_data['foto'], use_container_width=True)
        except:
            st.error("Foto mist.")

    with col_txt:
        # Vraag en knoppen
        st.markdown(f"### Vraag {st.session_state.q_index + 1}")
        st.markdown(f"**{q_data['vraag']}**")
        
        if "keuzes" in q_data:
            for keuze in q_data['keuzes']:
                if st.button(keuze):
                    check_answer(keuze)
        else:
            with st.form(key=f"form_{st.session_state.q_index}", clear_on_submit=True):
                user_text = st.text_input("Antwoord:", key="input_text")
                if st.form_submit_button("Controleer"):
                    check_answer(user_text)

# --- EIND SCHERM ---
elif st.session_state.stage == 'end':
    st.balloons()
    st.title("Gewonnen! 💖")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.write("Je bent de allerleukste!")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/English_pattern_10_of_hearts.svg/200px-English_pattern_10_of_hearts.svg.png", width=100)
        st.markdown("### 🎁 Je Cadeau:")
        st.success("🥂 Romantisch diner voor twee!\n\n📅 13-02 - 18:00\n\n📍 Oudegracht aan de Werf 159k")

    with c2:
        # Collage compact houden
        st.write("**Memory Lane:**")
        
        # Grid van 2x5 voor compactheid
        grid_col1, grid_col2 = st.columns(2)
        for i in range(10):
            target_col = grid_col1 if i < 5 else grid_col2
            with target_col:
                try:
                    st.image(f"foto{i+1}.jpeg", use_container_width=True)
                except:
                    pass
