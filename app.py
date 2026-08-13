import streamlit as st
import pandas as pd
import joblib


model = joblib.load('loan_model.pkl')


st.title(" FinTech Loan Underwriting AI")
st.write("Enter the applicant's financial details below to predict loan approval.")


cibil_score = st.number_input("CIBIL Credit Score", min_value=300, max_value=900, value=600)
calculated_dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=2.0, value=0.35)
loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=5)
commercial_assets = st.number_input("Commercial Assets Value", min_value=0, value=100000)


if st.button("Analyze Application"):
    # We package the inputs into a Pandas dataframe exactly like the one the AI studied
    # Note: For this MVP, we are only passing the top features the Decision Tree actually used
    input_data = pd.DataFrame({
        'cibil_score': [cibil_score],
        'calculated_dti': [calculated_dti],
        'loan_term': [loan_term],
        'commercial_assets_value': [commercial_assets]
    })
    
   
    prediction = model.predict(input_data)[0]
    
  
    st.markdown("---")
    if prediction == 1:
        st.error(" APPLICATION REJECTED: High Risk of Default")
    else:
        st.success(" APPLICATION APPROVED: Low Risk")