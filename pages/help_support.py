import streamlit as st

def display_faq():
    st.header("Frequently Asked Questions (FAQs)")
    st.markdown("""
    - **Q: How do I get started with the application?**
      A: To get started, simply navigate to the desired section and follow the instructions provided.
    
    - **Q: What should I do if I encounter an issue or bug?**
      A: Please reach out to our support team via the contact options listed below. We'll be happy to assist you.
    
   
    - **Q: How can I provide feedback or suggestions for improvement?**
      A: We welcome your feedback! Feel free to send us an email or message to inform us.
    """)


def display_contact_info():
    st.header("Contact Information")
    st.markdown("""
    **Email:** subasiarhan3@gmail.com
    
    **Telegram:** @arhansubasi
    
    **Discord:** arhansubasi
    """)


def main():
    st.title("Help & Support")

    st.write("Welcome to our help and support center! Here, you'll find resources to assist you with using our application.")

    # Display FAQ section
    display_faq()

    # Display contact information
    display_contact_info()

    
   

if __name__ == "__main__":
    main()
