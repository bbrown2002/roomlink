import streamlit as st
import random

st.set_page_config(page_title="Available Housing Listings", layout="wide")
st.title("🏡 Available Housing Listings")
st.markdown("Explore current off-campus housing options submitted by students and verified listers. Listings include location, rent, amenities, and rules.")

st.markdown("---")

# Sample data pool
locations = [
    "Ardmore", "Cloverdale", "West End", "Downtown", "Old Salem",
    "Reynolda Village", "Washington Park", "University Parkway"
]
lease_types = ["Month-to-month", "6-month lease", "1-year lease"]
rules = ["No Smoking", "Pet Friendly", "No Pets", "Utilities Included", "Furnished", "Student Only"]
descriptions = [
    "Quiet two-bedroom with private bathroom, 10 min from campus.",
    "Modern apartment with laundry and gym access, roommate needed.",
    "Studio in downtown loft with walkable access to cafes and bus.",
    "Townhouse with 3 rooms, large kitchen, pets negotiable.",
    "Private room in shared house. Quiet neighborhood. No smoking."
]

# Function to build a listing
def generate_listing():
    return {
        "price": f"${random.randint(500, 900)}/mo",
        "location": random.choice(locations),
        "lease": random.choice(lease_types),
        "rules": ", ".join(random.sample(rules, k=2)),
        "desc": random.choice(descriptions)
    }

# Generate 10 listings
listings = [generate_listing() for _ in range(10)]

# Display in rows
for i, l in enumerate(listings):
    st.markdown(f"### 🏠 Listing #{i+1}")
    col1, col2 = st.columns([1.5, 2.5])
    
    with col1:
        st.markdown(f"**Price**: {l['price']}")
        st.markdown(f"**Location**: {l['location']}")
        st.markdown(f"**Lease Type**: {l['lease']}")
        st.markdown(f"**Rules & Amenities**: {l['rules']}")
    
    with col2:
        st.markdown(f"📌 _{l['desc']}_")

    st.markdown("---")
