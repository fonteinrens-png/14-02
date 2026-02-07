import streamlit as st
import time

# -----------------------------------------------------------------------------
# 1. CONFIGURATIE & CSS (Voor de roze stijl)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Rens & Rens Valentijnsquiz", page_icon="❤️")

# We injecteren wat CSS om de achtergrond roze te maken en knoppen te stylen
st.markdown("""
    <style>
    .stApp {
        background-color: #fce4ec;
        color: #880e4f;
    }
    /* Stijl voor de titel */
    h1 {
        color: #d81b60;
        text-align: center;
    }
    /* Stijl voor normale tekst */
    p {
        font-size: 1.1rem;
    }
    /* Custom button styling om ze roze te maken */
    div.stButton > button {
        background-color: #e91e63;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #c2185b;
        color: white;
        border-color: #c2185b;
    }
    /* Input velden centreren */
    .stTextInput > div > div > input {
        text-align: center;
        border: 2px solid #f48fb1;
    }
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
        "antwoord": "rens" # Geen keuzes, dus open vraag
    }
]

# -----------------------------------------------------------------------------
# 3. SESSIE STATUS (Geheugen van de app)
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'start' # Opties: 'start', 'quiz', 'end'
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

# -----------------------------------------------------------------------------
# 4. FUNCTIES
# -----------------------------------------------------------------------------
def check_answer(user_input):
    current_q = vragen_lijst[st.session_state.q_index]
    
    # Check antwoord (hoofdletterongevoelig)
    if user_input.strip().lower() == current_q['antwoord'].lower():
        st.success("Goedzo! 🎉")
        time.sleep(1) # Korte pauze voor effect
        
        # Volgende vraag of einde
        if st.session_state.q_index < len(vragen_lijst) - 1:
            st.session_state.q_index += 1
            st.rerun() # Herlaad de pagina voor de volgende vraag
        else:
            st.session_state.stage = 'end'
            st.rerun()
    else:
        st.error("Helaas, niet goed! Probeer het nog eens ❤️")

# -----------------------------------------------------------------------------
# 5. UI OPBOUW
# -----------------------------------------------------------------------------

# --- START SCHERM ---
if st.session_state.stage == 'start':
    st.title("Valentijns Quiz 💌")
    st.write("Ik heb 10 vragen over ons voorbereid in aanloop naar valentijnsdag.")
    st.write("Weet jij alles nog?")
    st.write("**Ik hoop het want er staat veel op het spel...**")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start de Quiz"):
            st.session_state.stage = 'quiz'
            st.rerun()

# --- QUIZ SCHERM ---
elif st.session_state.stage == 'quiz':
    q_data = vragen_lijst[st.session_state.q_index]
    
    # Progress bar
    progress = (st.session_state.q_index) / len(vragen_lijst)
    st.progress(progress)
    
    st.markdown(f"### Vraag {st.session_state.q_index + 1}")
    
    # Toon foto (met error handling als lokaal bestand mist)
    try:
        st.image(q_data['foto'], use_container_width=True)
    except:
        st.warning(f"Kan afbeelding '{q_data['foto']}' niet vinden. Zorg dat deze in de map staat.")

    st.markdown(f"**{q_data['vraag']}**")
    
    # Check of het meerkeuze is of open vraag
    if "keuzes" in q_data:
        # MEERKEUZE: We gebruiken knoppen voor een app-gevoel
        for keuze in q_data['keuzes']:
            if st.button(keuze):
                check_answer(keuze)
    else:
        # OPEN VRAAG
        # We gebruiken een formulier zodat enter werkt en input leegt bij refresh
        with st.form(key=f"form_{st.session_state.q_index}"):
            user_text = st.text_input("Jouw antwoord...", key="input_text")
            submit_btn = st.form_submit_button("Controleer")
            
            if submit_btn:
                check_answer(user_text)

# --- EIND SCHERM ---
elif st.session_state.stage == 'end':
    st.balloons() # Confetti effect!
    st.title("Lekker gewerkt! 💖")
    st.write("Je bent de allerleukste!")
    
    # Harten 10
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/English_pattern_10_of_hearts.svg/200px-English_pattern_10_of_hearts.svg.png", width=150)
    
    st.markdown("---")
    st.subheader("📸 Memory Lane")
    
    # Collage maken (4 kolommen breed)
    cols = st.columns(4)
    for i in range(10):
        with cols[i % 4]: # Verdeel over de 4 kolommen
            try:
                st.image(f"foto{i+1}.jpeg", use_container_width=True)
            except:
                pass # Sla over als foto mist

    st.markdown("---")
    
    # GIFJE
    st.markdown('<img src="https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
    
    st.markdown("### 🎁 Je Cadeau:")
    st.markdown("### 🥂 Een romantisch diner voor twee!")
    st.info("📅 13-02 - 18:00\n\n📍 Oudegracht aan de Werf 159k")