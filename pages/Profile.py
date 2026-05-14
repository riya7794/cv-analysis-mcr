import streamlit as st
import time
import pymongo
conn=pymongo.MongoClient("mongodb+srv://shahiriya699_db_user:<db_password>@cluster0.ad4csox.mongodb.net/?appName=Cluster0")
mydb=conn["cv"]
my=mydb["user_info"]
with st.spinner("Loading...."):
    time.sleep(2)
c1,c2,c3,c4=st.columns(4)
st.header("User Profile")
st.success(st.session_state['username'])
st.success(f"Welcome:{st.session_state['username']}")
if c1.button("See  Profile"):
    st.subheader("Profile Status")
    str1=st.session_state['username']
    res=my.find({"username":str1})
    for data in res:
        st.success(f"Username:{data['username']}")
        st.success(f"Password:{data['password']}")
        st.success(f"Gender:{data['gender']}")
        st.success(f"Address:{data['address']}")
        st.success(f"Dob:{data['dob']}")
        img1 = data['photo']
        st.image(img1,width=100)
if c2.button("Change Password"):
    st.switch_page("pages/change pass.py")
if c3.button("CV Analysis"):
    st.switch_page("pages/cv.py")
if c4.button("Contact Us"):
    st.switch_page("pages/contact.py")        
