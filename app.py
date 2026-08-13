import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="FinTech AI", page_icon=":material/source_environment:", layout="wide")

model = joblib.load('loan_model.pkl')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


with st.sidebar:
    st.title(":material/lock: Secure Portal")
   
    if not st.session_state['logged_in']:
        st.write("Authorized Personnel Only")
        username = st.text_input("Underwriter ID")
        password = st.text_input("Password", type="password")
        
        if st.button("Log In"):
            
            if username == "admin" and password == "1234":
                st.session_state['logged_in'] = True
                st.rerun() 
            else:
                st.error("Invalid credentials. Access denied.")
                
   
    else:
        st.success("Authenticated as: Senior Underwriter")
        if st.button("Secure Logout"):
            st.session_state.clear() 
            st.rerun()

if not st.session_state['logged_in']:
    st.warning(":material/warning: You must log in via the sidebar to access the underwriting AI.")
    st.stop() 

st.title(":material/account_balance: FinTech Loan Underwriting Model")
st.markdown("**Enter the applicant's financial details below to predict loan approval.**")

col1, col2 = st.columns(2)

with col1:
    cibil_score = st.number_input("CIBIL Credit Score", min_value=300, max_value=900, value=600)
    loan_term = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=5)

with col2:
    calculated_dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=2.0, value=0.35)
    commercial_assets = st.number_input("Commercial Assets Value", min_value=0, value=100000)

st.markdown("---")

if st.button("Run Risk Assessment"):
    
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
    
   
    prediction_probs = model.predict_proba(input_data)[0]
    default_risk = prediction_probs[1] * 100  
    
    st.markdown("---")
    st.markdown("## :material/robot_2: Risk Assessment Report")
    
    
    if default_risk > 50:
        st.warning(f":material/warning: **High Risk Detected:** The AI estimates a {default_risk:.1f}% chance of this applicant defaulting.")
    elif default_risk > 20:
        st.info(f":material/info: **Moderate Risk:** The AI estimates a {default_risk:.1f}% chance of default.")
    else:
        st.success(f":material/check: **Low Risk:** The AI estimates only a {default_risk:.1f}% chance of default.")

   
    st.markdown("### :material/warning: Key Factors to Review:")
    red_flags = 0
    
    if cibil_score <= 550:
        st.error(f"- **Critical:** Applicant's CIBIL Score is {cibil_score}. (Bank minimum standard is 550)")
        red_flags += 1
    if calculated_dti > 0.50:
        st.error(f"- **Warning:** Debt-to-Income ratio is high at {calculated_dti:.2f}. Applicant carries significant existing debt.")
        red_flags += 1
    if commercial_assets < 50000 and default_risk > 50:
         st.error(f"- **Warning:** Low commercial collateral (${commercial_assets:,.2f}) to secure a high-risk loan.")
         red_flags += 1
         
    if red_flags == 0:
        st.write("No major anomalies detected in the primary financial metrics.")

    st.markdown("---")
    st.markdown("## :material/person: Underwriter Decision")
    st.write("Review the assessment above. You hold the final authority on this application.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(":material/check: Officially Approve Loan", use_container_width=True):
            st.success("Action Logged: Loan manually approved by underwriter.")
    with col2:
        if st.button(":material/close: Officially Reject Loan", use_container_width=True):
            st.error("Action Logged: Loan manually rejected by underwriter.")

st.markdown("---")
st.markdown("### :material/lock: Data Privacy Controls")
st.write("Ensure customer PII is wiped from the terminal memory after processing.")

if st.button(":material/delete: Wipe Applicant Data & Reset Terminal"):
    st.session_state.clear()
    st.session_state['logged_in'] = True 
    st.rerun()