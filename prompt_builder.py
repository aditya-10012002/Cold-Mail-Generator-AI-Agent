PROMPT_TEMPLATE = (
    "You are an expert at writing professional cold emails.\n"
    "Write a {tone} cold email to the {role} at {company} about {purpose}.\n"
    "Keep it concise, engaging, and include a clear call to action.\n"
    "Make sure to avoid any jargon or overly technical language\n"
    "and don't add any template prefix or suffix to the email, like 'Here is the generated email' etc"
)

def build_prompt(company: str, role: str, purpose: str, tone: str = 'Formal') -> str:
    """
    Construct the prompt for the Gemini API based on user inputs.
    """
    return PROMPT_TEMPLATE.format(
        tone=tone,
        role=role,
        company=company,
        purpose=purpose
    )