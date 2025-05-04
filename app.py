import streamlit as st

st.set_page_config(
    page_title="RoomLink | Student Housing & Roommates",
    page_icon="🏠",
    layout="wide",
)

# ========== HERO SECTION ==========
st.markdown(
    """
    <h1 style='font-size: 3.5rem; font-weight: 800; margin-bottom: 0;'>🏠 Find your people.<br>Find your place.</h1>
    <p style='font-size: 1.1rem; margin-top: 0.5rem;'>
        RoomLink connects students to verified roommates and local housing that fits their lifestyle. 
        No scams. No weird Craigslist messages. Just clean vibes and compatible matches.
    </p>
    """,
    unsafe_allow_html=True
)

# ========== SEARCH BAR ==========
search = st.text_input("📍 Where are you looking?", placeholder="e.g. Winston-Salem, NC")

col1, col2, col3, col4 = st.columns(4)
col1.selectbox("💸 Max Monthly Rent", ["No Max", "$500", "$750", "$1000", "$1250+"])
col2.selectbox("📅 Urgency", ["ASAP", "This Month", "Next Semester"])
col3.selectbox("📆 Lease Length", ["Flexible", "6 Months", "12 Months"])
col4.selectbox("🐾 Pet Friendly?", ["Doesn't Matter", "Yes", "No"])

st.markdown("---")

# ========== ROOMMATE CARDS ==========
st.markdown("## 🧑‍🤝‍🧑 Featured Roommates")

r1, r2 = st.columns(2)

with r1:
    st.image("https://randomuser.me/api/portraits/women/44.jpg", width=80)
    st.markdown("### Emily, 24")
    st.caption("🛌 Private Room | 📍 Downtown | 💸 $650/mo | 🐶 Pets Allowed")
    st.markdown("> Quiet, clean, night owl. Film student looking for chill roommate.")
    st.button("View Profile", key="emily")

with r2:
    st.image("https://randomuser.me/api/portraits/men/52.jpg", width=80)
    st.markdown("### Marcus, 23")
    st.caption("🛌 Shared 2BR | 📍 West End | 💸 $700/mo | 🚭 No Smoking")
    st.markdown("> Gym rat. Early riser. Needs roommate by end of month.")
    st.button("View Profile", key="marcus")

st.markdown("---")

# ========== CTA ==========
st.markdown("## 👇 Ready to match or list a space?")
st.markdown(
    """
- [Roommate Match Form](#) — Submit your preferences  
- [Housing Listings](#) — Browse available places  
- [Add a Listing](#) — List your apartment or extra room  
"""
)

# ========== FOOTER ==========
st.markdown("---")
st.caption("RoomLink © 2025 — Built by Braxton Brown with Streamlit")
