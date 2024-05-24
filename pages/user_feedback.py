import os
import streamlit as st
import pandas as pd
import datetime

# Function to save feedback to a CSV file
def save_feedback(name, email, feedback):
    feedback_data = {
        "Name": [name],
        "Email": [email],
        "Feedback": [feedback],
        "Timestamp": [datetime.datetime.now()]
    }
    feedback_df = pd.DataFrame(feedback_data)
    feedback_df.to_csv("feedback.csv", mode="a", header=not os.path.exists("feedback.csv"), index=False)

# Main function
def main():
    st.title("Feedback Form")

    # Get user feedback
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback = st.text_area("Feedback")
    submit_button = st.button("Submit")

    # Save feedback on submit
    if submit_button:
        if name and feedback:
            save_feedback(name, email, feedback)
            st.success("Feedback submitted successfully!")
        else:
            st.error("Name and feedback fields are required.")

if __name__ == "__main__":
    main()
