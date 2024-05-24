import streamlit as st
from dataclasses import dataclass

import ollama
@dataclass
class UserDetails:
    name: str
    email: str
    phone: str
    address: str
    education: str
    experience: str
    skills: str
    certifications: str
    additional_info: str

def generate_cv(details: UserDetails) -> str:
    # Create a prompt for Ollama to generate a detailed CV
    prompt = f"""
    Generate a professional CV for the following details:

    Name: {details.name}
    Email: {details.email}
    Phone: {details.phone}
    Address: {details.address}

    Education: {details.education}
    Experience: {details.experience}
    Skills: {details.skills}
    Certifications: {details.certifications}
    Additional Info: {details.additional_info}

    The CV should be well-structured, with clear headings for each section, and formatted for a professional appearance.
    """
    
    # Use Ollama to generate the CV
    llm = ollama()
    response = llm.generate(prompt)
    cv_content = response['text']
    
    return cv_content

def cv_form() -> UserDetails:
    st.header("CV Generator")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")
    education = st.text_area("Education")
    experience = st.text_area("Experience")
    skills = st.text_area("Skills")
    certifications = st.text_area("Certifications")
    additional_info = st.text_area("Additional Information")

    return UserDetails(name, email, phone, address, education, experience, skills, certifications, additional_info)

def main():
    st.title("AI-Powered CV Generator")

    user_details = cv_form()

    if st.button("Generate CV"):
        if all([user_details.name, user_details.email, user_details.phone, user_details.address, 
                user_details.education, user_details.experience, user_details.skills, 
                user_details.certifications, user_details.additional_info]):
            cv = generate_cv(user_details)
            st.subheader("Your Generated CV")
            st.text_area("CV", value=cv, height=400)
            st.download_button("Download CV", data=cv, file_name="cv.txt")
        else:
            st.error("Please fill in all the fields to generate the CV.")

if __name__ == "__main__":
    main()
