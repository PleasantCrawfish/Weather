import requests
import os
from twilio.rest import Client

api_key = 'b903f9fa6a03f397b22b436fd66a7804'
MY_LAT = 19.8
MY_LNG = 109.59

account_sid = 'ACaf6628dd70cba4f4b1agqag968a2be6fa3fcf'
auth_token = 'bb33961eafae515e4592sdg09559ff2be07'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'exclude': 'minutely,current,daily',
    'appid': api_key,

}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()
hourly_weather = data['hourly']
bring_umbrella = False

for hour in range(0, 12):
    certain_hour_weather = hourly_weather[hour]
    certain_hour_conditions = certain_hour_weather['weather']
    for condition in certain_hour_conditions:
        id = condition['id']
        if id < 700:
            bring_umbrella = True
if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Ожидается дождь",
        from_='+13185586409',
        to='+79876513641'
    )
    print('message.status')
