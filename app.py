import streamlit as st
import json
import ollama
from utils import render_cv_template, translate_text
from utils import InterviewAgent, ReviewAgent

st.title("CV Generator Tool")

# Define constants
CV_TEXT_PLACEHOLDER = "<CV_TEXT>"
BASICS_PROMPT = "Generate basics section for the given CV:\n" + CV_TEXT_PLACEHOLDER
EDUCATION_PROMPT = "Generate education section for the given CV:\n" + CV_TEXT_PLACEHOLDER
AWARDS_PROMPT = "Generate awards section for the given CV:\n" + CV_TEXT_PLACEHOLDER
PROJECTS_PROMPT = "Generate projects section for the given CV:\n" + CV_TEXT_PLACEHOLDER
SKILLS_PROMPT = "Generate skills section for the given CV:\n" + CV_TEXT_PLACEHOLDER
WORK_PROMPT = "Generate work experience section for the given CV:\n" + CV_TEXT_PLACEHOLDER

# CV Template and Language Selection
cv_template_choice = st.selectbox("Select CV Template", ["template1.html", "template2.html"])
language_choice = st.selectbox("Select Language", ["English", "Turkish"])

# CV Data Input
cv_data = {
    "name": st.text_input("Name"),
    "summary": st.text_area("Summary"),
    "skills": st.text_area("Skills").split("\n"),
    "experience": st.text_area("Experience").split("\n"),
    "education": st.text_area("Education").split("\n"),
    "awards": st.text_area("Awards").split("\n"),
    "projects": st.text_area("Projects").split("\n"),
}

# Generate CV
if st.button("Generate CV"):
    if language_choice != "English":
        cv_data = translate_text(cv_data, 'tr')
    cv_html = render_cv_template(cv_data, f'cv_templates/{cv_template_choice}')
    st.markdown(cv_html, unsafe_allow_html=True)

# Job Description Input for Evaluation
job_description = st.text_area("Job Description")
if st.button("Evaluate CV"):
    # Initialize Ollama
    ollama = ollama()

    # Generate JSON resume from CV text
    def generate_json_resume(cv_text):
        sections = {}
        for prompt in [BASICS_PROMPT, EDUCATION_PROMPT, AWARDS_PROMPT, PROJECTS_PROMPT, SKILLS_PROMPT, WORK_PROMPT]:
            filled_prompt = prompt.replace(CV_TEXT_PLACEHOLDER, cv_text)
            response = ollama.complete(filled_prompt)
            try:
                answer = json.loads(response.choices[0].text.strip())
                sections.update(answer)
            except Exception as e:
                print(f"Error processing prompt: {prompt}")
                print(e)
        return sections

    # Tailor CV based on job description
    def tailor_resume(cv_text):
        tailored_prompt = f"Tailor the given CV based on the job description:\n{cv_text}"
        response = ollama.complete(tailored_prompt)
        try:
            return response.choices[0].text.strip()
        except Exception as e:
            print("Failed to tailor resume.")
            print(e)
            return cv_text

    # Generate and tailor CV
    json_resume = generate_json_resume(cv_data)
    tailored_cv = tailor_resume(json.dumps(json_resume))

    # Evaluate CV
    evaluation = InterviewAgent.evaluate_cv(tailored_cv, job_description)
    st.write("CV Evaluation:", evaluation)

    # Review Interview
    interview_transcript = st.text_area("Interview Transcript")
    review = ReviewAgent.review_interview(interview_transcript)
    st.write("Interview Review:", review)
