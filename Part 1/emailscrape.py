def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    
    local_part, domain = email.split("@", 1)
    
    if not local_part or not domain:
        return False
    
    if "." not in domain:
        return False
    
    domain_name, extension = domain.rsplit(".", 1)
    
    if not domain_name or not extension:
        return False
    
    return True

def read_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        emails = file.readlines()
    return [email.strip() for email in emails]

def validate_emails(file_path):
    emails = read_emails_from_file(file_path)
    valid_emails = set()
    invalid_emails = set()

    for email in emails:
        if is_valid_email(email):
            valid_emails.add(email)
        else:
            invalid_emails.add(email)

    print("Valid Emails:")
    for email in valid_emails:
        print(email)

    print("\nInvalid Emails:")
    for email in invalid_emails:
        print(email)

# Example usage
file_path = 'emails.txt'  # Replace with your file path
validate_emails(file_path)