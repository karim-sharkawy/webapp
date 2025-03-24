import streamlit as st

st.title("Topic Modeling")

if "page" not in st.session_state:
    st.session_state.page = "Home"

def navigate_to(page):
    st.session_state.page = page

col1, col2, col3 = st.columns(3)


with col1:
    if st.button("Home"):
        navigate_to("Home")

with col2:
    if st.button("LDA Baseline"):
        navigate_to("LDA Baseline")

with col3:
    if st.button("BERTopic"):
        navigate_to("BERTopic")


if st.session_state.page == "Home":
    st.title("Research & Methodology")
    st.markdown("Topic Modeling Techniques:")
    st.markdown("BERT (BERTopic): Explanation of the advanced NLP technique used for analyzing the data, and its application in this project.")
    st.markdown("LDA as Baseline: Describe the use of Latent Dirichlet Allocation as a baseline for comparison and understanding.")
    st.markdown("Data Sources: How the data is being collected")
    st.markdown("Process Flow: Step-by-step breakdown of the analysis process, from data gathering to insights extraction.")

if st.session_state.page == "LDA Baseline":
    st.title("Insights & Findings of Latent Dirichlet Allocation (LDA) Model")
    st.markdown("Priliminary Results: If available, share initial findings, such as common themes, concerns, or emotions expressed by youth regarding climate anxiety.")
    st.markdown("Visualizations: ")
    st.markdown("Key Trends: ")

elif st.session_state.page == "BERTopic":
    st.title("Insights & Findings of BERTopic Model")
    st.markdown("Priliminary Results: If available, share initial findings, such as common themes, concerns, or emotions expressed by youth regarding climate anxiety.")
    st.markdown("Visualizations: ")
    st.markdown("Key Trends: ")