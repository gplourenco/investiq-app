import streamlit as st
from app.pages import Investment_Advice
from app.pages import User_Input

def main():
    st.set_page_config(page_title="InvestIQ", page_icon="💼", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a Page", ("Home", "User Input", "Investment Advice"))

    if page == "Home":
        home_page()
    elif page == "User Input":
        User_Input.user_input_page()
    elif page == "Investment Advice":
        Investment_Advice.investment_advice_page()

def home_page():
    st.title("Welcome to InvestIQ")
    st.markdown("""

    InvestIQ is your AI-powered robo-advisor, designed to democratize access to high-quality financial advice. Our platform is tailored for users with little to no prior experience in the financial markets, providing clear and detailed explanations for each investment recommendation.

    **Why Choose InvestIQ?**
    - **Educational Value**: Each investment recommendation comes with a detailed, easy-to-understand explanation, enhancing your financial literacy.
    - **Personalized Advice**: Our AI leverages advanced natural language models to provide investment advice tailored to your unique profile and needs.
    - **User-Friendly Platform**: With an intuitive interface, InvestIQ makes it easy to manage your investments and access advice on-the-go.

    ### How to Get Started

    1. **User Input**: Navigate to the "User Input" page to fill out your investment profile.
    2. **Investment Advice**: Once your profile is complete, go to the "Investment Advice" page to receive personalized investment recommendations.

    **Your Investment Journey Starts Here!**

    To begin, navigate to the "User Input" page and fill out your investment profile.
    """)

if __name__ == "__main__":
    main()
