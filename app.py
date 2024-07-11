from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import os

# Set the page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to apply local CSS
local_css("style/style.css")

# Load images
img_web_img = Image.open("images/web_img.png") 
img_web_process = Image.open("images/web_process.png")

# Page content
with st.container():
    st.subheader("Hi, I'm Thejzz :wave:")
    st.title("A Student From India")
    st.write("I'm a Computer Engineering Student at Ahalia School Of Engineering & Technology")
    st.write("[Learn more >](https://pythonandvba.com)")

# What I do section
with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(""" 
            Currently I'm looking for:
            - A Web designer position
            - Python Web development roles 
        """)

# Projects section
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_web_img)
    with text_column:
        st.subheader("Create Web App Using Python Flask")
        st.write(
            """
            Learn how to create a web app using python flask!
            """
        )
        st.markdown("[Watch video...](https://youtu.be/Z1RJmh_OqeA?si=KW3Yxip41Zy9USzD)")

# Contact form
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/thejzz.infinix@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
