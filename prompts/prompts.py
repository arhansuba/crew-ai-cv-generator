
from langchain.prompts import PromptTemplate

class PromptTemplates:
    """Store all prompt templates"""

    @staticmethod
    def data_analyst_template(context, question):
        return f"""
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let's think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Analyst.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            Based on the Resume, 
            Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Analyst.
            
            The questions should be in the context of the resume.
            
            There are 3 main types of questions: 
            1. Data Analysis Techniques
            2. SQL Queries
            3. Statistical Analysis
            
            Resume: 
            {context}
            
            1. Data Analysis Techniques:
            - What are the steps involved in data preprocessing?
            - Explain the difference between supervised and unsupervised learning.
            ...
            
            2. SQL Queries:
            - Write a SQL query to find the average salary of employees in a department.
            - How do you handle NULL values in SQL?
            ...
            
            3. Statistical Analysis:
            - What is hypothesis testing? Provide an example.
            - Describe the difference between correlation and causation.
            ...
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """

    @staticmethod
    def software_engineer_template(context, question):
        return f"""
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let's think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Software Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """

    @staticmethod
    def marketing_template(context, question):
        return f"""
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let's think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Marketing Associate.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
             Based on the Resume, 
            Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Marketing Associate.
            
            The questions should be in the context of the resume.
            
            There are 3 main types of questions: 
            1. Marketing Strategies
            2. Campaign Management
            3. Digital Marketing Tools
            
            Resume: 
            {context}
            
            1. Marketing Strategies:
            - How do you conduct market research for a new product launch?
            - Describe a successful marketing campaign you led.
            ...
            
            2. Campaign Management:
            - What metrics do you use to measure the success of a marketing campaign?
            - How do you segment your target audience for a marketing campaign?
            ...
            
            3. Digital Marketing Tools:
            - Have you used Google Analytics? Explain its key features.
            - How do you optimize email marketing campaigns for better engagement?
            ...
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """

    @staticmethod
    def finance_template(context, question):
         return f"""
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let's think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Finance Analyst.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
             Based on the Resume, 
            Create a guideline with the following topics for an interview to test the knowledge of the candidate on necessary skills for being a Finance Analyst.
            
            The questions should be in the context of the resume.
            
            There are 3 main types of questions: 
            1. Financial Analysis
            2. Investment Strategies
            3. Risk Management
            
            Resume: 
            {context}
            
            1. Financial Analysis:
            - How do you analyze a company's financial statements?
            - Explain the concept of financial ratios and their significance.
            ...
            
            2. Investment Strategies:
            - What factors do you consider when evaluating investment opportunities?
            - Describe your approach to portfolio management.
            ...
            
            3. Risk Management:
            - How do you assess and mitigate financial risks?
            - What is the difference between systematic and unsystematic risk?
            ...
            

            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """

def prompt_selector(position: str, prompts: PromptTemplates) -> dict:
    """Select the prompt template based on the position"""
    position = position.lower().replace(" ", "_") + "_template"
    template_function = getattr(prompts, position, None)
    if template_function:
        return {"prompt": PromptTemplate(template=template_function)}
    else:
        raise ValueError(f"Position '{position}' is not supported.")

# Additional depth for interview questions

def add_depth_to_questions(template_function, context, questions):
    """Add depth to interview questions by including subtopics and questions"""
    return template_function(context, "\n".join(questions))

# Example usage:
if __name__ == "__main__":
    # Select the position and template function
    position = "Data Analyst"
    template_function = getattr(PromptTemplates, position.lower().replace(" ", "_") + "_template")

    # Example context and questions
    context = "Sample resume context"
    background_skills_questions = ["Question 1: Describe your background in data analysis.",
                                   "Question 2: What programming languages are you proficient in?",
                                   "Question 3: Explain a challenging data analysis project you worked on."]

    # Add depth to questions
    prompt = add_depth_to_questions(template_function, context, background_skills_questions)
    print(prompt)
