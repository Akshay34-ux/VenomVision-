import streamlit as st
import time

# ------------------- CSS for Dark Mode Toggle -------------------
dark_mode_toggle = """
    <style>
        body {
            transition: background-color 0.3s ease;
        }
        .dark-mode {
            background-color: #0e1117;
            color: #ffffff;
        }
        .light-mode {
            background-color: #ffffff;
            color: #000000;
        }
    </style>
    <script>
        function toggleMode() {
            var body = document.body;
            if (body.classList.contains('dark-mode')) {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
            } else {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
            }
        }
    </script>
    <button onclick="toggleMode()" style="position:fixed;top:10px;right:10px;z-index:1000;">🌙 Toggle Dark Mode</button>
"""
st.markdown(dark_mode_toggle, unsafe_allow_html=True)

# ------------------- Title & Menu -------------------
st.title("🐍 VenomVision: Snake Identification & Awareness")

menu = st.sidebar.selectbox("Navigate", ["Home", "Identify Snake", "Snake Knowledge Hub", "Myths & Facts"])

# ------------------- Home Page -------------------
if menu == "Home":
    st.subheader("Welcome to VenomVision!")
    st.write("""
    VenomVision is your intelligent assistant for identifying snakes and spreading awareness about them.
    
    🧠 Built with AI, this app helps:
    - Identify snake species
    - Learn about venomous and non-venomous snakes
    - Bust common myths that put lives at risk
    - Understand first-aid protocols and facts

    > *"Snakes are not aggressive; they are just misunderstood."*

    👉 Use the sidebar to get started!
    """)

# ------------------- Identify Snake (placeholder) -------------------
elif menu == "Identify Snake":
    st.subheader("🔍 Identify a Snake")
    uploaded_file = st.file_uploader("Upload a snake image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Analyzing..."):
            time.sleep(3)  # Simulate processing time
        st.success("This looks like a **Spectacled Cobra** (Naja naja)")
        st.info("☠️ Venomous\n\nIf bitten, seek medical help immediately. Do not suck venom or cut the wound.")

# ------------------- Knowledge Hub -------------------
elif menu == "Snake Knowledge Hub":
    st.subheader("📚 Snake Knowledge Hub")
    
    snakes = {
        "Indian Cobra": {
            "Scientific Name": "Naja naja",
            "Venomous": "Yes",
            "Info": "Found all over India. Famous for its hood and spectacles mark."
        },
        "Russell's Viper": {
            "Scientific Name": "Daboia russelii",
            "Venomous": "Yes",
            "Info": "One of the Big Four in India. Very dangerous."
        },
        "Common Krait": {
            "Scientific Name": "Bungarus caeruleus",
            "Venomous": "Yes",
            "Info": "Nocturnal and highly venomous. Appears black or dark blue with white bands."
        },
        "Rat Snake": {
            "Scientific Name": "Ptyas mucosa",
            "Venomous": "No",
            "Info": "Non-venomous and helpful in controlling rodents."
        }
    }

    selected = st.selectbox("Select a snake to learn more", list(snakes.keys()))
    details = snakes[selected]
    st.write(f"**Scientific Name**: {details['Scientific Name']}")
    st.write(f"**Venomous**: {details['Venomous']}")
    st.write(f"**Info**: {details['Info']}")

# ------------------- Myths & Facts -------------------
elif menu == "Myths & Facts":
    st.subheader("🧠 Myths & Facts About Snakes")

    myths_facts = {
        "All snakes are venomous.": "❌ Myth\n\n✅ Fact: Only about 15% of all snakes are venomous.",
        "Snakes chase humans.": "❌ Myth\n\n✅ Fact: Snakes usually try to flee. They bite only when threatened.",
        "Sucking out venom helps.": "❌ Myth\n\n✅ Fact: This can worsen the wound. Always seek medical help.",
        "Snakes drink milk.": "❌ Myth\n\n✅ Fact: Snakes do not drink milk naturally; they may do so when dehydrated.",
        "Dead snakes can't bite.": "❌ Myth\n\n✅ Fact: Reflex action in dead snakes can still cause bites."
    }

    for myth, fact in myths_facts.items():
        with st.expander(myth):
            st.write(fact)
