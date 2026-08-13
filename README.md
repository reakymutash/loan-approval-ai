
# 🏦 FinTech Loan Underwriting AI

A machine learning-powered decision-support dashboard built for loan officers and underwriters. This application assesses the risk of loan default using a Decision Tree classifier while prioritizing human oversight, explainability, and data privacy.

---

## 🌟 Core Pillars of this Application

This project was engineered with responsible AI practices in mind:

* **Explainable AI (XAI):** Avoids "black box" decisions. The AI dynamically generates a custom risk report, highlighting specific red flags (e.g., low CIBIL scores or high DTI ratios) that triggered its assessment.
* **Human Oversight:** The AI acts as a co-pilot, not an autonomous agent. It outputs a probability-based risk assessment, requiring the human underwriter to make the final approval or rejection decision.
* **Data Privacy (Minimization):** Built with session-state controls that allow underwriters to instantly wipe sensitive applicant Personally Identifiable Information (PII) from the terminal memory.
* **Security:** Features a mock role-based authentication gateway, demonstrating how access can be restricted to authorized banking personnel only.

---

## 🛠️ Tech Stack

* **Frontend Interface:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** Scikit-Learn (Decision Tree Classifier)
* **Data Manipulation:** Pandas
* **Model Serialization:** Joblib
* **Deployment:** Streamlit Community Cloud

---

## 🚀 How to Run Locally

If you want to run this application on your local machine, follow these steps:

**1. Clone the repository:**

```bash
git clone [https://github.com/reakymutash/loan-approval-ai.git](https://github.com/reakymutash/loan-approval-ai.git)
cd loan-approval-ai
```
