import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = []
    results = data['results']
    for user in results:
        user_email = user['email']
        emails.append(user_email)
    return emails
# open file
print(get_email(get_data.get_data('randomuser_data.json')))