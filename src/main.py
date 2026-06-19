import joblib
from serial_reader import read_sensor
from email_alert import send_email
from thingspeak_upload import upload

MODEL = joblib.load("../models/accident_model.pkl")

API_KEY = "YOUR_API_KEY"

while True:

    data = read_sensor()

    if data is None:
        continue

    gas,x,y = data

    prediction = MODEL.predict([[gas,x,y]])[0]

    if prediction == 0:

        print("ACCIDENT DETECTED")

        send_email(
            "yourmail@gmail.com",
            "app_password",
            "receiver@gmail.com",
            "Accident Alert",
            f"Accident Detected!\nGas={gas}\nX={x}\nY={y}"
        )

    else:
        print("SAFE")

    upload(API_KEY,gas,x,y)