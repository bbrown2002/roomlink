import streamlit as st
from PIL import Image

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="RoomLink | Student Housing & Roommate Match",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== HEADER IMAGE ==========
# Optional: add your logo here
# st.image("assets/roomlink_logo.png", width=150)

st.title("🏠 RoomLink")
st.markdown("### Your One-Stop Platform for Off-Campus Housing and Roommate Matching")

# ========== INTRO PARAGRAPH ==========
st.markdown("""
Welcome to **RoomLink**, a platform built specifically for students navigating the chaos of off-campus living.  
Whether you're looking for a new place to stay or trying to avoid living with someone who leaves dishes in the sink for two weeks, we’ve got you covered.

RoomLink helps you:
- 🔍 **Browse verified housing listings** near campus
- 🤝 **Match with compatible roommates** based on your lifestyle
- 🧠 **Make smarter decisions** with clear, structured info
- 🔒 **Stay safe** with optional ID verification and profile filters
""")

# ========== FEATURES SECTION ==========
st.markdown("## 🌟 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 Roommate Matching")
    st.markdown("""
    - Personalized form collects lifestyle preferences
    - Filters by sleep schedule, cleanliness, social habits, and more
    - Avoid conflict by matching with people who actually vibe with you
    """)

    st.subheader("📬 Room Listing Submission")
    st.markdown("""
    - List available rooms or apartments
    - Upload price, location, lease length, pet policy, and more
    - Easy entry for students or local landlords
    """)

with col2:
    st.subheader("📄 Listings Page")
    st.markdown("""
    - See all active housing options with filters
    - View key info like rent, distance, rules, and contact email
    - Organized in a clean, scrollable table
    """)

    st.subheader("🛡 Safety & Trust")
    st.markdown("""
    - School email optional for verification
    - Profiles visible only after form submission
    - Future versions will include messaging and profile rating system
    """)

# ========== CALL TO ACTION ==========
st.markdown("---")
st.markdown("## 🚀 Ready to Get Started?")

st.markdown("""
Use the **navigation sidebar** to:
- Submit your roommate preferences
- Explore available listings
- Or list your own space

RoomLink was built with one goal in mind: **make student housing suck less**.
""")

st.info("🔧 This platform is still under development. All data shown is for demonstration purposes only.")

# ========== OPTIONAL FOOTER ==========
st.markdown("---")
st.caption("Developed by Braxton Brown | WSSU | 2025")
st.caption("GitHub: [@bbrown2002](https://github.com/bbrown2002) • Powered by Streamlit")

