import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="FinTech AI", page_icon="🏦", layout="wide")

model = joblib.load('loan_model.pkl')

st.title("🏦 FinTech Loan Underwriting AI")
st.markdown("Enter the applicant's financial details below to predict loan approval.")

col1, col2 = st.columns(2)

with col1:
    cibil_score = st.number_input("CIBIL Credit Score", min_value=300, max_value=900, value=600)
    loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=5)

with col2:
    calculated_dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=2.0, value=0.35)
    commercial_assets = st.number_input("Commercial Assets Value", min_value=0, value=100000)

st.markdown("---")


if st.button("Analyze Application"):
   
    input_data = pd.DataFrame({
        'no_of_dependents': [0],
        'education': [1], 
        'self_employed': [0], 
        'income_annum': [5000000],
        'loan_amount': [1000000],
        'loan_term': [loan_term],                   
        'cibil_score': [cibil_score],              
        'residential_assets_value': [0],
        'commercial_assets_value': [commercial_assets], 
        'luxury_assets_value': [0],
        'bank_asset_value': [0],
        'total_assets': [commercial_assets], 
        'monthly_income': [5000000 / 12],
        'monthly_payment': [1000000 / (loan_term * 12)],
        'calculated_dti': [calculated_dti]          
    })
    
   
    prediction = model.predict(input_data)[0]
    
  
    st.markdown("---")
    if prediction == 1:
        st.error(" APPLICATION REJECTED: High Risk of Default")
    else:
        st.success(" APPLICATION APPROVED: Low Risk")