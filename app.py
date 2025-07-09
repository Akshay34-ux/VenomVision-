import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- Helper function to load Lottie animation ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_snake = load_lottieurl("https://lottie.host/0599ba1e-e199-4e40-9611-cdbac3946bcb/wHFLjnnckd.json")

# --- Custom CSS ---
st.markdown("""
    <style>
        .center-text {
            text-align: center;
        }
        .hero-section {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .dark .hero-section {
            background-color: #1f1f1f;
            color: white;
        }
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Dark Mode Toggle ---
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

if st.sidebar.button("🌙 Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode

if st.session_state.dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #121212;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.markdown("<p class='sidebar-title'>🧭 Navigation</p>", unsafe_allow_html=True)
page = st.sidebar.selectbox("", ["Home", "Snake Knowledge Hub", "Myth Buster"])

# --- HOME PAGE ---
if page == "Home":
    st.markdown('<div class="center-text"><h1>🐍 VenomVision</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="center-text"><h4>Identify. Learn. Stay Safe.</h4></div>', unsafe_allow_html=True)

    if lottie_snake:
        st_lottie(lottie_snake, height=250, key="snake_lottie")

    st.markdown("""
        <div class='hero-section'>
            <h3>🌟 What Can You Do with VenomVision?</h3>
            <ul>
                <li>📸 Identify snakes based on traits and behavior</li>
                <li>📚 Learn facts and bust common snake myths</li>
                <li>🚑 Access emergency first-aid info for snake bites</li>
                <li>🌙 Use Dark Mode for night-time reading comfort</li>
            </ul>
            <p><strong>➡️ Use the sidebar to get started!</strong></p>
        </div>
    """, unsafe_allow_html=True)

# --- KNOWLEDGE HUB ---
elif page == "Snake Knowledge Hub":
    st.title("🐍 Snake Knowledge Hub")

    snakes = {
        "Indian Cobra": "A venomous snake found across India. It has a distinctive hood and delivers neurotoxic venom.",
        "Russell's Viper": "Highly venomous. Known for its loud hiss and responsible for many bites in rural India.",
        "Saw-scaled Viper": "Small but aggressive. Fast striking and delivers hemotoxic venom.",
        "Common Krait": "Nocturnal and highly venomous. Its bite is painless but deadly.",
        "Green Vine Snake": "Mildly venomous and slender with bright green color.",
        "Reticulated Python": "Non-venomous. One of the longest snakes in the world.",
        "King Cobra": "The world’s longest venomous snake. Feeds mainly on other snakes.",
        "Banded Krait": "Venomous and brightly patterned with black and yellow bands.",
        "Checkered Keelback": "Non-venomous and semi-aquatic, commonly found near water bodies.",
        "Indian Rock Python": "A massive non-venomous constrictor found in rocky and forested areas."
    }

    choice = st.selectbox("Select a snake to learn more:", list(snakes.keys()))
    st.info(snakes[choice])

# --- MYTH BUSTER ---
elif page == "Myth Buster":
    st.title("🧠 Snake Myths & Facts")

    myths_facts = [
        ("All snakes are venomous.", "❌ False: Only a small percentage of snakes are venomous."),
        ("Snakes chase humans.", "❌ False: Snakes prefer to escape and only strike when threatened."),
        ("Baby snakes are more dangerous than adults.", "⚠️ Partially true: They may inject venom randomly but have less venom overall."),
        ("Snakes drink milk.", "❌ False: Snakes drink water. The milk-drinking myth is a misconception."),
        ("Snakes hypnotize their prey.", "❌ False: Prey may freeze in fear, but snakes don’t hypnotize."),
        ("Snakes have ears and can hear.", "⚠️ Partially true: They don’t have external ears but sense vibrations."),
        ("Cutting a snake’s head ensures safety.", "❌ False: A severed snake head can still deliver venomous bites."),
        ("All snakes lay eggs.", "❌ False: Some snakes like boas and vipers give live birth."),
        ("Snakes are slimy.", "❌ False: Snakes have dry, scaly skin."),
        ("Snakes only live in forests.", "❌ False: They can be found in cities, farms, deserts, and water.")
    ]

    for myth, fact in myths_facts:
        st.markdown(f"**🌀 Myth:** {myth}")
        st.markdown(f"**✅ Fact:** {fact}")
        st.markdown("---")
