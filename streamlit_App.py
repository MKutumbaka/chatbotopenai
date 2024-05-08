import streamlit as st
import openai
import json
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
def main():
    st.title("Chat with GPT-3.5")
    st.markdown("This app uses OpenAI's GPT-3.5 to chat with you!")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        response = get_gpt_response(user_input)
        st.text("GPT-3.5: " + response)

def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    main()
