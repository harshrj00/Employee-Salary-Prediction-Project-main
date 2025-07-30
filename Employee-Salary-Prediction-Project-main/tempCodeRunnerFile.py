import streamlit as st
import pandas as pd
import joblib

# 🔧 Must be FIRST Streamlit command
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💸", layout="centered")

#  Load Model
try:
    model = joblib.load("best_model.pkl")
except Exception as e:
    st.error(f"Model failed to load: {e}")
    st.stop()

#  App Header
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px 10px;">
        <img src="https://edunetfoundation.org/wp-content/uploads/2022/11/Edunet-Foundation-logo.png" alt="Edunet Logo" width="140">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg" alt="IBM Logo" width="120">
    </div>
    <div style="text-align:center; margin-top: 10px;">
        <h1 style="color:#4CAF50;">Employee Salary Prediction WebApp </h1>
        <p><b>Enter your details to predict whether your income is likely to exceed ₹50,000/year.</b></p>
    </div>
""", unsafe_allow_html=True)

# Label Mappings

education_map = {
    "9th": 5,
    "10th": 6,
    "11th": 7,
    "12th": 8,
    "Completed high school (Grade 12)": 9,
    "Attended college but did not complete a degree": 10,
    "Associate's degree in a vocational program": 11,
    "Associate's degree in an academic programm": 12,
    "Bachelors": 13,
    "Masters": 14,
    "Completed a professional degree like law (LLB), medicine (MBBS), or similar": 15,
    "Doctorate": 16
}
workclass_map = {"Private": 3, "Self-emp-not-inc": 1, "Local-gov": 5, "State-gov": 4, "Federal-gov": 6, "Without-pay": 7, "Never-worked": 2, "Unknown": 0}
marital_map = {"Married": 1, "Single": 2, "Divorced": 3, "Separated": 4, "Widowed": 0}
relationship_map = {
    "Wife": 0,
    "Own-child": 1,
    "Husband": 2,
    "Not-in-family": 3,
    "Other-relative": 4,
    "Unmarried": 5
}

occupation_map = {
    "Tech-support": 0,
    "Craft-repair": 1,
    "Other-service": 2,
    "Sales": 3,
    "Exec-managerial": 4,
    "Prof-specialty": 5,
    "Handlers-cleaners": 6,
    "Machine-op-inspct": 7,
    "Adm-clerical": 8,
    "Farming-fishing": 9,
    "Transport-moving": 10,
    "Priv-house-serv": 11,
    "Protective-serv": 12,
    "Armed-Forces": 13,
    "Unknown": 14
}

race_map = {
    "White": 0,
    "Asian-Pac-Islander": 1,
    "Amer-Indian-Eskimo": 2,
    "Other": 3,
    "Black": 4
}
gender_map = {"Female": 0, "Male": 1}
native_country_map = {
    "Cambodia": 0, "Canada": 1, "China": 2, "Columbia": 3, "Cuba": 4, "Dominican-Republic": 5,
    "Ecuador": 6, "El-Salvador": 7, "England": 8, "France": 9, "Germany": 10, "Greece": 11,
    "Guatemala": 12, "Haiti": 13, "Holand-Netherlands": 14, "Honduras": 15, "Hong": 16, "Hungary": 17,
    "India": 18, "Iran": 19, "Ireland": 20, "Italy": 21, "Jamaica": 22, "Japan": 23, "Laos": 24,
    "Mexico": 25, "Nicaragua": 26, "Outlying-US(Guam-USVI-etc)": 27, "Peru": 28, "Philippines": 29,
    "Poland": 30, "Portugal": 31, "Puerto-Rico": 32, "Scotland": 33, "South": 34, "Taiwan": 35,
    "Thailand": 36, "Trinadad&Tobago": 37, "United-States": 38, "Vietnam": 39, "Yugoslavia": 40
}

#  Sidebar Inputs
st.sidebar.header("**📋 Provide Your Information**")
age = st.sidebar.number_input("Age", min_value=18, max_value=90, value=30)
selected_workclass = st.sidebar.selectbox("Workclass", list(workclass_map.keys()))
selected_education = st.sidebar.selectbox("Education Level", list(education_map.keys()))
educational_num = education_map[selected_education]
selected_marital = st.sidebar.selectbox("Marital Status", list(marital_map.keys()))
selected_relationship = st.sidebar.selectbox("Relationship", list(relationship_map.keys()))
selected_occupation = st.sidebar.selectbox("Occupation", list(occupation_map.keys()))
selected_race = st.sidebar.selectbox("Race", list(race_map.keys()))
selected_gender = st.sidebar.radio("Gender", list(gender_map.keys()))
capital_gain = st.sidebar.number_input("Capital Gain", min_value=0, max_value=100000, value=0)
capital_loss = st.sidebar.number_input("Capital Loss", min_value=0, max_value=5000, value=0)
hours_per_week = st.sidebar.number_input("Hours Per Week", min_value=1, max_value=100, value=40)
selected_country = st.sidebar.selectbox("Native Country", list(native_country_map.keys()))

# Convert Labels to Encoded Values
input_dict = {
    'age': age,
    'workclass': workclass_map[selected_workclass],
    'educational_num': educational_num,
    'marital_status': marital_map[selected_marital],
    'occupation': occupation_map[selected_occupation],
    'relationship': relationship_map[selected_relationship],
    'race': race_map[selected_race],
    'gender': gender_map[selected_gender],
    'capital_gain': capital_gain,
    'capital_loss': capital_loss,
    'hours_per_week': hours_per_week,
    'native_country': native_country_map[selected_country]
}

input_df = pd.DataFrame([input_dict])

#  Input Preview
st.subheader("🔍 Preview Your Input")
st.dataframe(input_df)

#  Reference Panel for Encoded Categories
with st.expander(" **What Do These Categories Mean?**"):
        st.markdown("**Relationship Codes:**")
        for label, code in relationship_map.items():
            st.markdown(f"- `{code}` = **{label}**")

        st.markdown("**Occupation Codes:**")
        for label, code in occupation_map.items():
            st.markdown(f"- `{code}` = **{label}**")

        st.markdown("**Race Codes:**")
        for label, code in race_map.items():
            st.markdown(f"- `{code}` = **{label}**")

        st.markdown("**Country Codes:**")
        for country, code in native_country_map.items():
            st.markdown(f"- Country `{code}` = **{country}**")
        
        st.markdown("**Education Level Reference:**")
        for label, code in education_map.items():
            st.markdown(f"- `{code}` = **{label}**")

#  Prediction
if st.button("**🔎 Predict Income**"):
    prediction = model.predict(input_df)[0]
    result_text = "Predicted Salary: More than ₹50,000" if prediction == 1 else "Predicted Salary: ₹50,000 or less"

     # 🗒️ Display Full Input Summary
    st.markdown("### 📋 Input Summary")
    st.markdown(f"""
    - **Age**: {age}  
    - **Workclass**: {selected_workclass}  
    - **Education Level**: {selected_education}  
    - **Marital Status**: {selected_marital}  
    - **Occupation**: {selected_occupation}  
    - **Relationship**: {selected_relationship}  
    - **Race**: {selected_race}  
    - **Gender**: {selected_gender}  
    - **Capital Gain**: ₹{capital_gain}  
    - **Capital Loss**: ₹{capital_loss}  
    - **Hours Per Week**: {hours_per_week}  
    - **Native Country**: {selected_country}  
    """)    


    st.markdown(f"<div class='prediction-box'> {result_text}</div>", unsafe_allow_html=True)

    if prediction == 1:
        st.markdown("###  Congratulations! You're projected to earn **more than ₹50,000** annually!")
        st.balloons()
    else:
        st.markdown("###  Estimated income is ₹50,000 or less — Keep growing, your potential is unlimited!")
        st.snow()

# 📎 Footer
st.markdown("---")
st.markdown("-> Powered by GradientBoosting, Scikit-learn Pipelines & Streamlit")
st.markdown("-> Inputs above are user-friendly — mapped to model's label-encoded categories automatically.")