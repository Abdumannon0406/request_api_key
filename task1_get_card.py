import requests

API_KEY = "78e705ad8ad443348d00e29d1083a4c8"


def get_random_card():
    """
    Make a GET request to the Randommer API to get a random card.

    This function should:
    - Send a GET request to: https://randommer.io/api/Card
    - Include the API key in the X-Api-Key header
    - Print the response JSON containing card information
    
    """
    headers ={ "X-Api-Key": API_KEY }
    r = requests.get("https://randommer.io/api/Card",headers=headers)

    print(r.text)

get_random_card()