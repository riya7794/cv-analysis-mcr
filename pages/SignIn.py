import streamlit as st
import pymongo

st.title("SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password")
if st.button("SIGNIN"):
     conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
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
