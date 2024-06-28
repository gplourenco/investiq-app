import streamlit as st

def user_input_page():
    st.title("Investment Profile")

    # Introduction text
    st.markdown("""
    Please fill out the form below to create your investment profile:
    """)

    # User profile form
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100)
    investment_amount = st.number_input("Investment Amount (€)", min_value=0.0, step=1000.0, format="%.2f")
    risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
    investment_duration = st.number_input("Investment Duration (years)", min_value=1, step=1)
    investment_goal = st.selectbox("Investment Goal", ["Retirement", "Wealth Growth", "Income Generation", "Home Purchase", "Other"])
    experience_level = st.selectbox("Investment Experience Level", ["Beginner", "Intermediate", "Advanced"])
    additional_concerns = st.text_area("Additional Concerns or Personalization Requests")


    if st.button("Submit"):
        st.session_state.user_profile = {
            "name": name,
            "age": age,
            "investment_amount": investment_amount,
            "risk_tolerance": risk_tolerance,
            "investment_duration": investment_duration,
            "investment_goal": investment_goal,
            "experience_level": experience_level,
            "additional_concerns": additional_concerns,
        }
        st.success("Profile saved! Go to the Investment Advice page.")

if __name__ == "__main__":
    user_input_page()
