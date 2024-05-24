from langchain.prompts import PromptTemplate

def prompt_selector(position: str, prompts: classmethod) -> dict:
    """Select the prompt template based on the position"""

    # Define a dictionary to map positions to prompt templates and input variables
    prompt_templates = {
        'Data Analyst': (prompts.da_template, ["context", "question"]),
        'Software Engineer': (prompts.swe_template, ["context", "question"]),
        'Marketing': (prompts.marketing_template, ["context", "question"]),
        'Finance' : (prompts.finance_template, ["context", "question"])
        # Add more positions and their corresponding templates here
    }

    # Check if the provided position is in the dictionary
    if position in prompt_templates:
        template, input_variables = prompt_templates[position]
        PROMPT = PromptTemplate(template=template, input_variables=input_variables)
        chain_type_kwargs = {"prompt": PROMPT}
    else:
        # Handle the case where the position is not found
        raise ValueError(f"Position '{position}' is not supported.")

    return chain_type_kwargs
