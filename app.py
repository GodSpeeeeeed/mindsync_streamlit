import streamlit as st
from utils.feelings_data import feelings_data

# Set page config
st.set_page_config(
    page_title="MindSync",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .big-font {
        font-size: 4rem !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }
    .description {
        font-size: 1.5rem !important;
        text-align: center !important;
        margin-bottom: 3rem !important;
    }
    .feelings-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    .feeling-card {
        width: 100px;
        text-align: center;
        margin: 1rem;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .feeling-card:hover {
        transform: scale(1.1);
    }
    .section-title {
        font-size: 2rem !important;
        margin: 2rem 0 1rem 0 !important;
        text-align: center !important;
    }
    .team-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    .team-member {
        width: 200px;
        text-align: center;
        margin: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Home Page
def home_page():
    st.markdown('<div class="big-font">MindSync</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Your compassionate mental health companion, here to listen and guide you towards emotional well-being.</div>', unsafe_allow_html=True)
    
    # Chatbot entry button
    with st.container(border=True, height=200):
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<div style='height: 50px'></div>", unsafe_allow_html=True)
            if st.button("Enter MindSync Chatbot", 
                        use_container_width=True,
                        type="primary",
                        help="Click to start chatting"):
                st.switch_page("pages/1_🧠_Chatbot.py")
    
    # Feelings section
    st.markdown('<div class="section-title">How are you feeling today?</div>', unsafe_allow_html=True)
    
    feelings = [
        {"name": "Happy", "icon": "😊", "color": "#FFD700"},
        {"name": "Sad", "icon": "😢", "color": "#6495ED"},
        {"name": "Angry", "icon": "😠", "color": "#FF6347"},
        {"name": "Anxious", "icon": "😰", "color": "#9370DB"},
        {"name": "Stressed", "icon": "😫", "color": "#FFA07A"}
    ]
    
    cols = st.columns(5)
    for i, feeling in enumerate(feelings):
        with cols[i]:
            if st.button(f"{feeling['icon']}\n{feeling['name']}", key=f"feeling_{feeling['name']}"):
                st.session_state['selected_feeling'] = feeling['name']
    
    # Display feeling details if selected
    if 'selected_feeling' in st.session_state:
        feeling = st.session_state['selected_feeling']
        with st.expander(f"About {feeling}", expanded=True):
            data = feelings_data.get(feeling.lower(), {})
            st.subheader("Symptoms")
            st.write(data.get("symptoms", "No data available"))
            
            st.subheader("What You Can Do")
            st.write(data.get("cures", "No data available"))
            
            st.subheader("Helpful Resources")
            for resource in data.get("resources", []):
                st.markdown(f"- [{resource['title']}]({resource['url']})")
    
    # Wellness Tools
    st.markdown('<div class="section-title">Wellness Tools</div>', unsafe_allow_html=True)
    st.write("Explore our collection of tools to support your mental health journey.")
    if st.button("Browse Wellness Tools →"):
        st.switch_page("pages/2_🌿_Wellness_Tools.py")
    
    # About Us
    st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)
    st.write("Meet the team behind MindSync")
    if st.button("Meet the Team →"):
        st.switch_page("pages/3_👥_About_Us.py")

# Main app logic
def main():
    home_page()

if __name__ == "__main__":
    main()