#  FinTech Loan Underwriting AI

A machine learning-powered decision-support dashboard built for loan officers and underwriters. This application assesses the risk of loan default using a Decision Tree classifier while prioritizing human oversight, explainability, and data privacy.

---

## Live Demo

You can test the live application here:
 [https://loan-approval-ai-gyh5zmx2wpy5nswbjetxbw.streamlit.app/](https://loan-approval-ai-gyh5zmx2wpy5nswbjetxbw.streamlit.app/)

###  Test Login Credentials

To bypass the security gateway on the live app, use the following credentials in the sidebar:

* **Underwriter ID:** `admin`
* **Password:** `1234`

---

##  Core Pillars of this Application

This project was engineered with responsible AI practices in mind:

* **Explainable AI (XAI):** Avoids "black box" decisions. The AI dynamically generates a custom risk report, highlighting specific red flags (e.g., low CIBIL scores or high DTI ratios) that triggered its assessment.
* **Human Oversight:** The AI acts as a co-pilot, not an autonomous agent. It outputs a probability-based risk assessment, requiring the human underwriter to make the final approval or rejection decision.
* **Data Privacy (Minimization):** Built with session-state controls that allow underwriters to instantly wipe sensitive applicant Personally Identifiable Information (PII) from the terminal memory.
* **Security:** Features a mock role-based authentication gateway, demonstrating how access can be restricted to authorized banking personnel only.

---

##  Tech Stack

* **Frontend Interface:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** Scikit-Learn (Decision Tree Classifier)
* **Data Manipulation:** Pandas
* **Model Serialization:** Joblib
* **Deployment:** Streamlit Community Cloud

---


