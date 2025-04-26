import re

def clean_email(raw: str) -> str:
    """
    Basic cleanup: strip unwanted whitespace, ensure proper formatting.
    """
    # Remove extraneous newlines
    email = re.sub(r"\n{2,}", "\n\n", raw.strip())
    return email