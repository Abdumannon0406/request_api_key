import requests

API_KEY = "78e705ad8ad443348d00e29d1083a4c8"


def get_random_name(nameType:str, quantity: int):
    """
    Make a GET request to the Randommer API to get a random name.

    This function should:
    - Send a GET request to: https://randommer.io/api/Name
    - With parameter nameType and quantity
    - nameType = one of these ("firstname" "surname" "fullname")
    - quantity = number of names
    - Include the API key in the X-Api-Key header
    - Print the random name from the response
    """
    headers = {"X-Api-Key":API_KEY}
    params = {"nameType":nameType,
              "quantity":quantity
              }
    r = requests.get("https://randommer.io/api/Name",headers=headers,params=params)
    print(r.text)


get_random_name("firstname",10)