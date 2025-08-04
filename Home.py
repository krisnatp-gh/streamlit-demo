import streamlit as st

def home_page():
    # Set page configuration
    st.set_page_config(
        page_title="Obesity Predictor Home",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .main-title {
            color: #2C3E50;
            font-size: 48px;
            text-align: center;
            margin-bottom: 30px;
        }
        .subtitle {
            color: #34495E;
            text-align: center;
            margin-bottom: 40px;
        }
        .description {
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    # # Sidebar Navigation
    # page = st.sidebar.radio("Navigate", 
    #     ["Home", "Predictor", "FAQ"], 
    #     index=0
    # )

    # # Sidebar additional elements
    # st.sidebar.markdown("---")
    # st.sidebar.info("🏥 Obesity Level Predictor")

    # # Navigation Logic
    # if page == "Predictor":
    #     st.switch_page("pages/predictor_page.py")
    # elif page == "FAQ":
    #     st.switch_page("pages/faq_page.py")

    # Main content for Home page
    st.markdown('<h1 class="main-title">🏥 Obesity Level Predictor</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="subtitle">Understand Your Health at a Glance</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="description">
    <p>Our advanced machine learning model helps you assess your obesity risk 
    by analyzing various personal health and lifestyle factors. By inputting 
    key information like age, weight, height, dietary habits, and physical activity, 
    you can get an instant prediction of your obesity level.</p>
    </div>
    """, unsafe_allow_html=True)

    # Information Sections
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📊 Comprehensive Analysis")
        st.write("Our model considers multiple health parameters to provide an accurate assessment.")
    
    with col2:
        st.markdown("#### 🔬 Machine Learning Powered")
        st.write("Leveraging advanced algorithms to predict obesity levels with high accuracy.")
    
    with col3:
        st.markdown("#### 🩺 Health Insights")
        st.write("Get personalized recommendations based on your predicted obesity level.")

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: #7F8C8D;">
    <p>Disclaimer: This tool is for informational purposes and does not replace professional medical advice.</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    home_page()

if __name__ == "__main__":
    main()