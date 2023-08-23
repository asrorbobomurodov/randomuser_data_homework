import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    lst_users = []
    dct = {
        "first_name": 0,
        "last_name": 0,
        'phone_number': 0,
    }
    results = data['results']
    
    for user in results:
        phone = user.get('phone')
        dct['phone_number'] = phone
        
        name = user.get('name')
        
        first_name = name['first']
        dct['first_name'] = first_name
        
        last_name = name['last']
        dct['last_name'] = last_name
        
        lst_users.append(dct)
    return lst_users

print(get_users_data(get_data.get_data('randomuser_data.json')))