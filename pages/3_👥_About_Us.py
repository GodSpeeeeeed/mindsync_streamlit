import streamlit as st
import os
from pathlib import Path

st.set_page_config(
    page_title="About Us",
    page_icon="👥"
)

# Helper function to find image with multiple possible extensions
def find_image(base_path):
    extensions = ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
    for ext in extensions:
        if os.path.exists(f"{base_path}{ext}"):
            return f"{base_path}{ext}"
    return None

st.title("👥 About Us")
st.write("Meet the team behind MindSync")

team = [
    {
        "name": "Amlan Anurag",
        "role": "AI/ML Engineer",
        "bio": "Building intelligent systems with data",
        "photo_base": "assets/teams/img1"  # No extension
    },
    {
        "name": "Prerit Mohanty",
        "role": "AI/ML Engineer",
        "bio": "Transforming raw data into AI solutions",
        "photo_base": "assets/teams/img2"
    },
    {   
        "name": "Aditya Nanda",
        "role": "Developer",
        "bio": "Creates intuitive and calming user experiences.",
        "photo_base": "assets/teams/img3"
    },
    {
        "name": "Yashaswini Sarangi",
        "role": "Backend Developer",
        "bio": "Ensuring seamless backend system operations",
        "photo_base": "assets/teams/img4"
    }
]

cols = st.columns(2)
for i, member in enumerate(team):
    with cols[i % 2]:
        # Find the actual image file
        photo_path = find_image(member["photo_base"])
        
        if photo_path:
            st.image(photo_path, width=150, caption=member["name"])
        else:
            st.warning(f"Image not found for {member['name']}")
            st.image("https://via.placeholder.com/150", width=150, caption="Placeholder")
        
        st.subheader(member["name"])
        st.caption(member["role"])
        st.write(member["bio"])

# Add back button
if st.button("← Back to Home"):
    st.switch_page("app.py")