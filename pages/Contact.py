import streamlit as st
st.title("Contact Us")
st.write("Fill out the form below and we'll get back to you")

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submit_button=st.form_submit_button("Send")

if submit_button:
    if name and email and message:
        st.success("Your message has been sent successfully!")


    st.write("### Submitted Details")
    st.write(f"Name:{name}")
    st.write(f"Email:{email}") 
    st.write(f"Message:{message}")
else:
        st.error("Please fill in all fields.") 
