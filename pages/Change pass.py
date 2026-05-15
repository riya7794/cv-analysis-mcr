import streamlit as st
import time
import pymongo
st.header("Change Password")
conn=pymongo.MongoClient("mongodb+srv://Riya_123-mcrRiya-123098@:@cluster0.ad4csox.mongodb.net/?appName=Cluster0")
mydb=conn["cv"]
my=mydb["user_info"]
t1=st.text_input("Old Password")
t2=st.text_input("New Password")
if st.button("Change Password",key="b"):
    res=my.update_one({"password":t1},{'$set':{"password":t2}})
    st.success("Password Changed Successfully!!!")
    st.success(f"value:{res}")
