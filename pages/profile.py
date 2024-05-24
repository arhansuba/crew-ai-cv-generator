import ollama
import streamlit as st
from streamlit_lottie import st_lottie

from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain, RetrievalQA
from langchain.prompts.prompt import PromptTemplate
from langchain.text_splitter import NLTKTextSplitter
import nltk
from typing import Literal, List
from dataclasses import dataclass
import json
import base64
import os

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Initialize Ollama LLM
ollama_llm = ollama()

# Function to save text vectors
def save_vector(text: str):
    nltk.download('punkt')
    text_splitter = NLTKTextSplitter()
    texts = text_splitter.split_text(text)
    embeddings = OllamaEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    return docsearch

# Initialize Streamlit app
st.title("Candidate Profile")

# Display welcome animation
st_lottie(load_lottiefile("images/welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)

# Error handling info
with st.expander("Why did I encounter errors when I tried to access the profile information?"):
    st.write("""
    This could be due to various reasons such as incorrect data format, network issues, or server errors. 
    Please ensure that the data provided is valid and try again. If the issue persists, contact support.""")

# Candidate profile input
candidate_profile = st.text_area("Please enter the candidate's profile information:")

# Function to initialize session state
def initialize_session_state():
    if 'profile_vector' not in st.session_state:
        st.session_state.profile_vector = save_vector(candidate_profile)
    if 'retriever' not in st.session_state:
        st.session_state.retriever = st.session_state.profile_vector.as_retriever(search_type="similarity")
    if 'chain_type_kwargs' not in st.session_state:
        Interview_Prompt = PromptTemplate(input_variables=["context", "question"], template="Ask questions relevant to the candidate's profile.")
        st.session_state.chain_type_kwargs = {"prompt": Interview_Prompt}
    if 'memory' not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()
    if "history" not in st.session_state:
        st.session_state.history = []
        st.session_state.history.append(Message("ai", "Hello! I'm the interviewer. Let's discuss your profile. Please introduce yourself."))
    if "token_count" not in st.session_state:
        st.session_state.token_count = 0
    if "guideline" not in st.session_state:
        st.session_state.guideline = RetrievalQA.from_chain_type(
            llm=ollama_llm,
            chain_type_kwargs=st.session_state.chain_type_kwargs,
            chain_type='stuff',
            retriever=st.session_state.retriever,
            memory=st.session_state.memory).run("Create an interview guideline and prepare relevant questions.")
    if "conversation" not in st.session_state:
        PROMPT = PromptTemplate(
            input_variables=["history", "input"],
            template="""Act as an interviewer following the given guideline. Ask questions related to the candidate's profile. Wait for responses and continue the conversation accordingly.

            Current Conversation:
            {history}

            Candidate: {input}
            AI: """
        )
        st.session_state.conversation = ConversationChain(prompt=PROMPT, llm=ollama_llm, memory=st.session_state.memory)

# Function to handle user answers
def answer_callback():
    # Get user's answer
    user_answer = st.session_state.answer
    # Add user's answer to history
    st.session_state.history.append(Message("human", user_answer))
    # Run conversation with Ollama
    ollama_answer = st.session_state.conversation.run(user_answer)
    # Add Ollama's answer to history
    st.session_state.history.append(Message("ai", ollama_answer))
    return ollama_answer

# Class to represent messages in conversation
@dataclass
class Message:
    origin: Literal["human", "ai"]
    message: str

# Initialize session state
initialize_session_state()

# Display interview guideline
st.sidebar.subheader("Options")
if st.sidebar.button("Show Interview Guideline"):
    st.write(st.session_state.guideline)

# Display interview feedback
if st.sidebar.button("Get Interview Feedback"):
    evaluation = st.session_state.feedback.run("Please provide feedback on the interview.")
    st.markdown(evaluation)
    st.download_button(label="Download Interview Feedback", data=evaluation, file_name="interview_feedback.txt")
    st.stop()

# Interview process
chat_placeholder = st.container()
answer_placeholder = st.container()
audio = None

if candidate_profile:
    with answer_placeholder:
        answer = st.text_input("Your answer:")
        if answer:
            st.session_state['answer'] = answer
            audio = answer_callback()

    with chat_placeholder:
        for msg in st.session_state.history:
            if msg.origin == 'ai':
                with st.chat_message("assistant"):
                    st.write(msg.message)
                    if audio:
                        st.write(audio)
            else:
                with st.chat_message("user"):
                    st.write(msg.message)
