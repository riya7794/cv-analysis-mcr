import streamlit as st
import pymongo

st.title("SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password")
if st.button("SIGNIN"):
     conn=pymongo.MongoClient("mongodb+srv://Riya_123-mcrRiya-123098@:@cluster0.ad4csox.mongodb.net/?appName=Cluster0")
     mydb=conn["cv"]
     my=mydb["user_info"]
     res=my.find({"username":t1,"password":t2})
     d=0
     for data in res:
         d=d+1
         st.session_state["username"]=data["username"]
         st.switch_page("pages/profile.py")
         
     if d==0:
         st.success("Invalid Login!!!!!")
