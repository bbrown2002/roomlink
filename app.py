import streamlit as st
from faker import Faker
fake = Faker()
import random
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
    use_container_width=True  # ✅ Fix: updated parameter
)

st.markdown("---")

# Define apartments grouped by neighborhood
neighborhood_apartments = {
    "Ardmore": [
        "Legacy at Ardmore - 1606 Covington Heights Cir",
        "Ardmore Terrace - 2325 Cloverdale Ave",
        "Village at Ardmore Landing - 2225 Silas Creek Pkwy"
    ],
    "Cloverdale": [
        "Cloverdale Apartments - Near Cloverdale Plaza",
        "Cloverdale Plaza Apartments - Adjacent to Plaza",
        "Ardmore Terrace - 2325 Cloverdale Ave"
    ],
    "West End": [
        "West End Station - 206 N Green St",
        "4th and Green - 822 W 4th St",
        "The Easley - 994 W 2nd St"
    ],
    "Downtown": [
        "Link Apartments® 4th Street - 501 W 4th St",
        "The Easley - 994 W 2nd St",
        "The Artreaux - 950 N Trade St"
    ],
    "Old Salem": [
        "Belo House - 455 S Main St",
        "Old Salem Apartments - Near Museums & Gardens",
        "Historic District Rentals - Old Salem Area"
    ],
    "Reynolda Village": [
        "Pine Ridge at Reynolda - 3736 Reynolda Rd",
        "Corners at Crystal Lake - 2700 Reynolda Rd",
        "Reynolda Manor Apartments - 3736 Reynolda Rd"
    ],
    "Washington Park": [
        "255 Bond St Unit",
        "830 S Broad St - Remodeled Home",
        "2123 Hollyrood Street Apartments"
    ],
    "University Parkway": [
        "Assembly Terrace - 3731 University Pkwy",
        "Northcliffe Forest - 2030 Northcliffe Dr",
        "Beltway Park Apartments - 114 Penner St"
    ]
}

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
st.subheader("📬 Looking for a Room")

st.markdown("""
Use this section to share what you're looking for in a room, apartment, or housing setup in the Winston-Salem area.
Your info will help match you with listings and roommates that fit your needs.
""")

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Preferred Neighborhood or Area", [
        "Ardmore", "Cloverdale", "West End", "Downtown", "Old Salem",
        "Reynolda Village", "Washington Park", "University Parkway"
    ])
    price = st.number_input("Maximum Monthly Rent ($)", min_value=300, max_value=2000, step=25)
    lease_type = st.selectbox("Preferred Lease Type", ["Month-to-month", "6 months", "9 months", "12 months", "Flexible"])

with col2:
    pets_allowed = st.radio("Can Live with Pets?", ["Yes", "No"])
    smoking_policy = st.radio("Can Live with Smokers?", ["Yes", "No"])
    guest_policy = st.radio("Okay with Guests?", ["Yes", "No"])
    utilities_included = st.radio("Need Utilities Included?", ["Yes", "No"])

st.markdown("### 📝 Additional Notes")
description = st.text_area("Write a short description of your ideal setup, roommate expectations, or deal-breakers", height=150)

# --- Build "rules" string on the fly ---
rules = []
if pets_allowed == "Yes":
    rules.append("Pet friendly")
else:
    rules.append("No pets")

if smoking_policy == "Yes":
    rules.append("Can live with smokers")
else:
    rules.append("Non-smoking only")

if guest_policy == "Yes":
    rules.append("Guest friendly")
else:
    rules.append("No guests preferred")

if utilities_included == "Yes":
    rules.append("Needs utilities included")

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
st.subheader("📝 Roommate Match Preferences")

col1, col2 = st.columns(2)

with col1:
    full_name = st.text_input("Full Name")
    age = st.slider("Your Age", 18, 30, 20)
    gender = st.selectbox("Your Gender", ["Woman", "Man", "Non-binary", "Prefer not to say"])
    school_email = st.text_input("School Email (.edu)")
    major = st.text_input("Your Major")

with col2:
    cleanliness = st.selectbox("Cleanliness Level", ["Messy", "Average", "Very Clean"])
    sleep_schedule = st.selectbox("Sleep Schedule", ["Early Riser", "Night Owl", "Flexible"])
    social_level = st.selectbox("Social Comfort", ["Introverted", "Moderate", "Extroverted"])
    noise_tolerance = st.selectbox("Noise Tolerance", ["Low", "Medium", "High"])
    study_habits = st.selectbox("Study Habits", ["Quiet room", "Library", "With music", "Late-night"])

st.markdown("### Lifestyle Preferences")
lifestyle_col1, lifestyle_col2 = st.columns(2)

with lifestyle_col1:
    smoking_ok = st.radio("Okay living with someone who smokes?", ["Yes", "No"])
    pets_ok = st.radio("Okay living with pets?", ["Yes", "No"])

with lifestyle_col2:
    guests_ok = st.radio("Okay with overnight guests?", ["Never", "Sometimes", "Often"])
    shared_items = st.radio("Willing to share items?", ["Yes", "Some", "No"])

st.markdown("### Hobbies & Personal Statement")
hobbies = st.text_input("Your Hobbies (comma separated)", placeholder="Ex: Gaming, Gym, Reading")
bio = st.text_area("Tell us about yourself and what kind of roommate you're looking for.")

# --- Store in Session Live ---
st.session_state["user_preferences"] = {
    "full_name": full_name,
    "age": age,
    "gender": gender,
    "school_email": school_email,
    "major": major,
    "cleanliness": cleanliness,
    "sleep_schedule": sleep_schedule,
    "social_level": social_level,
    "noise_tolerance": noise_tolerance,
    "study_habits": study_habits,
    "smoking_ok": smoking_ok,
    "pets_ok": pets_ok,
    "guests_ok": guests_ok,
    "shared_items": shared_items,
    "hobbies": hobbies,
    "bio": bio
}
# ===========================


# ===========================
# --- Roommate Match Results ---

if "user_preferences" in st.session_state:
    prefs = st.session_state["user_preferences"]

    st.subheader("🎯 Your Roommate Matches")
    st.markdown(f"""
    Based on the preferences submitted by **{prefs['full_name']}**, here are your best roommate matches.
    These aren’t perfect clones, but they're matched on **budget, lifestyle, and social compatibility**.
    """)

    def generate_variation(preference, category):
        variations = {
            "cleanliness": {
                "Messy": ["Average", "Messy"],
                "Average": ["Very Clean", "Average"],
                "Very Clean": ["Very Clean", "Average"]
            },
            "sleep_schedule": {
                "Early Riser": ["Early Riser", "Flexible"],
                "Night Owl": ["Night Owl", "Flexible"],
                "Flexible": ["Flexible", "Early Riser", "Night Owl"]
            },
            "social_level": {
                "Introverted": ["Introverted", "Moderate"],
                "Moderate": ["Introverted", "Extroverted", "Moderate"],
                "Extroverted": ["Extroverted", "Moderate"]
            },
            "noise_tolerance": {
                "Low": ["Low", "Medium"],
                "Medium": ["Low", "High"],
                "High": ["Medium", "High"]
            },
            "gender": {
                "Man": ["Man"],
                "Woman": ["Woman"],
                "Non-binary": ["Non-binary", "Woman", "Man"],
                "Prefer not to say": ["Man", "Woman", "Non-binary"]
            }
        }
        return random.choice(variations.get(category, {}).get(preference, [preference]))

    def generate_matches(prefs):
        listing = st.session_state.get("current_listing", {})
        base_budget = int(listing.get("price", "$1000").replace("$", ""))
        base_location = listing.get("location", "Downtown")

        matches = []
        for i in range(5):
            match = {
                "age": random.randint(18, 25),
                "gender": generate_variation(prefs["gender"], "gender"),
                "budget": random.randint(base_budget - 100, base_budget + 100),
                "location": random.choice(neighborhood_apartments.get(base_location, [base_location])),
                "cleanliness": generate_variation(prefs["cleanliness"], "cleanliness"),
                "sleep_schedule": generate_variation(prefs["sleep_schedule"], "sleep_schedule"),
                "social_level": generate_variation(prefs["social_level"], "social_level"),
                "noise_tolerance": generate_variation(prefs["noise_tolerance"], "noise_tolerance"),
                "study_habits": prefs["study_habits"],
                "smoking_ok": prefs["smoking_ok"],
                "pets_ok": prefs["pets_ok"],
                "guests_ok": prefs["guests_ok"],
                "shared_items": prefs["shared_items"],
                "hobbies": prefs["hobbies"] or "Not specified",
            }
            matches.append(match)

        return matches

    matches = generate_matches(prefs)

    def random_name(gender):
        if gender == "Man":
            return fake.name_male()
        elif gender == "Woman":
            return fake.name_female()
        else:
            return fake.name()

    for idx, m in enumerate(matches):
        name = random_name(m['gender'])
        first, last = name.split(" ")[0], name.split(" ")[-1]
        username = f"{first[0].lower()}{last.lower()}{random.randint(10, 99)}"

        st.markdown(f"### Match #{idx+1} — **{name}**")
        st.markdown(f"""
        - **Age**: {m['age']}
        - **Gender**: {m['gender']}
        - **Budget Range**: Around ${m['budget']} per month
        - **Preferred Location**: {m['location']}
        - **Cleanliness**: {m['cleanliness']}
        - **Sleep Schedule**: {m['sleep_schedule']}
        - **Social Comfort**: {m['social_level']}
        - **Noise Tolerance**: {m['noise_tolerance']}
        - **Study Habits**: {m['study_habits']}
        - **Open to Smoking Roommates**: {m['smoking_ok']}
        - **Okay with Pets**: {m['pets_ok']}
        - **Guest Policy**: {m['guests_ok']}
        - **Willing to Share Items**: {m['shared_items']}
        - **Shared Interests**: {m['hobbies']}
        """)

        with st.expander("💬 Contact Preview"):
            st.write(f"**Username:** {username}")
            st.write("**Status:** Online now ✅")
            st.text_area("Send a message...", placeholder=f"Hey! I'm also looking to live around {m['location']} — want to connect?", key=f"msg_text_{idx}")
            st.button("📨 Send Message", key=f"msg_btn_{idx}")

        st.markdown("---")
else:
    st.info("Fill out the housing and roommate forms above to see your matches.")


# ===========================


# --- Footer ---
st.markdown("---")
st.caption("RoomLink © 2025 — Developed by Braxton Brown & Ridgill Jenkins | Winston-Salem State University | Computer Science Project")
