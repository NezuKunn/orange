import requests

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        return {
            'ip': data['ip'],
            'city': data['city'],
            'region': data['region'],
            'country': data['country'],
            'latitude': latitude,
            'longitude': longitude
        }
    except Exception as e:
        return {'error': str(e)}