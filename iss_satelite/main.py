import  requests
import datetime as dt
import smtplib



def check_sunrise_sunset():
    my_lat=-0.718090
    my_lon=37.158951
    sunrise_sunset_URL="https://api.sunrise-sunset.org/json"

    my_parameters={
        "lat":my_lat,
        "lng":my_lon,
        "formatted":0
    }
    response = requests.get(url=sunrise_sunset_URL, params=my_parameters)
    response.raise_for_status()
    data = response.json()
    sunset = data["results"]["sunset"]

    today_time = dt.datetime.now()
    today_time = today_time.hour
    sunset = sunset.split("T")[1].split(":")[0]
    sunrise = data["results"]["sunrise"]

    if sunset > today_time or sunrise < today_time:
        return  True
def check_iss_location():
    my_lat = -0.718090
    my_lon = 37.158951
    iss_location_url="http://api.open-notify.org/iss-now.json"

    response2=requests.get(url=iss_location_url)
    data2=response2.json()
    latitude=float(data2["iss_position"]["latitude"])
    longitude=float(data2["iss_position"]["longitude"])
    if my_lat-5 <= latitude <= my_lat+5 and my_lon-5 <= longitude <= my_lon+5:
        return True


Email="alexngotho06@gmail.com"
Password="Alex0987."


if check_iss_location() and check_sunrise_sunset():
    with smtplib.SMTP("smtp.gmail.com") as name :
        name.starttls()
        name.login(user=Email,password=Password)
        name.sendmail(from_addr=Email,to_addrs=Email,msg="subject:check the sky \n \n  the iss is near you check in the sky to see it")

