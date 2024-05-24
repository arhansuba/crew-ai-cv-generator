# agents/__init__.py

# Import all agent modules here so they can be accessed as package attributes
from .interview_agent import InterviewAgent
from .resume_agent import ResumeAgent
from .feedback_agent import FeedbackAgent
from .cover_letter_agent import CoverLetterAgent
from .cv_evaluation_agent import CvEvaluationAgent

__all__ = ["InterviewAgent", "ResumeAgent", "FeedbackAgent", "CoverLetterAgent", "CvEvaluationAgent"]