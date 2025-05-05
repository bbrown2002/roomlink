import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="RoomLink | Find Your Next Roommate",
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

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("## 📂 Navigation")
    st.page_link("app.py", label="🏠 Home", icon="🏠")
    st.page_link("pages/room_form.py", label="📬 Submit a Room Listing", icon="📦")
    st.page_link("pages/housing_listings.py", label="🏡 View Housing Listings", icon="📍")

# --- Header ---
st.markdown('<p class="roomlink-header">RoomLink</p>', unsafe_allow_html=True)
st.markdown('<p class="roomlink-sub">Student Housing Made Safe, Smart, and Social</p>', unsafe_allow_html=True)
st.markdown("---")

# --- Main Hero Section ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🏠 Welcome to RoomLink")
    st.markdown("""
    **RoomLink** is a web-based housing and roommate discovery tool designed specifically for college students in Winston-Salem. Whether you're new to campus or just tired of unreliable roommate hookups, RoomLink puts everything in one place — clean, simple, and built with your needs in mind.

    🔒 Verified through school communities  
    🛏️ Filtered by lifestyle and rent preferences  
    💬 Easy access to listings and profiles
    """)

    st.markdown("### 🚀 Get Started:")
    if st.button("🏡  Find Housing"):
        st.switch_page("pages/housing_listings.py")

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
RoomLink connects students with local off-campus housing and roommate opportunities through two main systems:

1. **Roommate Directory**  
   Browse verified student profiles, each with habits, lifestyle preferences, rent expectations, and availability. Use filters to match with roommates who actually fit your vibe.

2. **Housing Listings**  
   Scroll listings from students and landlords in popular student neighborhoods. Filter by rent, lease terms, and rules like pets or smoking.

3. **Submit a Room**  
   List an available space with clean, simple forms. All data stays local and secure.

Together, these tools create a trusted network for college housing in Winston-Salem.
""")

# --- Testimonials ---
st.subheader("💬 What Students Are Saying")

col1, col2 = st.columns(2)
with col1:
    st.markdown("> “I found someone who matches my sleep schedule and study habits. I don’t miss random roommates at all.” — *Maya T.*")
with col2:
    st.markdown("> “I posted my extra room and had three people hit me up by the end of the week. Easy and clean.” — *Jaylen B.*")

# --- Trust Section ---
st.subheader("🔐 Built on Trust")
st.markdown("""
RoomLink is designed for one thing: **student safety**. We don’t just throw listings and bios on a page. Every form asks the right questions, and every profile prioritizes compatibility and real-life living.

✅ Students verify school status in submissions  
✅ No random strangers — just students looking to live right  
✅ No distractions — just clean housing and roommate info

Future upgrades may include messaging, .edu email sign-ins, and verified reviews.
""")

# --- Call to Action Banner ---
st.markdown("""
<div class="section-box">
<h4 style='margin-bottom:10px;'>Want to get listed?</h4>
<p>Fill out the housing form today and join the network. Whether you need a spot or have one to share — RoomLink makes it easy.</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("RoomLink © 2025 — Developed by Braxton Brown & Ridgill Jenkins | Winston-Salem State University | Computer Science Project")
