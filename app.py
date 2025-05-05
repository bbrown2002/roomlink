import streamlit as st
import pandas as pd
import os
import random

# --- Page Config ---
st.set_page_config(page_title="RoomLink | All-In-One", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS ---
st.markdown("""
    <style>
    .roomlink-header {
        font-size: 42px;
        font-weight: 800;
        color: #B31B1B;
        letter-spacing: -1px;
        margin-bottom: 0;
    }
    .roomlink-sub {
        font-size: 20px;
        color: #444;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="roomlink-header">RoomLink</p>', unsafe_allow_html=True)
st.markdown('<p class="roomlink-sub">All-in-One: Submit, Match, and View</p>', unsafe_allow_html=True)
st.markdown("---")

# --- Room Form ---
st.subheader("📬 Submit a Room or Property")
with st.form("room_form"):
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Neighborhood or Area", [
            "Ardmore", "Cloverdale", "West End", "Downtown", "Old Salem",
            "Reynolda Village", "Washington Park", "University Parkway"
        ])
        price = st.number_input("Monthly Rent ($)", min_value=300, max_value=2000, step=25)
        lease_type = st.selectbox("Lease Type", ["Month-to-month", "6 months", "9 months", "12 months", "Flexible"])
    with col2:
        pets_allowed = st.radio("Pets Allowed?", ["Yes", "No"])
        smoking_policy = st.radio("Smoking Allowed?", ["Yes", "No"])
        guest_policy = st.radio("Guests Allowed?", ["Yes", "No"])
        utilities_included = st.radio("Utilities Included?", ["Yes", "No"])
    description = st.text_area("Write a short description about the room", height=150)
    room_submitted = st.form_submit_button("Submit Room Listing")

# --- Save Room Listing to Session State ---
if room_submitted:
    rules = []
    if pets_allowed == "No": rules.append("No pets")
    else: rules.append("Pets allowed")
    if smoking_policy == "No": rules.append("No smoking")
    else: rules.append("Smoking allowed")
    if guest_policy == "No": rules.append("No guests")
    else: rules.append("Guest friendly")
    if utilities_included == "Yes": rules.append("Utilities included")
    rules_str = ", ".join(rules)

    st.session_state["room_data"] = {
        "price": f"${int(price)}",
        "location": location,
        "lease": lease_type,
        "rules": rules_str,
        "desc": description or "No description provided."
    }
    st.success("✅ Room listing saved! You can now fill out roommate match preferences.")

# --- Roommate Match Form ---
st.subheader("📝 Roommate Match Form")
if "room_data" in st.session_state:
    with st.form("match_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name")
            age = st.slider("Your Age", 18, 30, 20)
            gender = st.selectbox("Your Gender", ["Woman", "Man", "Non-binary", "Prefer not to say"])
            budget = st.number_input("Max Rent Willing to Pay ($)", min_value=300, max_value=1500, step=25)
        with col2:
            location_pref = st.selectbox("Preferred Neighborhood", [
                "Ardmore", "Downtown", "West End", "Old Salem", "Peters Creek",
                "Cloverdale", "Washington Park", "Reynolda Village", "University Parkway"
            ])
            cleanliness = st.selectbox("Cleanliness Level", ["Messy", "Average", "Very Clean"])
            sleep_schedule = st.selectbox("Sleep Schedule", ["Early Riser", "Night Owl", "Flexible"])
        social_level = st.selectbox("Social Comfort", ["Introverted", "Moderate", "Extroverted"])
        noise_tolerance = st.selectbox("Noise Tolerance", ["Low", "Medium", "High"])
        smoking_ok = st.radio("Okay with Smoking?", ["Yes", "No"])
        pets_ok = st.radio("Okay with Pets?", ["Yes", "No"])
        guests_ok = st.radio("Guest Policy?", ["Never", "Sometimes", "Often"])
        shared_items = st.radio("Willing to Share Items?", ["Yes", "Some", "No"])
        hobbies = st.text_input("Hobbies", placeholder="e.g., Gym, Gaming")
        match_submit = st.form_submit_button("See Matches")

    # --- Display Matches ---
    if match_submit:
        def generate_variation(preference, category):
            variations = {
                "cleanliness": {"Messy": ["Average", "Messy"], "Average": ["Very Clean", "Average"], "Very Clean": ["Very Clean", "Average"]},
                "sleep_schedule": {"Early Riser": ["Early Riser", "Flexible"], "Night Owl": ["Night Owl", "Flexible"], "Flexible": ["Flexible", "Early Riser", "Night Owl"]},
                "social_level": {"Introverted": ["Introverted", "Moderate"], "Moderate": ["Introverted", "Extroverted", "Moderate"], "Extroverted": ["Extroverted", "Moderate"]},
                "noise_tolerance": {"Low": ["Low", "Medium"], "Medium": ["Low", "High"], "High": ["Medium", "High"]},
                "gender": {"Man": ["Man"], "Woman": ["Woman"], "Non-binary": ["Non-binary", "Woman", "Man"], "Prefer not to say": ["Man", "Woman", "Non-binary"]}
            }
            return random.choice(variations.get(category, {}).get(preference, [preference]))

        prefs = {
            "full_name": full_name, "age": age, "gender": gender, "budget": budget, "location_pref": location_pref,
            "cleanliness": cleanliness, "sleep_schedule": sleep_schedule, "social_level": social_level,
            "noise_tolerance": noise_tolerance, "smoking_ok": smoking_ok, "pets_ok": pets_ok,
            "guests_ok": guests_ok, "shared_items": shared_items, "hobbies": hobbies or "Not specified"
        }

        st.subheader("🎯 Your Roommate Matches")
        for idx in range(3):
            m = {
                "age": random.randint(18, 25),
                "gender": generate_variation(prefs["gender"], "gender"),
                "budget": random.randint(prefs["budget"] - 100, prefs["budget"] + 100),
                "location": random.choice([prefs["location_pref"], "Downtown", "West End", "Old Salem", "Ardmore", "Cloverdale"]),
                "cleanliness": generate_variation(prefs["cleanliness"], "cleanliness"),
                "sleep_schedule": generate_variation(prefs["sleep_schedule"], "sleep_schedule"),
                "social_level": generate_variation(prefs["social_level"], "social_level"),
                "noise_tolerance": generate_variation(prefs["noise_tolerance"], "noise_tolerance"),
                "study_habits": "Quiet room", "smoking_ok": prefs["smoking_ok"], "pets_ok": prefs["pets_ok"],
                "guests_ok": prefs["guests_ok"], "shared_items": prefs["shared_items"], "hobbies": prefs["hobbies"]
            }
            st.markdown(f"### 🧑 Match #{idx+1}")
            st.markdown(f"""
            - **Age**: {m['age']}
            - **Gender**: {m['gender']}
            - **Budget**: ${m['budget']}/mo
            - **Location**: {m['location']}
            - **Cleanliness**: {m['cleanliness']}
            - **Sleep Schedule**: {m['sleep_schedule']}
            - **Social Level**: {m['social_level']}
            - **Noise Tolerance**: {m['noise_tolerance']}
            - **Smoking OK**: {m['smoking_ok']}
            - **Pets OK**: {m['pets_ok']}
            - **Guests OK**: {m['guests_ok']}
            - **Shared Items**: {m['shared_items']}
            - **Interests**: {m['hobbies']}
            """)
            st.markdown("---")
else:
    st.info("⚠️ Please submit your room listing above to unlock the match form.")
