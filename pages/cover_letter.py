import streamlit as st
from dataclasses import dataclass
import ollama

@dataclass
class UserDetails:
    name: str
    email: str
    phone: str
    job_title: str
    company_name: str
    company_address: str
    body: str

def generate_cover_letter(details: UserDetails) -> str:
    # Create a prompt for Ollama to generate a detailed cover letter
    prompt = f"""
    Generate a professional cover letter for the following details:
    
    Name: {details.name}
    Email: {details.email}
    Phone: {details.phone}
    
    Company Name: {details.company_name}
    Company Address: {details.company_address}
    
    Job Title: {details.job_title}
    
    Body: {details.body}
    
    The cover letter should start with a formal greeting, followed by an introduction, professional background, key skills and achievements, alignment with the company's values, and a conclusion expressing eagerness to discuss the application further.
    """
    
    # Use Ollama to generate the cover letter
    ollama_response = ollama.generate_text(prompt)
    cover_letter = ollama_response  # Assuming Ollama returns the generated text directly
    
    return cover_letter

def cover_letter_form() -> UserDetails:
    st.header("Cover Letter Generator")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    company_address = st.text_area("Company Address")
    body = st.text_area("Cover Letter Body")

    return UserDetails(name, email, phone, job_title, company_name, company_address, body)

def main():
    st.title("AI-Powered Cover Letter Generator")

    user_details = cover_letter_form()

    if st.button("Generate Cover Letter"):
        if all([user_details.name, user_details.email, user_details.phone, user_details.job_title, user_details.company_name, user_details.company_address, user_details.body]):
            cover_letter = generate_cover_letter(user_details)
            st.subheader("Your Generated Cover Letter")
            st.text_area("Cover Letter", value=cover_letter, height=300)
            st.download_button("Download Cover Letter", data=cover_letter, file_name="cover_letter.txt")
        else:
            st.error("Please fill in all the fields to generate the cover letter.")

if __name__ == "__main__":
    main()
