"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/

"""
from pprint import pprint

import requests

import json

# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
# url = "http://api.coincap.io/v2/assets/ethereum/history?interval=d1"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))

# pprint(json_data['data'])

previous_days = 7

seven_days_ago_price = json_data['data'][-previous_days]['priceUsd']
# print(f"Seven Days Ago Price : {seven_days_ago_price}")

today_price = json_data['data'][-1]['priceUsd']
# print(f"Today Price : {today_price}")

# print("Write your code below 'VVVVVV'")
price_list = []
for price in json_data['data']:
    # print(price)
    # print(price['priceUsd'])
    price_list.append(int(float(price['priceUsd'])))

# print(price_list)


for btc_price in price_list:
    # print(len(price_list))
    print(price_list[len(price_list)-1])
    # print(btc_price)



