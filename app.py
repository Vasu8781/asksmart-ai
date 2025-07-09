import streamlit as st
import requests
import json

API_KEY = "AIzaSyC__FewMUoeHIw4mqGHW4wFIWWtuj2GHwg"  # replace with a working key

st.set_page_config(page_title="AskSmart AI", page_icon="🦄")
st.title("🦄 AskSmart AI - Powered by Gemini")
st.subheader("Your intelligent multi-model AI assistant")

# Form to handle input + button together
with st.form(key="ask_form"):
    user_input = st.text_input("Ask me anything:")
    submit = st.form_submit_button("Ask")

# When button is clicked
if submit and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            headers = {"Content-Type": "application/json"}
            body = {
                "contents": [
                    {"parts": [{"text": user_input}]}
                ]
            }

            response = requests.post(url, headers=headers, data=json.dumps(body))

            if response.status_code == 200:
                result = response.json()
                output = result["candidates"][0]["content"]["parts"][0]["text"]
                st.markdown("### 💬 Answer:")
                st.write(output)
            else:
                st.error(f"❌ Error {response.status_code}: {response.json()}")

        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")
