import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Obesity Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        color: #2C3E50;
        font-size: 36px;
        text-align: center;
        margin-bottom: 30px;
    }
    .sidebar .sidebar-content {
        background-color: #F0F4F8;
    }
    .stNumberInput, .stSelectbox {
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="main-title">🏥 Obesity Level Predictor</h1>', unsafe_allow_html=True)

# Sidebar with improved layout
st.sidebar.header("📊 Personal Health Information")
st.sidebar.markdown("---")

def user_input_features():    
    # Columns for better layout
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        Gender = st.selectbox("Gender", ['Male', 'Female'])
        Age = st.number_input("Age", min_value=14, max_value=61, step=1, value=22, 
                               help="Your current age")
        Height = st.number_input("Height (m)", 1.450, 1.980, 1.70, 0.001, 
                                  help="Height in meters")
        Weight = st.number_input("Weight (kg)", 39.0, 173.0, 83.0, 1.0, 
                                  help="Weight in kilograms")

    with col2:
        # Vegetable Intake
        veg_intake_map = {'Never': 1.0, 'Sometimes':2.0, 'Always':3.0}
        veg_intake_options = ["Never", "Sometimes", "Always"]
        veg_intake = st.selectbox("Vegetable Intake 🥗", veg_intake_options, 
                                   help="Frequency of vegetable consumption")
        FCVC = veg_intake_map[veg_intake]

        # Daily Meals
        dailymeals_map = {'1': 1.0, '2':2.0, '3':3.0, '>3':4.0}
        dailymeals_options = ["1", "2", "3", ">3"]
        dailymeals = st.selectbox("Daily Meals 🍗", dailymeals_options, 
                                   help="Number of meals per day")
        NCP = dailymeals_map[dailymeals]

        # Water Intake
        water_intake_map = {'<1 L': 1.0, '1-2 L':2.0, '>2 L':3.0}
        water_intake_options = ["<1 L", "1-2 L", ">2 L"]
        water_intake = st.selectbox("Water Intake 🚰", water_intake_options, 
                                    help="Daily water consumption")
        CH2O = water_intake_map[water_intake]

    # Additional sections with expanders for cleaner look
    with st.sidebar.expander("🚴 Physical Activity in a Week"):
        phys_act_map = {'1-2 days': 1.0, '2-4 days':2.0, '4-5 days':3.0}
        phys_act_options = ["1-2 days", "2-4 days", "4-5 days"]
        phys_act = st.selectbox("Physical Activity", phys_act_options, 
                                   help="Physical Activity Frequency on Weekdays")
        FAF = phys_act_map[phys_act]


    with st.sidebar.expander("🍔 Dietary Habits"):
        FAVC = st.selectbox("High Caloric Food Intake", ["yes", "no"])
        CAEC = st.selectbox("Snacking Habits", 
                             ['Sometimes', 'Frequently', 'Always', 'no'])
        CALC = st.selectbox("Alcohol Consumption", 
                             ['no', 'Sometimes', 'Frequently', 'Always'])

    with st.sidebar.expander("🚬 Additional Factors"):
        SMOKE = st.selectbox("Do you smoke?", ["yes", "no"])
        family_history = st.selectbox("Family Overweight History", ["yes", "no"])
        SCC = st.selectbox("Calorie Monitoring", ['no', 'yes'])
        MTRANS = st.selectbox("Transportation Mode", 
                               ['Public_Transportation', 'Walking', 
                                'Automobile', 'Motorbike', 'Bike'])

    # Tech Device Usage
    with st.sidebar.expander("💻 Technology Usage"):
        tech_usage_map = {'0-2 hours': 1.0, '3-5 hours':2.0, 'More than 5 hours':3.0}
        tech_usage_options = ["0-2 hours", "3-5 hours", "More than 5 hours"]
        tech_usage = st.selectbox("Tech Device Usage", tech_usage_options, 
                                   help="Time spent on devices such as phone, computer, etc.")
        TUE = tech_usage_map[tech_usage]



    # Create DataFrame with EXACT column names used in model training
    df = pd.DataFrame({
        "Gender": [Gender],
        "Age": [Age],
        "Height": [Height],
        "Weight": [Weight],
        "family_history_with_overweight": [family_history],
        "FAVC": [FAVC],
        "FCVC": [FCVC],
        "NCP": [NCP],
        "CAEC": [CAEC],
        "SMOKE": [SMOKE],
        "CH2O": [CH2O],
        "SCC": [SCC],
        "FAF": [FAF],
        "TUE": [TUE],
        "CALC": [CALC],
        "MTRANS": [MTRANS]
    })

    # Reorder columns to match model training
    column_order = ['Gender', 'Age', 'Height', 'Weight', 
                    'family_history_with_overweight', 'FAVC', 'FCVC', 
                    'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE', 
                    'CALC', 'MTRANS']
    
    return df[column_order]

# Main App Logic
def main():
    # User Input
    df_user = user_input_features()
    
    # Display input data for verification
    st.write("Input Data:", df_user)
    
    # Prediction Button
    if st.sidebar.button("Predict Obesity Level", type="primary"):
        try:
            # Load Model
            model_loaded = pickle.load(open('obesity_predictor_v2.sav', 'rb'))
            
            # Predict
            obesity_level = model_loaded.predict(df_user)[0][0]
            
            # Display Results with Styling
            st.markdown("## 📋 Prediction Results")
            st.info(f"### Your Predicted Obesity Level: {obesity_level}")
            
            # Optional: Add some visual feedback or explanation
            if obesity_level == "Obesity Type III":
                st.warning("⚠️ Consider consulting a healthcare professional.")
            elif obesity_level == "Normal Weight":
                st.success("👍 You're maintaining a healthy weight!")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()