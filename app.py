import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- Load Lottie animation ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load snake animation
lottie_snake = load_lottieurl("https://lottie.host/0599ba1e-e199-4e40-9611-cdbac3946bcb/wHFLjnnckd.json")

# --- Dark Mode Toggle ---
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

if st.sidebar.button("🌙 Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode

# Apply dark mode styles
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .st-bw {
            background-color: #2b2b2b;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("Navigate", ["Home", "Snake Knowledge Hub", "Myth Buster"])

# --- HOME PAGE ---
if page == "Home":
    st.title("🐍 VenomVision")
    st.subheader("Discover the world of snakes — Identify, Learn, and Stay Safe")

    if lottie_snake:
        st_lottie(lottie_snake, height=300, key="snake")

    st.markdown("""
        Welcome to **VenomVision**, your one-stop app to:

        - 🧠 **Learn about various snakes** and their traits  
        - ❓ **Bust common snake myths**  
        - 🚑 **Access first-aid tips** in case of a bite  

        👉 Start by selecting a section from the **left sidebar**.
    """)

# --- SNAKE KNOWLEDGE HUB ---
elif page == "Snake Knowledge Hub":
    st.title("🐍 Snake Knowledge Hub")

    snakes = {
        "Indian Cobra": "Venomous. Known for its hood and neurotoxic venom.",
        "Russell's Viper": "Highly venomous. Loud hiss and hemotoxic venom.",
        "Saw-scaled Viper": "Aggressive. Fast striker with hemotoxic venom.",
        "Common Krait": "Painless but deadly neurotoxic bite. Nocturnal.",
        "Green Vine Snake": "Mildly venomous. Slender and bright green.",
        "Reticulated Python": "Non-venomous. Longest snake. Constrictor.",
        "King Cobra": "World’s longest venomous snake. Eats other snakes.",
        "Banded Krait": "Brightly banded. Neurotoxic venom. Shy in nature.",
        "Indian Rock Python": "Non-venomous. Large constrictor. Slow moving.",
        "Checkered Keelback": "Non-venomous. Common water snake."
    }

    choice = st.selectbox("Select a snake to learn more:", list(snakes.keys()))
    st.info(snakes[choice])

# --- MYTH BUSTER ---
elif page == "Myth Buster":
    st.title("🧠 Snake Myths & Facts")

    myths_facts = [
        ("All snakes are venomous.", "❌ False: Only a small percentage are venomous."),
        ("Snakes chase humans.", "❌ False: They avoid conflict and escape if possible."),
        ("Snakes drink milk.", "❌ False: Snakes don’t naturally drink milk."),
        ("Poison and venom are the same.", "❌ False: Poison is ingested; venom is injected."),
        ("Baby snakes are more dangerous.", "❌ False: Venom quantity is less and varies by species."),
        ("Snakes hypnotize prey.", "❌ False: They rely on stealth and speed."),
        ("Snakes remember people.", "❌ False: Snakes don’t have that kind of memory."),
        ("Snakes always live in forests.", "❌ False: Many live in farms, wetlands, cities."),
    ]

    for myth, fact in myths_facts:
        st.markdown(f"**Myth:** {myth}<br>**Fact:** {fact}", unsafe_allow_html=True)
        st.markdown("---")
