import requests

def share_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = data['loc'].split(',')
        lat, lon = float(location[0]), float(location[1])
        print(f"Current Location: {lat}, {lon}")
        return lat, lon
    except Exception as e:
        print(f"Error sharing location: {e}")
        return None
