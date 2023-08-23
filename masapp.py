# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:35:34 2023

@author: 27823
"""
from PIL import Image
import streamlit as st


st.set_page_config(page_title="masinsight", page_icon="images/Capture.PNG", layout="wide")

img_logo = Image.open("images/masinsightnew.png")
# Specify the width and height values
image_width = 300  # in pixels
image_height = 200  # in pixels
st.image(img_logo)
st.markdown(f'<img src="{image}" width="{image_width}" height="{image_height}">', unsafe_allow_html=True)

#---LOAD ASSETS---

video_file1 = open("video/rentalprop.mov", "rb")
video_bytes1 = video_file1.read()
video_file2 = open("video/salespredict.mov", "rb")
video_bytes2 = video_file2.read()


#--- ABOUT ---
st.write("---")
st.header("Using Econometric Modelling to simplify marketing business problems")
st.write(
    """
    Generate business strategies with easy-to-use dashboards
    
    """)

st.write("---")

st.header("What do you want to analyze?")
st.write("##")
                  
with st.container():
    #st.header("Are you a visual thinker?")
    st.write("##")
    video_column, text_column = st.columns((1,2))
    with video_column:
        st.video(video_bytes1)
    with text_column:
        st.subheader("Real Estate Dashboard")
        st.write(
            """
            Analyze residential properties by tracking real estate prices to compare assets across cities. 
            
            """
            )
        st.write("[View Here >](https://propertytrendsdashpy-mtk4fbj3lf.streamlit.app/)")
        
with st.container():
    st.write("---")
    st.write("##")
    video_column1, text_column = st.columns((1,2))
    with video_column1:
        st.video(video_bytes2)
    with text_column:
        st.subheader("Sales Forecasting Dashboard")
        st.write(
            """
            Gain insights on expected sales or the potential impact of seasonal factors, such as holidays or marketing campaigns
            
            """
            )
        st.write("[View Here >](https://salespredictionapp.streamlit.app/)")        

#UPCOMING TOOLS
st.write("---") 
st.header("Upcoming Dashboards:")
st.markdown("""
             **Product Interest Prediction:** Analyze which customers are likely to purchase a product from your marketing mail list   
             **Influencer Impact:** Analyze the impact of influencer marketing on sales using sales and impressions data   

            """)
#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")      
        
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
    pass
 
                    
