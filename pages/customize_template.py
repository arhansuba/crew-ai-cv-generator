import ollama
import streamlit as st
from dataclasses import dataclass


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

def generate_cv(details: UserDetails, template: str) -> str:
    # Create a prompt for Ollama to generate a detailed CV using the selected template
    prompt = f"""
    Generate a professional CV using the following template:

    Template: {template}

    User Details:
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

def template_selection() -> str:
    st.header("Select and Customize Your CV Template")

    template_options = [
        "Classic",
        "Modern",
        "Creative",
        "Minimalist"
    ]
    
    template = st.selectbox("Choose a template", template_options)

    if template == "Classic":
        st.write("Classic template selected. This template is formal and traditional.")
    elif template == "Modern":
        st.write("Modern template selected. This template is sleek and stylish.")
    elif template == "Creative":
        st.write("Creative template selected. This template is colorful and unique.")
    elif template == "Minimalist":
        st.write("Minimalist template selected. This template is simple and clean.")

    # Allow users to add additional custom sections
    st.subheader("Customize Your Template")
    custom_section = st.text_area("Add any additional custom sections or notes here:")

    if custom_section:
        template += f"\nCustom Section: {custom_section}"

    return template

def main():
    st.title("AI-Powered CV Generator with Customizable Templates")

    user_details = cv_form()
    template = template_selection()

    if st.button("Generate CV"):
        if all([user_details.name, user_details.email, user_details.phone, user_details.address, 
                user_details.education, user_details.experience, user_details.skills, 
                user_details.certifications, user_details.additional_info]):
            cv = generate_cv(user_details, template)
            st.subheader("Your Generated CV")
            st.text_area("CV", value=cv, height=400)
            st.download_button("Download CV", data=cv, file_name="cv.txt")
        else:
            st.error("Please fill in all the fields to generate the CV.")

if __name__ == "__main__":
    main()
