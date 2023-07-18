


from bardapi import Bard
import streamlit as st
import os
from dotenv import load_dotenv




_Bard_API_KEY = os.environ.get("_BARD_API_KEY") 
load_dotenv()


st.set_page_config(
    page_title="Enigma Engine ",
  
)
st.title("Welcome to Enigma-Engine")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFFFFF; /* Default background color */
        }
         .user-message {
            color: white;
            background-color: #2B2B2B;
            padding: 10px;
            border-radius: 5px;
        }
        .engine-message {
            color: white;
            background-color: #1E90FF;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
     input_text = st.text_input("You:", value="", key="user_input", help="Type your query here...")
     return input_text

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_text = user_input()
if user_text:
    response = response_api(user_text)
    st.session_state.messages.append({"user": user_text, "response": response})
   
if st.session_state.messages:
    # st.image("chat_icon.png", width=100)  # Replace with your chat icon or logo
    for msg in st.session_state.messages:
        st.write("You:", msg["user"])
        st.write("Enigma Engine:", msg["response"])
        st.write("---")


      
  

