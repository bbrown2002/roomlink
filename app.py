import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="RoomLink | Off-Campus Student Housing",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    .section-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="roomlink-header">RoomLink</p>', unsafe_allow_html=True)
st.markdown('<p class="roomlink-sub">Student Housing Made Safe, Smart, and Social</p>', unsafe_allow_html=True)
st.markdown("---")

# --- Main Hero Section ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🏠 Welcome to RoomLink")
    st.markdown("""
    **RoomLink** is a web-based off-campus housing resource designed specifically for college students in Winston-Salem. Whether you're new to the city or looking to upgrade your living situation, RoomLink is your go-to tool for safe, verified listings and community-driven housing options.

    🔒 Verified through school communities  
    🛏️ Filtered by lifestyle and rent preferences  
    💬 Built for students, by students
    """)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=870&q=80",
        caption="Off-campus living, simplified",
        use_column_width=True
    )

st.markdown("---")

# --- Stats Tiles ---
col1, col2, col3 = st.columns(3)
col1.metric("Roommates Available", "50+")
col2.metric("Housing Listings", "12 Active")
col3.metric("Local Neighborhoods", "9 Areas")

# --- How It Works ---
st.subheader("📚 How It Works")
st.markdown("""
RoomLink connects students with verified off-campus housing options in Winston-Salem. It streamlines the entire process through:

1. **Housing Listings**  
   View submitted listings from students and local property owners. Filter by location, rent range, lease length, and housing rules like pets or smoking.

2. **School-Affiliated Access**  
   Access is limited to verified students to keep listings clean, honest, and useful.

More features are being built to support profile verification, communication tools, and neighborhood safety insights.
""")

# --- Testimonials ---
st.subheader("💬 What Students Are Saying")

col1, col2 = st.columns(2)

with col1:
    st.markdown("> “No more Facebook guesswork. I finally found a clean place close to campus.” — *Maya T.*")

with col2:
    st.markdown("> “I posted my room, and it got 3 hits in the first week. Way easier than Craigslist.” — *Jaylen B.*")

# --- Trust Section ---
st.subheader("🔐 Built on Trust")
st.markdown("""
RoomLink exists to make student housing safer and smarter:

✅ Students confirm university affiliation  
✅ Listings require verified submissions  
✅ Lifestyle preferences and lease details are upfront

We're keeping it local and curated for real students—not just randoms with keys.
""")

# ===========================
# --- ROOM FORM SECTION ---
st.subheader("📬 Submit a Room or Property")

st.markdown("""
Use this section to list an available room, apartment, or housing unit for students in the Winston-Salem area.
Details will be used to filter and generate roommate match context.
""")

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

# --- Build "rules" string on the fly ---
rules = []
if pets_allowed == "Yes":
    rules.append("Pets allowed")
else:
    rules.append("No pets")

if smoking_policy == "Yes":
    rules.append("Smoking allowed")
else:
    rules.append("No smoking")

if guest_policy == "Yes":
    rules.append("Guest friendly")
else:
    rules.append("No guests")

if utilities_included == "Yes":
    rules.append("Utilities included")

rules_str = ", ".join(rules)

# --- Store listing in session_state (optional) ---
st.session_state["current_listing"] = {
    "price": f"${int(price)}",
    "location": location,
    "lease": lease_type,
    "rules": rules_str,
    "desc": description or "No description provided."
}
# ===========================


# ===========================
# 🔻 PASTE ROOMMATE FORM CODE HERE (NO submit buttons, just capture values)
# Example: full_name = st.text_input(...), etc.
# ===========================


# ===========================
# 🔻 MATCH RESULTS — Put your match generation + display code below
# ONLY display if all needed fields are filled
# (ex: if location and full_name and location_pref ...)
# ===========================


# --- Footer ---
st.markdown("---")
st.caption("RoomLink © 2025 — Developed by Braxton Brown & Ridgill Jenkins | Winston-Salem State University | Computer Science Project")
