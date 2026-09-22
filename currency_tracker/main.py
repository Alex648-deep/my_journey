import requests
import smtplib

my_api = "d2ad899c436800963e3f2817"
my_email="alexngotho06@gmail.com"
my_password="Alex1234.?"
result =""


response=requests.get(url=f"https://v6.exchangerate-api.com/v6/{my_api}/latest/KES")

answer=response.json()

with open("text.txt") as datas:
        data=datas.readlines()
        old_USA=float(data[0].strip())
        old_United_Arab_Emirates =float(data[1].strip())
        old_United_Kingdom = float(data[2].strip())
        old_Qatar = float(data[3].strip())
        old_Tanzania = float(data[4].strip())





new_USA = answer["conversion_rates"]["USD"]
new_United_Arab_Emirates = answer["conversion_rates"]["AED"]
new_United_Kingdom = answer["conversion_rates"]["GBP"]
new_Qatar = answer["conversion_rates"]["QAR"]
new_Tanzania = answer["conversion_rates"]["TZS"]



def usa_function():
    if new_USA > old_USA:
        results=new_USA-old_USA
        global  result
        result = f"usa raised by {results} "


def united_kingdom_function():
    if new_United_Kingdom > old_United_Kingdom:
        results=new_United_Kingdom-old_United_Kingdom
        global result
        result = f"united_kingdom raised by {results} "



def united_arab_emirates_function():
    if new_United_Arab_Emirates > old_United_Arab_Emirates:
        results=new_United_Arab_Emirates-old_United_Arab_Emirates
        global result
        result = f"united_arab_emirates raised by {results} "



def qatar_function():
    if new_Qatar >old_Qatar:
        results=new_Qatar-old_Qatar
        global result
        result = f"qatar raised by {results} "



def tanzania_function():
    if new_Tanzania > old_Tanzania:
        results = new_Tanzania - old_Tanzania
        global result
        result=f"tanzania raised by {results} "

usa_function()
united_kingdom_function()
united_arab_emirates_function()
qatar_function()
tanzania_function()


with smtplib.SMTP("Smtp.gmail.com") as name:
    name.starttls()
    name.login(user=my_email,password=my_password)
    name.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"subject:THERE IS A HIGH RAISE IN CURRENCY \n \n {result}")







