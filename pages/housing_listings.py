import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Available Housing Listings", layout="wide")
st.title("🏡 Available Housing Listings")
st.markdown("Explore current off-campus housing options submitted by students and verified listers. Listings include location, rent, amenities, and rules.")
st.markdown("---")

# Define path to CSV
csv_path = "housing_listings.csv"  # no folder, file is in the root directory

# Ensure 'data/' folder exists
os.makedirs("data", exist_ok=True)

# If CSV doesn't exist, create it with headers
if not os.path.exists(csv_path):
    df_empty = pd.DataFrame(columns=["price", "location", "lease", "rules", "desc"])
    df_empty.to_csv(csv_path, index=False)

# Load saved listings
df = pd.read_csv(csv_path)

# --- Filter UI ---
if not df.empty:
    st.sidebar.header("🔍 Filter Listings")

    # Price range filter
    min_price, max_price = st.sidebar.slider("Monthly Rent ($)", 300, 2000, (500, 1000), step=50)

    # Location filter
    unique_locations = df["location"].dropna().unique().tolist()
    selected_locations = st.sidebar.multiselect("Filter by Location", unique_locations, default=unique_locations)

    # Filter DataFrame
    df["numeric_price"] = df["price"].str.extract('(\d+)').astype(float)
    filtered_df = df[
        (df["numeric_price"] >= min_price) &
        (df["numeric_price"] <= max_price) &
        (df["location"].isin(selected_locations))
    ]

    st.markdown(f"### Showing {len(filtered_df)} matching listings")

    for i, row in filtered_df.iterrows():
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
else:
    st.info("No listings found yet. Be the first to submit your property!")
