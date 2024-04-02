# Importing all the libraries
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_chat import message
import utils
import requests
import base64


def set_page_title():
    """
    Function to add the Header and Title of the streamlit webapp
    """
    st.set_page_config(page_title="Saiyan AI - Gen AI Powered Chatbot", page_icon=":robot:", layout="wide")
    st.markdown("""
    <style>
    .big-font {
        font-size:70px !important;
        color:#dc143c;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Saiyan AI - Natural Language to SQL Chatbot</p>', unsafe_allow_html=True)
    st.header("Revolutionising Customer Experience with Gen AI Powered NL2SQL Chatbot")


def load_lottieurl(url):
    """
    Function to add Chatbot animation using from lottie on the streamlit web app.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def add_bg_from_local(image_file):
    """
    Function to add background image for the webapp.
    """
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
  

def load_local_css(file_name):
    """
    Function to use css file stored in the style folder for improving the design of the web app.
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def initialize_session_state():
    """
    Session State is a way to share variables between reruns, for each user session.
    """
    st.session_state.setdefault('history', [])
    st.session_state.setdefault('generated', ["Hello! I am here to provide answers to questions fetched from Database."])
    st.session_state.setdefault('past', ["Hello Saiyan!"])


def display_chat(conversation_chain, chain):
    """
    Streamlit related code where we are passing conversation_chain instance created earlier
    It creates two containers
    container: To group our chat input form
    reply_container: To group the generated chat response

    Args:
    - conversation_chain: Instance of LangChain ConversationalRetrievalChain
    """
    # Create containers to better organise the elements on the streamlit webapp
    reply_container = st.container()
    container = st.container()

    with container:
        with st.form(key='chat_form', clear_on_submit=True):
            user_input = st.text_input("Question:", placeholder="Ask me any question related to the connected database", key='input')
            submit_button = st.form_submit_button(label='Send ⬆️')
        
        # Check if user submit question with user input and generate response of the question
        if submit_button and user_input:
            generate_response(user_input, conversation_chain, chain)
    
    # Display generated response to streamlit web UI
    display_generated_responses(reply_container)


def generate_response(user_input, conversation_chain, chain):
    """
    Generate LLM response based on the user question by retrieving data from Database
    Also, stores information to streamlit session states 'past' and 'generated' so that it can
    have memory of previous generation for conversational type of chats (Like chatGPT)

    Args
    - user_input(str): User input as a text
    - conversation_chain: Instance of ConversationalRetrievalChain 
    - chain: Instance 
    """
    with st.spinner('Generating your answer.....'):
        output = conversation_chat(user_input, conversation_chain, chain, st.session_state['history'])

    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)


def conversation_chat(user_input, conversation_chain, chain, history):
    """
    Returns LLM response after invoking model through conversation_chain

    Args:
    - user_input(str): User input
    - conversation_chain: Instance of ConversationalRetrievalChain
    - history: Previous response history
    returns:
    - result["answer"]: Response generated from LLM
    """
    response = conversation_chain.invoke(user_input)
    final_response = chain.invoke(f"Based on the following information please use the query parameter along with result to generate a human readble response with some context: query: {response['query']}, result: {response['result']}")
    history.append((user_input, final_response))
    return final_response


def display_generated_responses(reply_container):
    """
    Display generated LLM response to Streamlit Web UI

    Args:
    - reply_container: Streamlit container created at previous step
    """
    if st.session_state['generated']:
        with reply_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=f"{i}_user", avatar_style="adventurer")
                message(st.session_state["generated"][i], key=str(i), avatar_style="bottts")

def main():
    """
    First function to call when we start streamlit app
    """
    # Set the page title and header
    set_page_title()

    # Initialize session state
    initialize_session_state()

    # Add the animation on the webapp
    lottie_animation = load_lottieurl("https://lottie.host/809195fb-20cb-4ea3-a4f6-7bb0070316ce/zQt3oMjZon.json")
    st_lottie(lottie_animation, height=400, key="Sayian AI Chatbot")

    # Use local css file to improve the webapp further.
    load_local_css("style/style.css")
    
    # Hide some of the streamlit features
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>

            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Create the background for the webapp
    add_bg_from_local("images/background.jpg")  

    # Step 2: Initialize Streamlit
    conversation_chain, chain = utils.create_conversational_chain()

    #Step 3 - Display Chat to Web UI
    display_chat(conversation_chain, chain)

if __name__ == "__main__":
    main()
