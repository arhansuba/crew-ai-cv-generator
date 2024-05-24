import ollama
import streamlit as st

# Function to generate interview questions
def generate_questions(job_title, num_questions):
    # Initialize Ollama LLM
    llm = ollama()

    # Generate interview questions using Ollama
    prompt = f"Generate interview questions for a candidate applying for a {job_title} position."
    response = llm.generate(prompt, max_tokens=200, num_results=num_questions)
    questions = response["text"].split("\n")[:num_questions]  # Limit to num_questions

    return questions

# Function to conduct the interview
def conduct_interview(questions):
    st.header("AI Interviewer")
    st.write("Welcome to the AI Interviewer! I'll be asking you a series of questions to assess your suitability for the position.")

    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(question)
        st.text_area("Your Answer", key=f"answer_{i}")

# Main function
def main():
    st.title("AI Interviewer")

    # Sidebar options
    st.sidebar.subheader("Options")

    # Custom job title input
    custom_job_title = st.sidebar.text_input("Enter Your Job Title or Profession")

    # Number of questions selection
    num_questions = st.sidebar.slider("Number of Questions", min_value=5, max_value=20, value=10)

    # Generate interview questions
    if st.sidebar.button("Generate Questions"):
        if custom_job_title:
            questions = generate_questions(custom_job_title, num_questions)
            conduct_interview(questions)
        else:
            st.error("Please enter your job title or profession.")

# Run the main function
if __name__ == "__main__":
    main()
