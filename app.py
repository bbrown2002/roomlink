import streamlit as st
import random

st.markdown("## 🧑‍🤝‍🧑 Available Roommates")

# Sample data to randomize
first_names = ["Ava", "Jaylen", "Maya", "Elijah", "Naomi", "Zion", "Jasmine", "Kai", "Nia", "Malik", "Deja", "Tre", "Sarai", "Khalil", "Skye"]
majors = ["Pre-nursing", "Engineering", "Creative Writing", "Sociology", "Biology", "Pre-Med", "Psychology", "Business", "Art", "Music"]
vibes = ["Quiet", "Clean freak", "Chill", "Sociable", "Early sleeper", "Night owl", "Smoker", "Pet friendly", "Gamer", "Gym rat"]
locations = ["Downtown", "Northside", "Rams Commons", "Near WSSU Library", "Midtown", "East Winston", "Salem Lake", "West End"]
genders = ["men", "women"]

def generate_roommate():
    gender = random.choice(genders)
    image_id = random.randint(0, 99)
    name = random.choice(first_names)
    age = random.randint(19, 25)
    major = random.choice(majors)
    vibe1, vibe2 = random.sample(vibes, 2)
    location = random.choice(locations)
    price = f"${random.randint(500, 750)}/mo"
    bio = f"{major} major. {vibe1}. {vibe2}."
    return {
        "name": f"{name}, {age}",
        "img": f"https://randomuser.me/api/portraits/{gender}/{image_id}.jpg",
        "bio": bio,
        "price": price,
        "location": location
    }

# Generate 10 fresh roommates
roommates = [generate_roommate() for _ in range(10)]

# Display in rows of 5
for i in range(0, len(roommates), 5):
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if i + idx < len(roommates):
            rm = roommates[i + idx]
            with col:
                st.image(rm["img"], width=100)
                st.markdown(f"**{rm['name']}**")
                st.caption(f"{rm['bio']}")
                st.markdown(f"💸 {rm['price']}  \n📍 {rm['location']}")
                st.button("View Profile", key=f"profile_{i+idx}")
st.markdown("---")
st.markdown("## 📍 Platform Overview")

st.markdown("""
RoomLink is a modern, student-centered web application designed to help users find safe, affordable off-campus housing and connect with compatible roommates. It addresses the most common pain points students face — limited verified listings, unreliable roommate sources, and no centralized way to filter based on lifestyle or budget.

Unlike outdated rental boards or sketchy group chats, RoomLink combines clean design with smart logic to make off-campus housing less stressful and more strategic.

### 🧠 Why RoomLink?

- **For Students, By Students**: Every feature is tailored toward the student lifestyle — from flexible lease filters to roommate matching by sleep schedule.
- **Verified Housing Data**: Listings include rent, rules, distance, and more — structured in a way that’s easy to compare.
- **Lifestyle-Based Matching**: Instead of random pairings, RoomLink learns your habits and matches you with roommates you’ll actually get along with.
- **Simple, Secure, and Scalable**: This version is a fully functioning prototype built using Streamlit and Python, but the structure supports future growth with messaging, verification, and school email sign-on.
""")

st.markdown("---")
st.markdown("## 🔑 Feature Highlights")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📬 Housing Listing Submission")
    st.markdown("""
    Any user can submit available housing using a simple form that collects:
    - Property address
    - Rent amount
    - Lease type and terms
    - Pet/smoking policies
    - Optional image links or notes

    All data is displayed on a clean listings page so students can browse and filter options easily.
    """)

with col2:
    st.subheader("📝 Roommate Match Form")
    st.markdown("""
    Our match form collects detailed lifestyle information:
    - Sleep schedule (early riser vs night owl)
    - Cleanliness rating
    - Social habits and guest policy
    - Preferred noise level, pets, smoking

    Users are matched based on overlapping preferences, not just availability.
    """)

st.markdown("---")
st.markdown("## 💻 Technologies Used")

st.markdown("""
RoomLink was designed to be scalable, fast, and accessible to anyone. The current build uses:

- **Streamlit**: To create a clean Python-powered UI with instant deployment.
- **GitHub**: For version control, project structure, and collaboration.
- **Google Forms/Sheets (optional)**: For mock backend data storage if needed.
- **RandomUser API**: To simulate real-world profiles without privacy concerns.
- **Python**: For all data handling, user logic, and future backend compatibility.

The project is hosted publicly on GitHub and deployable through Streamlit Cloud for real-time access.
""")

st.markdown("---")
st.markdown("## 📈 Future Roadmap")

st.markdown("""
RoomLink is designed to grow beyond a prototype. The structure supports features that could turn it into a full SaaS platform for student housing, including:

- 🔐 **School Email Verification**: Limit access to verified students only.
- 💬 **Built-in Messaging**: Let users connect through the app once matched.
- 🧾 **Contract Assistance**: Auto-generate lease templates or agreement forms.
- 🔎 **Advanced Filtering**: Add map views, ratings, and affordability calculators.
- 📲 **Mobile Optimization**: Convert to PWA or mobile-first layout with responsive design.
""")

st.markdown("---")
st.markdown("## 🚀 How to Use RoomLink")

st.markdown("""
Getting started is simple:
1. Use the sidebar to **submit your roommate preferences** or **list your available room**.
2. Browse the **available listings** and **read profile summaries**.
3. Use the information provided to reach out directly and make the right housing decision.

As a tool built by students for students, RoomLink centers accessibility, trust, and simplicity.
""")

st.markdown("---")
st.markdown("## 🧾 Credits & Acknowledgements")

st.markdown("""
RoomLink was developed by **Braxton Brown** as part of a computer science project focused on solving real-world student problems through smart, user-friendly technology. The project combines front-end design, back-end logic, and a clear focus on user needs.

**Special thanks to:**
- Winston-Salem State University
- Open-source communities (Streamlit, RandomUser, GitHub)
- Students who shared roommate horror stories that inspired this 😂
""")

st.markdown("---")
st.caption("RoomLink © 2025 — Developed by Braxton Brown & Ridgill Jenkins  | GitHub: @bbrown2002")
