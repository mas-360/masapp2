# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:35:34 2023

@author: 27823
"""
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="masinsight", page_icon="images/Capture.PNG", layout="wide")

#---logo
img_logo = Image.open("images/masinsight3.PNG") 


with st.container():
    image_col, txt_col = st.columns((0.3,1))
    with image_col:
        st.image(img_logo)
    with txt_col:
        st.empty()

#---HORIZONTAL MENU

selected = option_menu(
    menu_title=None,
    options=["Home", "Data Apps", "Contact"],
    icons=["house", "bar-chart", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#545454"},
        "icon": {"color": "#ffffff", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#a5a5a5",
            "color": "#ffffff"
            },
        "nav-link-selected": {"background-color": "#545454"},
    },
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

#---LOAD ASSETS---
lottie_coding1 = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_xk0j3gld.json")

img_dash_1 =Image.open("images/1.PNG") 
img_dash_2 = Image.open("images/Capture3.PNG")

if selected == "Home":
  
    #--- ABOUT ---
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((0.5,0.5))
        with left_column:
            st.header("Data visualization sits at the intersaction of science and art.")
            st.write("##")
            st.write(
                """
                Unlock the true potential of your data and storytelling with **masinsight**.    
                Overcoming barriers to producing business value has never been easier.  
                Don't let your data go to waste. Visualize your data like never before and join the ranks of data-driven pioneers.   
                Discover the untapped potential that lies within your information and propel your business towards unprecedented success.
                """)
        with right_column:
            st_lottie(lottie_coding1, 
                      height=300, 
                      key="coding"
                      ) 
                      
        with st.container():
            st.write("---")
            lft_col, rght_col = st.columns((1,1))
            
            with lft_col:
               st.header("How your data is transformed.")
               st.write("##")
               st.write(
                   """
                   From data cleansing and modeling to captivating visualization, **masinsight** seamlessly converts your information into a dynamic data app, all through the power of Python and Streamlit.   
                   Say goodbye to tedious manual processes on Excel, Google Sheets etc and hello to actionable insights at your fingertips.
                   """)
               with rght_col:
                   st.header("Your data is secure.")
                   st.write("##")
                   st.write(
                       """
                      We prioritize the protection of your valuable data by serving all data apps exclusively over HTTPS, guaranteeing end-to-end encryption. You have full control over who can access and manage your data apps within your business.   
                      Define permissions, set restrictions, and ensure that your sensitive information remains in trusted hands.
                       """
                   )
                   
                                   
    
elif selected == "Data Apps":
    
        with st.container():
            st.write("---")
            #st.header("Are you a visual thinker?")
            st.write("##")
            image_column, text_column = st.columns((1,2))
            with image_column:
                st.image(img_dash_1, width=400)
            with text_column:
                st.subheader("Customer Experience Dashboard")
                st.write(
                    """
                    Net Promoter Score (NPS), the ultimate loyalty metric, empowers you to gauge customer devotion and benchmark your performance in the market.
                    
                    """
                    )
                st.write("[View Here >](https://npsapppy-70b7nzky3j2.streamlit.app/)")
    
        
        with st.container():
            st.write("---")
            #st.header("Are you a visual thinker?")
            st.write("##")
            image_column, text_column = st.columns((1,2))
            with image_column:
                st.image(img_dash_2, width=400)
            with text_column:
                st.subheader("Real Estate Dashboard")
                st.write(
                    """
                    Analyze residential properties by tracking real estate prices to compare assets across cities. 
                    
                    """
                    )
                st.write("[View Here >](https://propertytrendsdashpy-mtk4fbj3lf.streamlit.app/)")
                
        
elif selected == "Contact":
        
    #---CONTACT FORM---
    with st.container():
        st.write("---")
        st.header("Unlock the potential of your data today!")
        st.write("Take the first step towards getting your very own data app by completing the simple form below.")
        st.write("##")
        
        contact_form = """
        <form action="https://formsubmit.co/masinsight360@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
       """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
                    
                    
