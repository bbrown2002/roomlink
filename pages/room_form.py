import streamlit as st
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(page_title="Submit Housing Listing", layout="wide")
st.title("📬 Submit a Room or Property")

st.markdown("""
Use this form to list an available room, apartment, or housing unit for students in the Winston-Salem area.
Make sure all details are accurate — listings will be publicly shown on the Housing Listings page.
""")

st.markdown("---")

# --- Form ---
with st.form("room_listing_form"):
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

    st.markdown("### 📝 Description & Notes")
    description = st.text_area("Write a short description about the room, amenities, or rules", height=150)

    submitted = st.form_submit_button("Submit Listing")

# --- Submission Logic ---
if submitted:
    # Construct the 'rules' string
    rules = []
    if pets_allowed == "No":
        rules.append("No pets")
    elif pets_allowed == "Yes":
        rules.append("Pets allowed")

    if smoking_policy == "No":
        rules.append("No smoking")
    elif smoking_policy == "Yes":
        rules.append("Smoking allowed")

    if guest_policy == "No":
        rules.append("No guests")
    elif guest_policy == "Yes":
        rules.append("Guest friendly")

    if utilities_included == "Yes":
        rules.append("Utilities included")

    rules_str = ", ".join(rules)

    # Create listing
    listing = {
        "price": f"${int(price)}",
        "location": location,
        "lease": lease_type,
        "rules": rules_str,
        "desc": description or "No description provided."
    }

    # Save to CSV
    csv_path = "housing_listings.csv"
    df = pd.DataFrame([listing])

    try:
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode="a", header=False, index=False)
        else:
            df.to_csv(csv_path, index=False)
    except Exception as e:
        st.error(f"Failed to save listing: {e}")
        st.stop()

    # Mark form as complete and redirect
    st.session_state["room_form_completed"] = True
    st.success("✅ Listing submitted! Redirecting you to the Roommate Form...")
    st.rerun()  # Ensure session is saved before switching
    st.switch_page("pages/roommate_form.py")
