import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Available Housing Listings", layout="wide")
st.title("🏡 Available Housing Listings")
st.markdown("Explore current off-campus housing options submitted by students and verified listers. Listings include location, rent, amenities, and rules.")
st.markdown("---")

# Define path to CSV
csv_path = "data/housing_listings.csv"

# If CSV doesn't exist, create it with headers
if not os.path.exists(csv_path):
    df_empty = pd.DataFrame(columns=["price", "location", "lease", "rules", "desc"])
    df_empty.to_csv(csv_path, index=False)

# Load saved listings
df = pd.read_csv(csv_path)

# Check if there are any listings
if df.empty:
    st.info("No listings found yet. Be the first to submit your property!")
else:
    for i, row in df.iterrows():
        st.markdown(f"### 🏠 Listing #{i+1}")
        col1, col2 = st.columns([1.5, 2.5])
        
        with col1:
            st.markdown(f"**Price**: {row['price']}")
            st.markdown(f"**Location**: {row['location']}")
            st.markdown(f"**Lease Type**: {row['lease']}")
            st.markdown(f"**Rules & Amenities**: {row['rules']}")
        
        with col2:
            st.markdown(f"📌 _{row['desc']}_")

        st.markdown("---")
