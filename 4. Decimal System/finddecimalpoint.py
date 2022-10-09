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

# print("Write your code below 'VVVVVV' \n")

seven_days_ago_price = float(seven_days_ago_price)
today_price= float(today_price)
different = (today_price - seven_days_ago_price)
percentage = ((different*100)/seven_days_ago_price)
print(f'price up and down percentage: {percentage} % \n')

"""
what is the difference of 45 days ago price to 90 days ago price
"""
# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))


previous_days = int(input("Enter previous days: "))
last_days = int(input("Enter last  days: "))

previous_price = json_data['data'][-previous_days]['priceUsd']
print(f"{previous_days} days ago price : {previous_price}")

last_price = json_data['data'][-last_days]['priceUsd']
print(f"{last_days} ago price : {last_price}")

previous_price = float(previous_price)
last_price = float(last_price)

different =  (last_price - previous_price)
percentage_two = ((different * 100)/previous_price)
print(f'price between {previous_days} and {last_days} days up and down percentage is: {percentage_two} %')
print("\n")

"""
The average of last ten days price.
"""
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))


today_price = (float(json_data['data'][-1]['priceUsd']))
two_days_ago_price = (float(json_data['data'][-2]['priceUsd']))
three_days_ago_price = (float(json_data['data'][-3]['priceUsd']))
four_days_ago_price = (float(json_data['data'][-4]['priceUsd']))
five_days_ago_price = (float(json_data['data'][-5]['priceUsd']))
six_days_ago_price = (float(json_data['data'][-6]['priceUsd']))
seven_days_ago_price = (float(json_data['data'][-7]['priceUsd']))
eight_days_ago_price = (float(json_data['data'][-8]['priceUsd']))
nine_days_ago_price = (float(json_data['data'][-9]['priceUsd']))
ten_days_ago_price = (float(json_data['data'][-10]['priceUsd']))

sum = (today_price + two_days_ago_price + three_days_ago_price + four_days_ago_price + five_days_ago_price + six_days_ago_price + seven_days_ago_price + eight_days_ago_price + nine_days_ago_price + ten_days_ago_price)
average = sum/10
print(f'The average of the previous ten days prise is: {average}')
