import streamlit as st
from prompt_builder import build_prompt
from gemini_client import GeminiClient
from post_processor import clean_email

# Initialize session state for fields
for key in ['company', 'role', 'purpose', 'tone', 'generated_email', 'is_generating']:
    if key not in st.session_state:
        if key == 'tone':
            st.session_state[key] = 'Formal'
        elif key == 'is_generating':
            st.session_state[key] = False
        else:
            st.session_state[key] = ''

st.title("AI Cold Email Generator")

with st.form(key="input_form"):
    st.session_state.company = st.text_input("Company Name", value=st.session_state.company)
    st.session_state.role = st.text_input("Recipient Role/Title", value=st.session_state.role)
    st.session_state.purpose = st.text_area("Purpose of Email", value=st.session_state.purpose)
    st.session_state.tone = st.selectbox("Tone", ['Formal', 'Friendly'], index=['Formal', 'Friendly'].index(st.session_state.tone))
    
    col1, col2 = st.columns(2)
    with col1:
        generate = st.form_submit_button("Generate Email")
    with col2:
        clear = st.form_submit_button("Clear")

# Clear action
if clear:
    st.session_state.company = ''
    st.session_state.role = ''
    st.session_state.purpose = ''
    st.session_state.tone = 'Formal'
    st.session_state.generated_email = ''
    st.rerun()

# Generate action
if generate:
    st.session_state.is_generating = True
    prompt = build_prompt(
        st.session_state.company,
        st.session_state.role,
        st.session_state.purpose,
        st.session_state.tone
    )
    client = GeminiClient()
    raw = client.generate(prompt)
    st.session_state.generated_email = clean_email(raw)
    st.session_state.is_generating = False

# Display generated email
if st.session_state.generated_email:
    st.subheader("Generated Cold Email")
    st.code(st.session_state.generated_email)
