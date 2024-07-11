import requests

def get_main_data(equipid):
    return requests.get(f"https://api.olhar.media/?getvideos&equipid={equipid}").json()