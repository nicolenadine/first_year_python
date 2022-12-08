# By setting the email, password, server SMTP, latitude and longitude variables
# This program will check for the location of the International Space Station
# Every 60 seconds and when it is overhead from the provided location it will
# Send the specified address an email to "Look up at the sky"
# Enjoy

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = ""                   # Add your email here
MY_PASSWORD = ""                # Add your password here
SERVER_SMTP = "smtp@gmail.com"  # Change if you use provider other than gmail
MY_LAT = 37.053108              # Your latitude
MY_LONG = -122.074097           # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Check ISS location every 60 seconds
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SERVER_SMTP)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up 👆🏻\n\nThe ISS is above you in the sky."
        )





