import streamlit as st
import os

# Function to list all templates in a directory
def list_templates(directory):
    templates = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            templates.append(os.path.join(directory, filename))
    return templates

# Main function
def main():
    st.title("Template Gallery")

    # Sidebar options
    st.sidebar.header("Options")
    template_dir = st.sidebar.text_input("Template Directory", "./templates")
    refresh_button = st.sidebar.button("Refresh")

    # List templates in the directory
    if refresh_button:
        templates = list_templates(template_dir)

        if templates:
            st.sidebar.success(f"Found {len(templates)} templates.")
        else:
            st.sidebar.error("No templates found.")

        # Display template names
        st.subheader("Available Templates")
        for template in templates:
            st.write(os.path.basename(template))

    # Display selected template
    selected_template = st.selectbox("Select Template", templates, index=0 if templates else None)
    if selected_template:
        with open(selected_template, "r") as f:
            template_content = f.read()
            st.subheader("Template Preview")
            st.code(template_content, language="html")

if __name__ == "__main__":
    main()
