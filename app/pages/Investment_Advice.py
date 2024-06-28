import streamlit as st
from ai.assistants.financial_assistant import get_financial_assistant

def investment_advice_page():
    st.title("Investment Advice")

    if 'user_profile' not in st.session_state:
        st.warning("Please fill out your investment profile first.")
        return

    user_profile = st.session_state.user_profile
    st.write(f"Generating advice for {user_profile['name']}")

    assistant = get_financial_assistant(debug_mode=True)

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

        # Generate initial investment advice
        initial_prompt = f"""
        Based on the following user profile, provide personalized investment advice:
        {user_profile}

        Include:
        1. Asset allocation recommendation
        2. Specific investment suggestions
        3. Explanation of the rationale behind your recommendations
        4. Any relevant market insights
        5. Final Summary of the investment strategy, the platform where the user should invest, and future steps.
        """
        response = ""
        for delta in assistant.run(initial_prompt):
            response += delta
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Display existing messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    if prompt := st.chat_input("Ask for more details or other investment advice:"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Construct the full conversation history
        conversation_history = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages])
        full_prompt = f"{conversation_history}\nUser: {prompt}\nAssistant:"

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ""
                resp_container = st.empty()
                for delta in assistant.run(full_prompt):
                    response += delta
                    resp_container.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    investment_advice_page()
