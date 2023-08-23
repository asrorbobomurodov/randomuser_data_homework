import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    lst_gender = []
    
    users = {
        'Male': 0,
        'Female': 0
    }
    results = data['results']
    
    for user in  results:
        gender = user['gender']
        
        if gender == 'male':
            users['Male'] += 1
            
        if gender == 'female':
            users['Female'] += 1
            
    for item in users.items():
        lst_gender.append(item)
        
    return lst_gender

print(get_gender_users(get_data.get_data('randomuser_data.json')))