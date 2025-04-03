import re

# Task I: Extract all email addresses from a given text
def extract_email_addresses(text):
    # Regular expression for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

# Task II: Validate a date in the format "YYYY-MM-DD"
def validate_date(date):
    # Regular expression for validating a date in the format "YYYY-MM-DD"
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date):
        return True
    else:
        return False

# Task III: Replace all occurrences of a word with another word in a string
def replace_word_in_text(text, old_word, new_word):
    # Regular expression for replacing words
    replaced_text = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text)
    return replaced_text

# Sample input text for testing the functions
sample_text = """
    Here are some email addresses: john.doe@example.com, alice.smith@company.org, and test123@domain.co.
    The event is scheduled for 2025-05-21.
    I need
