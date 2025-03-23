import re

def extract_emails(text):
     e
    emails = re.findall(email_pattern, text)
    return emails


def validate_date(date_str):
    if re.match(date_pattern, date_str):
        return True
    return False

def replace_word_in_string(text, old_word, new_word):
    """Replace all occurrences of a word with another word in a string using regex."""
    # Use \b to match whole words only
    pattern = r'\b' + re.escape(old_word) + r'\b'
    replaced_text = re.sub(pattern, new_word, text)
    return replaced_text

def main():
    # Example text for email extraction
    text_with_emails = """
    
    emails = extract_emails(text_with_emails)
    print("Extracted emails:", emails)

    # Example date validation
    date_to_validate = "2023-10-05"
    is_valid