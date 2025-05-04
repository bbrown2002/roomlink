import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="RoomLink | Find Your Next Roommate",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- App Branding ---
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
    .cta-button {
        font-size: 18px;
        padding: 0.75rem 1.5rem;
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
    **RoomLink** is a web-based housing and roommate discovery tool built specifically for college students in Winston-Salem. Whether you’re looking for a safe off-campus place to stay or a compatible roommate with the same sleep schedule and study habits, we make the process simple and smart.

    We created this platform because students deserve better than unreliable group chats and random roommate assignments. RoomLink puts everything you need in one place—filtered by what actually matters: location, budget, lifestyle, and trust.

    🔒 Verified by school communities  
    🛏️ Filtered by lifestyle preferences  
    💬 Built with students in mind
    """)

    st.markdown("### 🚀 Get Started:")
    if st.button("🧑‍🤝‍🧑  Find a Roommate"):
        st.switch_page("pages/roommate_directory.py")

    if st.button("🏡  Find Housing"):
        st.switch_page("pages/housing_listings.py")

    if st.button("📝  Submit Your Info"):
        st.switch_page("pages/roommate_form.py")

with col2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=870&q=80", caption="Off-campus living, simplified", use_column_width=True)

st.markdown("---")

# --- How It Works Section ---
st.subheader("📚 How It Works")

st.markdown("""
RoomLink is divided into three main parts, all connected to make roommate and housing decisions less chaotic:

1. **Roommate Directory**  
   View a list of verified student profiles, complete with bio details, lifestyle habits, rent range, and location. Use filters to narrow by compatibility and click to view more.

2. **Housing Listings**  
   Explore available rooms and apartments submitted by students and local hosts. Listings include rent, location, lease terms, pet/smoking rules, and contact info.

3. **Submit Your Info**  
   Add yourself to the roommate pool or list your available property. Our forms ask all the right questions: sleep habits, guest rules, cleaning standards, and more.

Each submission helps build a stronger, safer student housing network in Winston-Salem.
""")

st.markdown("---")

# --- Trust & Community Section ---
st.subheader("🔐 Built on Trust")

st.markdown("""
RoomLink was designed with one thing in mind: **student safety**. That means verified users, protected data, and profiles that reflect real student lifestyles—not just avatars and anonymous posts.

✅ Users must confirm school affiliation in forms  
✅ Listings are reviewed for clarity and relevance  
✅ Lifestyle compatibility is prioritized over random pairings

It’s not just about housing—it’s about building a living situation that works.

Want features like messaging, school email sign-in, and verified reviews? That’s coming next. We’re just getting started.
""")

st.markdown("---")

# --- Footer ---
st.caption("RoomLink © 2025 — Developed by Braxton Brown & Ridgill Jenkins")
