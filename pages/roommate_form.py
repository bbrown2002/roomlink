import streamlit as st

st.set_page_config(page_title="Roommate Match Form", layout="wide")

st.title("📝 Roommate Match Form")
st.markdown("Fill out the form below to help us find roommate matches that fit your lifestyle, preferences, and personality.")

st.markdown("---")

with st.form("match_form"):
    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        age = st.slider("Your Age", 18, 30, 20)
        gender = st.selectbox("Your Gender", ["Woman", "Man", "Non-binary", "Prefer not to say"])
        school_email = st.text_input("School Email (.edu)")
        major = st.text_input("Your Major")
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
        study_habits = st.selectbox("Study Habits", ["Quiet room", "Library", "With music", "Late-night"])
    
    st.markdown("### Lifestyle Preferences")
    lifestyle_col1, lifestyle_col2 = st.columns(2)

    with lifestyle_col1:
        smoking_ok = st.radio("Are you okay living with someone who smokes?", ["Yes", "No"])
        pets_ok = st.radio("Are you okay living with pets?", ["Yes", "No"])

    with lifestyle_col2:
        guests_ok = st.radio("Are you okay with overnight guests?", ["Never", "Sometimes", "Often"])
        shared_items = st.radio("Willing to share items (kitchen, groceries, etc.)?", ["Yes", "Some", "No"])

    st.markdown("### Hobbies & Personal Statement")
    hobbies = st.text_input("Your Hobbies (comma separated)", placeholder="Ex: Gaming, Gym, Reading")
    bio = st.text_area("Tell us about your personality, lifestyle, and what kind of roommate you're looking for.")

    submitted = st.form_submit_button("Submit and See Matches")

    if submitted:
        st.success("Form submitted successfully! Generating your matches...")

        # Save to session state for match_results.py
        st.session_state["user_preferences"] = {
            "full_name": full_name,
            "age": age,
            "gender": gender,
            "school_email": school_email,
            "major": major,
            "budget": budget,
            "location_pref": location_pref,
            "cleanliness": cleanliness,
            "sleep_schedule": sleep_schedule,
            "social_level": social_level,
            "noise_tolerance": noise_tolerance,
            "study_habits": study_habits,
            "smoking_ok": smoking_ok,
            "pets_ok": pets_ok,
            "guests_ok": guests_ok,
            "shared_items": shared_items,
            "hobbies": hobbies,
            "bio": bio
        }

        st.markdown("👉 [Click here to view your roommate matches](match_results.py)")
