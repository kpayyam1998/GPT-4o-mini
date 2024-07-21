import requests
import streamlit as st

st.title("GPT-4o-Mini model")


query=st.text_input("Enter you query")

if st.button("Submit"):
    try:

        url="http://127.0.0.1:5000/api/gpt4omini"
        data={
            "prompt": query
        }
        headers = {
        "Content-Type": "application/json"
        }
        response=requests.post(url,json=data,headers=headers)

        if response.status_code==200:
            st.success(response.json()['message'])
        else:
            st.error(response.json()['error'])
    except ValueError:
        st.error("Please enter a valid prompt")

