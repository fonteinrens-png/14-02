import streamlit as st
import time
import base64
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURATIE & CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Rens & Rens Quiz", page_icon="❤️")

st.markdown("""
    <style>
    /* Maak de app compact */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 600px;
    }
    
    .stApp {
        background-color: #fce4ec;
        color: #880e4f;
    }

    /* Knoppen styling - Compact en duidelijk */
    div.stButton > button {
        background-color: #e91e63;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 8px 10px; /* Iets minder padding */
        font-weight: bold;
        width: 100%;
        margin-top: 5px;
        font-size: 14px;
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        background-color: #c2185b;
        transform: scale(1.01);
    }

    /* Titel styling */
    h1 {
        color: #d81b60;
        text-align: center;
        font-size: 1.8rem;
        margin-bottom: 5px;
        margin-top: 0;
    }
    
    /* Input velden centreren */
    .stTextInput > div > div > input {
        text-align: center;
        border: 2px solid #f48fb1;
        border-radius: 10px;
        padding: 8px;
    }
    
    /* Footer weg */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. HULPFUNCTIE: FOTO LADEN
# -----------------------------------------------------------------------------
def get_img_as_base64(file_path):
    """Zet afbeelding om naar base64 string voor HTML weergave"""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# -----------------------------------------------------------------------------
# 3. DE VRAGENLIJST
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
# 4. SESSIE STATUS
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

# -----------------------------------------------------------------------------
# 5. LOGICA
# -----------------------------------------------------------------------------
def check_answer(user_input):
    current_q = vragen_lijst[st.session_state.q_index]
    
    if user_input.strip().lower() == current_q['antwoord'].lower():
        st.toast("Goedzo! 🎉", icon="✅")
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
# 6. UI OPBOUW
# -----------------------------------------------------------------------------

# --- START SCHERM ---
if st.session_state.stage == 'start':
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Valentijns Quiz 💌")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("10 vragen over ons. Weet jij alles nog?")
        st.write("**Er staat veel op het spel...**")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Start de Quiz", use_container_width=True):
            st.session_state.stage = 'quiz'
            st.rerun()

# --- QUIZ SCHERM ---
elif st.session_state.stage == 'quiz':
    q_data = vragen_lijst[st.session_state.q_index]
    
    # Progress bar (klein)
    st.progress((st.session_state.q_index) / len(vragen_lijst))
    
    # 1. FOTO MET HTML (De truc voor perfecte hoogte zonder scrollen)
    # We zetten max-height op 45vh (45% van schermhoogte)
    img_b64 = get_img_as_base64(q_data['foto'])
    
    if img_b64:
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="data:image/jpeg;base64,{img_b64}" '
            f'style="max-height: 40vh; max-width: 100%; object-fit: contain; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.error(f"Foto '{q_data['foto']}' niet gevonden.")

    # 2. VRAAG & KNOPPEN
    st.markdown(f"<h3 style='text-align: center; margin-bottom: 5px; font-size: 1.2rem;'>Vraag {st.session_state.q_index + 1}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-weight: bold; margin-bottom: 10px;'>{q_data['vraag']}</p>", unsafe_allow_html=True)
    
    if "keuzes" in q_data:
        for keuze in q_data['keuzes']:
            if st.button(keuze):
                check_answer(keuze)
    else:
        with st.form(key=f"form_{st.session_state.q_index}", clear_on_submit=True):
            user_text = st.text_input("Antwoord:", key="input_text", label_visibility="collapsed", placeholder="Typ je antwoord...")
            if st.form_submit_button("Controleer"):
                check_answer(user_text)

# --- EIND SCHERM ---
elif st.session_state.stage == 'end':
    st.balloons()
    st.title("Gewonnen! 💖")
    
    st.markdown("<p style='text-align: center;'>Je bent de allerleukste!</p>", unsafe_allow_html=True)
    
    # Harten 10
    st.markdown(
        '<div style="display: flex; justify-content: center; margin-bottom: 15px;">'
        '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/English_pattern_10_of_hearts.svg/200px-English_pattern_10_of_hearts.svg.png" width="100">'
        '</div>', 
        unsafe_allow_html=True
    )
    
    st.success("### 🎁 Je Cadeau:\n\n🥂 **Romantisch diner voor twee!**\n\n📅 13-02 - 18:00\n\n📍 Oudegracht aan de Werf 159k")

    st.markdown("---")
    st.write("**Memory Lane:**")
    
    # Collage
    grid_col1, grid_col2 = st.columns(2)
    for i in range(10):
        target_col = grid_col1 if i < 5 else grid_col2
        with target_col:
            try:
                st.image(f"foto{i+1}.jpeg", use_container_width=True)
            except:
                pass
