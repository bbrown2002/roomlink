import streamlit as st

st.set_page_config(page_title="Submit Housing Listing", layout="wide")
st.title("📬 Submit a Room or Property")

st.markdown("""
Use this form to list an available room, apartment, or housing unit for students in the Winston-Salem area.
Make sure all details are accurate — listings will be publicly shown on the Housing Listings page.
""")

st.markdown("---")

with st.form("room_listing_form"):
    col1, col2 = st.columns(2)

    with col1:
        lister_name = st.text_input("Your Name")
        contact_email = st.text_input("Contact Email")
        location = st.selectbox("Neighborhood or Area", [
            "Ardmore", "Cloverdale", "West End", "Downtown", "Old Salem",
            "Reynolda Village", "Washington Park", "University Parkway"
        ])
        price = st.number_input("Monthly Rent ($)", min_value=300, max_value=2000, step=25)
        lease_type = st.selectbox("Lease Type", ["Month-to-month", "6 months", "12 months", "Flexible"])

    with col2:
        room_type = st.selectbox("Room Type", ["Private Room", "Shared Room", "Studio", "Entire Apartment"])
        furnished = st.radio("Is the unit furnished?", ["Yes", "No"])
        pets_allowed = st.radio("Pets Allowed?", ["Yes", "No"])
        smoking_policy = st.radio("Smoking Allowed?", ["Yes", "No"])
        utilities_included = st.radio("Utilities Included in Rent?", ["Yes", "No"])

    st.markdown("### 📝 Description & Notes")
    description = st.text_area("Write a short description about the room, amenities, or rules", height=150)

    submitted = st.form_submit_button("Submit Listing")

    if submitted:
        st.success("✅ Listing submitted! Your room will appear on the Housing Listings page after review.")
        st.balloons()

        # Save submission (later you can store this in a CSV or database)
import pandas as pd
import os

# Create dictionary from form fields
listing = {
    "Lister Name": lister_name,
    "Email": contact_email,
    "Location": location,
    "Rent": price,
    "Lease Type": lease_type,
    "Room Type": room_type,
    "Furnished": furnished,
    "Pets Allowed": pets_allowed,
    "Smoking Policy": smoking_policy,
    "Utilities Included": utilities_included,
    "Description": description
}

# Save to CSV
csv_path = "data/housing_listings.csv"
df = pd.DataFrame([listing])

if os.path.exists(csv_path):
    df.to_csv(csv_path, mode="a", index=False, header=False)
else:
    df.to_csv(csv_path, index=False)


        st.markdown("---")
        st.subheader("📄 Summary of Your Listing:")
        st.markdown(f"- **Lister Name**: {lister_name}")
        st.markdown(f"- **Contact**: {contact_email}")
        st.markdown(f"- **Location**: {location}")
        st.markdown(f"- **Price**: ${price}/mo")
        st.markdown(f"- **Lease Type**: {lease_type}")
        st.markdown(f"- **Room Type**: {room_type}")
        st.markdown(f"- **Furnished**: {furnished}")
        st.markdown(f"- **Pets Allowed**: {pets_allowed}")
        st.markdown(f"- **Smoking Policy**: {smoking_policy}")
        st.markdown(f"- **Utilities Included**: {utilities_included}")
        st.markdown(f"- **Description**: {description or 'None'}")
