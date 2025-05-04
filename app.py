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

# ========== MAIN TITLE ==========
st.title("🏠 RoomLink")
st.markdown("## Find housing. Find roommates. Live better.")

# ========== INTRO PARAGRAPH ==========
st.markdown("""
RoomLink is built for students who need off-campus housing and real roommate compatibility.  
Use the sidebar to get started:

- Submit a Roommate Match Form  
- Browse available Housing Listings
""")

# ========== DETAILED SECTION ==========
st.markdown("---")
st.markdown("## 🔍 What Is RoomLink?")

st.markdown("""
RoomLink is a web-based housing and roommate connection system designed to simplify the student living experience. Whether you're new to campus, relocating, or just tired of getting ghosted on Facebook housing groups, RoomLink gives you the tools to:
- 📬 List or find off-campus housing
- 🤝 Match with roommates based on lifestyle compatibility
- 🧠 Make better living decisions with verified info and community filters
""")

# ========== FEATURES ==========
st.markdown("---")
st.markdown("## 🌟 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧑‍🤝‍🧑 Roommate Matching")
    st.markdown("""
    • Match with students based on sleep schedule, social habits, and more  
    • Clean, easy-to-use form to submit your living preferences  
    • System designed to reduce lifestyle clashes  
    """)

    st.subheader("📄 Room Listings")
    st.markdown("""
    • Browse available off-campus housing options near your school  
    • Filter by rent, distance, pet policy, lease length, and more  
    • Organized display of listing info and contact details  
    """)

with col2:
    st.subheader("📬 Room Submission")
    st.markdown("""
    • Submit available housing to help other students  
    • Input price, location, lease terms, and upload image links  
    • Listings added directly to the platform’s housing page  
    """)

    st.subheader("🔒 Safety & Trust")
    st.markdown("""
    • School email verification (future feature)  
    • Private profiles until match confirmed  
    • Reduced risk through transparency and student-only visibility  
    """)

# ========== CALL TO ACTION ==========
st.markdown("---")
st.markdown("## 🚀 Ready to Get Started?")

st.markdown("""
Use the navigation sidebar to:
- 📝 Submit your **Roommate Match Form**  
- 🏘 Browse available **Housing Listings**  
- 📤 List your own housing opportunity  

RoomLink was created to give students power, safety, and clarity when choosing who they live with and where they live.
""")

# ========== FOOTER ==========
st.markdown("---")
st.caption("Developed by Braxton Brown • Winston-Salem State University • 2025")
st.caption("GitHub: [@bbrown2002](https://github.com/bbrown2002) • Built with ❤️ using Streamlit")
