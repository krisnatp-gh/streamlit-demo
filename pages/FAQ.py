import streamlit as st

def faq_page():
    # Set page configuration
    st.set_page_config(
        page_title="Obesity Predictor FAQ",
        page_icon="❓",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # # Sidebar Navigation
    # page = st.sidebar.radio("Navigate", 
    #     ["Home", "Predictor", "FAQ"], 
    #     index=2
    # )

    # # Navigation Logic
    # if page == "Home":
    #     st.switch_page("home_page.py")
    # elif page == "Predictor":
    #     st.switch_page("predictor_page.py")

    # Main FAQ Content
    st.title("Frequently Asked Questions")

    faqs = [
        {
            "question": "How does the Obesity Predictor work?",
            "answer": "Our predictor uses a machine learning model trained on comprehensive health data. By analyzing inputs like age, weight, height, lifestyle, and dietary habits, it predicts potential obesity levels."
        },
        {
            "question": "What factors influence obesity prediction?",
            "answer": "Key factors include age, gender, height, weight, family history, physical activity, dietary habits, water intake, tech device usage, and more."
        },
        {
            "question": "Is my data safe?",
            "answer": "Yes, all personal information is processed locally and not stored or shared. Your privacy is our top priority."
        },
        {
            "question": "How accurate is the prediction?",
            "answer": "While our model is based on advanced machine learning techniques, it should not replace professional medical advice. It provides an estimate based on available data."
        }
    ]

    for faq in faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

    # Additional Resources
    st.markdown("### Additional Resources")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[WHO Obesity Information](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)")
    with col2:
        st.markdown("[CDC Healthy Weight](https://www.cdc.gov/healthyweight/index.html)")

def main():
    faq_page()

if __name__ == "__main__":
    main()