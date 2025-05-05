import streamlit as st
import random

st.set_page_config(page_title="Your Roommate Matches", layout="wide")
st.title("🎯 Your Roommate Matches")

# --- Session Check ---
if "user_preferences" not in st.session_state:
    st.warning("Please fill out the Roommate Match Form first.")
    st.stop()

prefs = st.session_state["user_preferences"]

st.markdown(f"""
Here are your top roommate matches based on the preferences you submitted, **{prefs['full_name']}**.
These suggestions aren’t identical to your profile, but are built to reflect your **budget, habits, and compatibility needs.**
""")

st.markdown("---")

# --- Matching Variations ---
def generate_variation(preference, category):
    variations = {
        "cleanliness": {
            "Messy": ["Average", "Messy"],
            "Average": ["Very Clean", "Average"],
            "Very Clean": ["Very Clean", "Average"]
        },
        "sleep_schedule": {
            "Early Riser": ["Early Riser", "Flexible"],
            "Night Owl": ["Night Owl", "Flexible"],
            "Flexible": ["Flexible", "Early Riser", "Night Owl"]
        },
        "social_level": {
            "Introverted": ["Introverted", "Moderate"],
            "Moderate": ["Introverted", "Extroverted", "Moderate"],
            "Extroverted": ["Extroverted", "Moderate"]
        },
        "noise_tolerance": {
            "Low": ["Low", "Medium"],
            "Medium": ["Low", "High"],
            "High": ["Medium", "High"]
        },
        "gender": {
            "Man": ["Man"],
            "Woman": ["Woman"],
            "Non-binary": ["Non-binary", "Woman", "Man"],
            "Prefer not to say": ["Man", "Woman", "Non-binary"]
        }
    }

    return random.choice(variations.get(category, {}).get(preference, [preference]))

# --- Generate Matches ---
def generate_matches(prefs):
    matches = []
    for i in range(5):
        match = {
            "age": random.randint(18, 25),
            "gender": generate_variation(prefs["gender"], "gender"),
            "budget": random.randint(prefs["budget"] - 100, prefs["budget"] + 100),
            "location": random.choice([
                prefs["location_pref"],
                "Downtown", "West End", "Old Salem", "Ardmore", "Cloverdale"
            ]),
            "cleanliness": generate_variation(prefs["cleanliness"], "cleanliness"),
            "sleep_schedule": generate_variation(prefs["sleep_schedule"], "sleep_schedule"),
            "social_level": generate_variation(prefs["social_level"], "social_level"),
            "noise_tolerance": generate_variation(prefs["noise_tolerance"], "noise_tolerance"),
            "study_habits": prefs["study_habits"],
            "smoking_ok": prefs["smoking_ok"],
            "pets_ok": prefs["pets_ok"],
            "guests_ok": prefs["guests_ok"],
            "shared_items": prefs["shared_items"],
            "hobbies": prefs["hobbies"] or "Not specified",
        }
        matches.append(match)
    return matches

# --- Display Matches ---
matches = generate_matches(prefs)

for idx, m in enumerate(matches):
    st.markdown(f"### 🧑 Match #{idx+1}")
    st.markdown(f"""
    - **Age**: {m['age']}
    - **Gender**: {m['gender']}
    - **Budget Range**: Around ${m['budget']} per month
    - **Preferred Location**: {m['location']}
    - **Cleanliness**: {m['cleanliness']}
    - **Sleep Schedule**: {m['sleep_schedule']}
    - **Social Comfort**: {m['social_level']}
    - **Noise Tolerance**: {m['noise_tolerance']}
    - **Study Habits**: {m['study_habits']}
    - **Open to Smoking Roommates**: {m['smoking_ok']}
    - **Okay with Pets**: {m['pets_ok']}
    - **Guest Policy**: {m['guests_ok']}
    - **Willing to Share Items**: {m['shared_items']}
    - **Shared Interests**: {m['hobbies']}
    """)
    
    with st.expander("💬 Contact Preview"):
        st.write(f"**Username:** match_user_{idx+1}")
        st.write("**Status:** Online now ✅")
        st.text_area("Send a message...", placeholder=f"Hey! I'm also looking to live around {m['location']} — want to connect?", key=f"msg_text_{idx}")
        st.button("📨 Send Message", key=f"msg_btn_{idx}")
    
    st.markdown("---")

# --- Action Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("🔁 Edit Preferences"):
        st.switch_page("pages/roommate_form.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")
