import langchain
import ollama
import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

class InterviewAgent:
    def __init__(self, llm, ollama_model):
        self.llm = llm
        self.ollama_model = ollama_model

    def evaluate_cv(self, cv_data, job_description):
        try:
            # Preprocess CV data
            cv_text = ''
            for key, value in cv_data.items():
                if isinstance(value, list):
                    for item in value:
                        cv_text += f'{key}: {item}\n'
                else:
                    cv_text += f'{key}: {value}\n'

            # Evaluate CV using LangChain
            cv_embedding = self.llm.encode(cv_text)
            job_description_embedding = self.llm.encode(job_description)
            similarity = self.llm.similarity(cv_embedding, job_description_embedding)
            evaluation = {'similarity': similarity}

            logger.info(f"CV evaluation successful: {evaluation}")
            return evaluation
        except Exception as e:
            logger.error(f"Error evaluating CV: {e}")
            return None

    def translate_cv(self, cv_data, target_language):
        try:
            # Translate CV data
            translated_cv = {}
            for key, value in cv_data.items():
                if isinstance(value, list):
                    translated_cv[key] = [self.ollama_model.translate(item, target_language) for item in value]
                else:
                    translated_cv[key] = self.ollama_model.translate(value, target_language)

            logger.info(f"CV translation successful: {translated_cv}")
            return translated_cv
        except Exception as e:
            logger.error(f"Error translating CV: {e}")
            return None

class ReviewAgent:
    def __init__(self, llm, ollama_model):
        self.llm = llm
        self.ollama_model = ollama_model

    def review_interview(self, interview_transcript):
        try:
            # Analyze interview transcript using LangChain
            transcript_embedding = self.llm.encode(interview_transcript)
            sentiment = self.llm.sentiment(transcript_embedding)
            review = {'sentiment': sentiment}

            logger.info(f"Interview review successful: {review}")
            return review
        except Exception as e:
            logger.error(f"Error reviewing interview: {e}")
            return None

# Example usage
llm = langchain.LLM()
ollama_model = ollama.OllamaModel()

interview_agent = InterviewAgent(llm, ollama_model)
cv_data = {
    'name': 'John Doe',
    'experience': [
        {'company': 'ABC Corp', 'title': 'Software Engineer', 'description': 'Developed XYZ feature.'},
        {'company': 'DEF Inc', 'title': 'Senior Software Engineer', 'description': 'Led the development of the LMNOP project.'}
    ]
}

translated_cv = interview_agent.translate_cv(cv_data, 'es')
evaluation = interview_agent.evaluate_cv(translated_cv, 'We are looking for a Software Engineer with experience in Python and Machine Learning.')

review_agent = ReviewAgent(llm, ollama_model)
interview_transcript = "The candidate seemed very knowledgeable and confident. They answered all questions thoroughly and provided clear explanations."

review = review_agent.review_interview(interview_transcript)