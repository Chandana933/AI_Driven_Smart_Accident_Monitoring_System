import requests

def upload(api_key,gas,x,y):

    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key":api_key,
        "field1":gas,
        "field2":x,
        "field3":y
    }

    requests.post(url,data=payload)