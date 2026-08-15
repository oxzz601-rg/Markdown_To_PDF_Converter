import re

def clean_markdown_text(text):
    # Remove any HTML tags
    text = re.sub(r'<.*?>', '', text)
    return text