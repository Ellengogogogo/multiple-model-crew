import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('Your Research Assistant')
# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
# os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Main topic of your research:")

if st.button('Run Research'):
    if not topic:
        st.error("Please fill the topic.")
    else:
        inputs = f"Research Topic: {topic}\n"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Results of your research project:")
        st.write(result)
