import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f = open(filename, 'r', encoding='UTF8' )
    data = f.read()
    return json.loads(data)

# print(get_data('randomuser_data.json'))
