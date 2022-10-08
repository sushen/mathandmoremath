"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/
"""
from pprint import pprint

import requests

import json

url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))


previous_days = 7

seven_days_ago_price = json_data['data'][-previous_days]['priceUsd']
print(f"Seven Days Ago Price : {seven_days_ago_price}")

today_price = json_data['data'][-1]['priceUsd']
print(f"Today Price : {today_price}")

print("Write your code below 'VVVVVV'")

seven_days_ago_price = float(seven_days_ago_price)
today_price= float(today_price)
different = (today_price - seven_days_ago_price)
percentage = ((different*100)/seven_days_ago_price)
print(f'price up and down percentage: {percentage} %')

"""
what is the difference of 45 days ago price to 90 days ago price
"""
# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))


previous_days = 90

ninety_five_ago_price = json_data['data'][-previous_days]['priceUsd']
print(f"nient- five days ago price : {ninety_five_ago_price}")

forty_five_ago_price = json_data['data'][-46]['priceUsd']
print(f"forty-five days ago price : {forty_five_ago_price}")
ninety_five_ago_price = float(ninety_five_ago_price)
forty_five_ago_price = float(forty_five_ago_price)
different =  (forty_five_ago_price - ninety_five_ago_price)
percentage_two = ((different * 100)/ninety_five_ago_price)
print(f'price between 45 and 90 up and down percentage: {percentage_two} %')
