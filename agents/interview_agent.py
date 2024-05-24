# scripts/agents/interview_agent.py

import logging
import random

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

class InterviewAgent:
    def __init__(self):
        self.interview_questions = {
            'Data Analyst': [
                "Can you explain your experience with data analysis?",
                "How do you handle large datasets?",
                "Describe a challenging data analysis project you worked on.",
                # Add more data analyst questions
            ],
            'Software Engineer': [
                "What programming languages are you proficient in?",
                "Can you discuss a complex software project you've worked on?",
                "How do you approach debugging code?",
                # Add more software engineer questions
            ],
            'Marketing': [
                "Tell me about your experience with marketing campaigns.",
                "How do you measure the success of a marketing campaign?",
                "Describe a successful marketing strategy you implemented.",
                # Add more marketing questions
            ]
            # Add more job roles and corresponding questions
        }

    def conduct_interview(self, cv_data, position):
        try:
            # Retrieve interview questions based on the candidate's position
            questions = self.interview_questions.get(position, [])
            if not questions:
                logger.warning(f"No predefined questions found for position: {position}")
                return

            logger.info(f"Starting the interview for {position}:")
            for question in questions:
                logger.info(f"Question: {question}")
                # Simulate the candidate's response
                candidate_response = self.generate_candidate_response(question)
                logger.info(f"Candidate's Response: {candidate_response}")
            logger.info("Interview completed.")
        except Exception as e:
            logger.error(f"Error conducting interview: {e}")

    def generate_candidate_response(self, question):
        # Generate a simulated candidate response
        response_templates = [
            "I believe {question} is an important aspect of my role as a {position}. In my previous experience, I...",
            "Great question! When it comes to {question}, I usually approach it by...",
            "That's an interesting question. In my current position, I've encountered similar situations where...",
        ]
        return random.choice(response_templates).format(question=question, position="Software Engineer")
