import streamlit as st

st.set_page_config(
    page_title="Wellness Tools",
    page_icon="🌿"
)

st.title("🌿 Wellness Tools")

tools = [
    {
        "name": "Breathing Exercises",
        "description": "Guided breathing techniques to help reduce stress and anxiety.",
        "icon": "🧘",
        "link": "https://example.com/breathing"
    },
    {
        "name": "Meditation Guides",
        "description": "Audio guides for meditation and mindfulness practices.",
        "icon": "🕉️",
        "link": "https://example.com/meditation"
    },
    {
        "name": "Mood Tracker",
        "description": "Track your mood over time to identify patterns and triggers.",
        "icon": "📊",
        "link": "https://example.com/mood-tracker"
    },
    {
        "name": "Sleep Helper",
        "description": "Tools and tips to improve your sleep quality.",
        "icon": "😴",
        "link": "https://example.com/sleep"
    }
]

cols = st.columns(2)
for i, tool in enumerate(tools):
    with cols[i % 2]:
        with st.expander(f"{tool['icon']} {tool['name']}", expanded=True):
            st.write(tool['description'])
            st.markdown(f"[Explore this tool →]({tool['link']})")