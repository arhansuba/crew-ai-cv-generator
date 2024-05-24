import ollama
import streamlit as st
from langchain_community.utils import preprocess_text
from langchain_community.chat_models import ChatOllama

def evaluate_cv(cv_text: str) -> str:
    # Preprocess CV text
    cv_text = preprocess_text(cv_text)

    # Define evaluation prompt
    prompt = f"""
    Evaluate the quality of the following CV:

    {cv_text}

    Provide feedback on the strengths and weaknesses of the CV and suggest areas for improvement.
    """

    # Initialize Ollama LLM
    llm = ollama()

    # Generate evaluation using Ollama
    response = llm.generate(prompt)
    evaluation = response['text']
    
    return evaluation

def display_evaluation(cv_text: str, evaluation: str):
    st.subheader("Evaluation Result")
    st.write(f"**CV Text:**\n{cv_text}")
    st.write(f"**Evaluation:**\n{evaluation}")

def main():
    st.title("CV Evaluator")

    # User input: CV text
    cv_text = st.text_area("Paste the CV text here:", height=200)

    if st.button("Evaluate CV"):
        if cv_text:
            # Evaluate CV
            evaluation = evaluate_cv(cv_text)

            # Display evaluation
            display_evaluation(cv_text, evaluation)
        else:
            st.error("Please paste the CV text before evaluating.")

if __name__ == "__main__":
    main()
