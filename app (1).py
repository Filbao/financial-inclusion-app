import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.joblib")
columns = joblib.load("columns.joblib")

st.title("Financial Inclusion Predictor")

age = st.slider("Age", 18, 100, 30)
education = st.selectbox("Education", ["No formal education", "Primary education", "Secondary education", "Vocational/Specialised training", "Tertiary education"])
job = st.selectbox("Job Type", ["Self employed", "Government Dependent", "Formally employed Private", "Informally employed", "Other Income", "Farming and Fishing"])
gender = st.radio("Gender", ["Male", "Female"])
marital = st.selectbox("Marital Status", ["Single/Never Married", "Married/Living together", "Divorced/Separated", "Widowed", "Don't know"])
relationship = st.selectbox("Relationship", ["Head of Household", "Spouse", "Child", "Parent", "Other relative", "Other non-relatives"])
location = st.selectbox("Location", ["Urban", "Rural"])
cellphone = st.radio("Cellphone Access", ["Yes", "No"])
household_size = st.slider("Household Size", 1, 20, 5)

# Manual encoding
input_dict = {
    "age_of_respondent": age,
    "household_size": household_size,
    "education_level_Primary education": int(education == "Primary education"),
    "education_level_Secondary education": int(education == "Secondary education"),
    "education_level_Tertiary education": int(education == "Tertiary education"),
    "education_level_Vocational/Specialised training": int(education == "Vocational/Specialised training"),
    "job_type_Government Dependent": int(job == "Government Dependent"),
    "job_type_Formally employed Private": int(job == "Formally employed Private"),
    "job_type_Informally employed": int(job == "Informally employed"),
    "job_type_Other Income": int(job == "Other Income"),
    "job_type_Self employed": int(job == "Self employed"),
    "job_type_Farming and Fishing": int(job == "Farming and Fishing"),
    "gender_of_respondent_Male": int(gender == "Male"),
    "marital_status_Married/Living together": int(marital == "Married/Living together"),
    "marital_status_Single/Never Married": int(marital == "Single/Never Married"),
    "marital_status_Divorced/Separated": int(marital == "Divorced/Separated"),
    "marital_status_Widowed": int(marital == "Widowed"),
    "relationship_with_head_Head of Household": int(relationship == "Head of Household"),
    "relationship_with_head_Spouse": int(relationship == "Spouse"),
    "relationship_with_head_Child": int(relationship == "Child"),
    "relationship_with_head_Parent": int(relationship == "Parent"),
    "relationship_with_head_Other relative": int(relationship == "Other relative"),
    "relationship_with_head_Other non-relatives": int(relationship == "Other non-relatives"),
    "location_type_Urban": int(location == "Urban"),
    "cellphone_access_Yes": int(cellphone == "Yes")
}

# Create a DataFrame with all possible columns initialized to 0
input_df = pd.DataFrame(0, index=[0], columns=columns)

# Update the DataFrame with user inputs
for col, value in input_dict.items():
  if col in input_df.columns:
    input_df[col] = value

if st.button("Validate and Predict"):
    prediction = model.predict(input_df)[0]
    result = "Has Bank Account" if prediction == "Yes" else "No Bank Account"
    st.success(f"Prediction: {result}")
