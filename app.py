import streamlit as st
import pandas as pd
import random
import os

# --- Page Config ---
st.set_page_config(page_title="RoomLink | All-in-One", layout="wide")

# --- Header ---
st.title("🏠 RoomLink | Student Housing & Roommate Finder")
st.markdown("Safe, smart, and social housing for Winston-Salem students.")
st.markdown("---")

# --- Step 1: Housing Form ---
st.subheader("📬 Submit a Room or Property")

with st.form("room_form"):
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Neighborhood", ["Ardmore", "Cloverdale", "West End", "Downtown", "Old Salem", "Reynolda Village", "Washington Park", "University Parkway"])
        price = st.number_input("Monthly Rent ($)", 300, 2000, step=25)
        lease_type = st.selectbox("Lease Type", ["Month-to-month", "6 months", "9 months", "12 months", "Flexible"])
    with col2:
        pets = st.radio("Pets Allowed?", ["Yes", "No"])
        smoke = st.radio("Smoking Allowed?", ["Yes", "No"])
        guests = st.radio("Guests Allowed?", ["Yes", "No"])
        utilities = st.radio("Utilities Included?", ["Yes", "No"])
    desc = st.text_area("Room Description", height=150)
    submit_room = st.form_submit_button("Save Room Info")

if submit_room:
    rules = []
    if pets == "No": rules.append("No pets")
    else: rules.append("Pets allowed")
    if smoke == "No": rules.append("No smoking")
    else: rules.append("Smoking allowed")
    if guests == "No": rules.append("No guests")
    else: rules.append("Guest friendly")
    if utilities == "Yes": rules.append("Utilities included")

    st.session_state["room_data"] = {
        "price": f"${int(price)}",
        "location": location,
        "lease": lease_type,
        "rules": ", ".join(rules),
        "desc": desc or "No description"
    }
    st.success("Room saved!")

# --- Step 2: Roommate Preferences Form ---
if "room_data" in st.session_state:
    st.markdown("---")
    st.subheader("📝 Roommate Match Form")

    with st.form("roommate_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            age = st.slider("Age", 18, 30)
            gender = st.selectbox("Gender", ["Woman", "Man", "Non-binary", "Prefer not to say"])
            email = st.text_input("School Email")
            major = st.text_input("Major")
            budget = st.number_input("Max Rent Willing to Pay", 300, 1500, step=25)
        with col2:
            location_pref = st.selectbox("Preferred Neighborhood", ["Ardmore", "Downtown", "West End", "Old Salem", "Peters Creek", "Cloverdale", "Washington Park", "Reynolda Village", "University Parkway"])
            clean = st.selectbox("Cleanliness Level", ["Messy", "Average", "Very Clean"])
            sleep = st.selectbox("Sleep Schedule", ["Early Riser", "Night Owl", "Flexible"])
            social = st.selectbox("Social Comfort", ["Introverted", "Moderate", "Extroverted"])
            noise = st.selectbox("Noise Tolerance", ["Low", "Medium", "High"])
            study = st.selectbox("Study Habits", ["Quiet room", "Library", "With music", "Late-night"])
        lifestyle1, lifestyle2 = st.columns(2)
        with lifestyle1:
            smoking_ok = st.radio("OK with Smoking Roommates?", ["Yes", "No"])
            pets_ok = st.radio("OK with Pets?", ["Yes", "No"])
        with lifestyle2:
            guests_ok = st.radio("OK with Guests?", ["Never", "Sometimes", "Often"])
            shared_items = st.radio("Share Items (kitchen, etc)?", ["Yes", "Some", "No"])
        hobbies = st.text_input("Hobbies", placeholder="Gaming, Gym, Reading")
        bio = st.text_area("Your Bio")

        submit_roommate = st.form_submit_button("Find Matches")

    if submit_roommate:
        st.session_state["roommate_prefs"] = {
            "full_name": name, "age": age, "gender": gender, "school_email": email,
            "major": major, "budget": budget, "location_pref": location_pref,
            "cleanliness": clean, "sleep_schedule": sleep, "social_level": social,
            "noise_tolerance": noise, "study_habits": study, "smoking_ok": smoking_ok,
            "pets_ok": pets_ok, "guests_ok": guests_ok, "shared_items": shared_items,
            "hobbies": hobbies, "bio": bio
        }
        st.success("Preferences submitted!")

# --- Step 3: Show Match Results ---
if "roommate_prefs" in st.session_state:
    st.markdown("---")
    st.subheader("🎯 Your Roommate Matches")

    prefs = st.session_state["roommate_prefs"]

    def variation(preference, category):
        options = {
            "cleanliness": {"Messy": ["Average", "Messy"], "Average": ["Very Clean", "Average"], "Very Clean": ["Very Clean", "Average"]},
            "sleep_schedule": {"Early Riser": ["Early Riser", "Flexible"], "Night Owl": ["Night Owl", "Flexible"], "Flexible": ["Flexible", "Early Riser", "Night Owl"]},
            "social_level": {"Introverted": ["Introverted", "Moderate"], "Moderate": ["Introverted", "Extroverted", "Moderate"], "Extroverted": ["Extroverted", "Moderate"]},
            "noise_tolerance": {"Low": ["Low", "Medium"], "Medium": ["Low", "High"], "High": ["Medium", "High"]},
            "gender": {"Man": ["Man"], "Woman": ["Woman"], "Non-binary": ["Non-binary", "Woman", "Man"], "Prefer not to say": ["Man", "Woman", "Non-binary"]}
        }
        return random.choice(options.get(category, {}).get(preference, [preference]))

    for i in range(5):
        match = {
            "age": random.randint(18, 25),
            "gender": variation(prefs["gender"], "gender"),
            "budget": random.randint(prefs["budget"] - 100, prefs["budget"] + 100),
            "location": random.choice([prefs["location_pref"], "Downtown", "West End", "Old Salem", "Ardmore", "Cloverdale"]),
            "cleanliness": variation(prefs["cleanliness"], "cleanliness"),
            "sleep_schedule": variation(prefs["sleep_schedule"], "sleep_schedule"),
            "social_level": variation(prefs["social_level"], "social_level"),
            "noise_tolerance": variation(prefs["noise_tolerance"], "noise_tolerance"),
            "study_habits": prefs["study_habits"],
            "smoking_ok": prefs["smoking_ok"],
            "pets_ok": prefs["pets_ok"],
            "guests_ok": prefs["guests_ok"],
            "shared_items": prefs["shared_items"],
            "hobbies": prefs["hobbies"]
        }

        st.markdown(f"### 👤 Match #{i+1}")
        st.markdown(f"""
        - **Age**: {match['age']}
        - **Gender**: {match['gender']}
        - **Budget Range**: ~${match['budget']}
        - **Location**: {match['location']}
        - **Cleanliness**: {match['cleanliness']}
        - **Sleep Schedule**: {match['sleep_schedule']}
        - **Social**: {match['social_level']}
        - **Noise Tolerance**: {match['noise_tolerance']}
        - **Study Habits**: {match['study_habits']}
        - **Smoking OK**: {match['smoking_ok']}
        - **Pets OK**: {match['pets_ok']}
        - **Guests OK**: {match['guests_ok']}
        - **Shares Items?**: {match['shared_items']}
        - **Hobbies**: {match['hobbies']}
        """)
        st.markdown("---")
