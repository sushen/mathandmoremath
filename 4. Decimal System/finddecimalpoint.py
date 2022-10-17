"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/
"""
from pprint import pprint

import requests

import json

# url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1664323200000&end=1664928000000"
url = "http://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text.encode('utf8'))
"""
The average of last 7 days, 25 days and 90 days price.
"""
seven_days_price = []
for i in range(1, 8):
    print(f"{i} days price is: {json_data['data'][-i]['priceUsd']}")
    seven_days_price.append(int(float(json_data['data'][-i]['priceUsd'])))
average_a =(f'The average of seven days price is: {sum(seven_days_price)/(len(seven_days_price))}\n')
print(average_a)

twenty_five_days_price = []
for i in range(1, 26):
    # print(f"{i} days price is: {json_data['data'][-i]['priceUsd']}")
    twenty_five_days_price.append(int(float(json_data['data'][-i]['priceUsd'])))
average_b =(f'The average of twenty five days price is: {sum(twenty_five_days_price)/(len(twenty_five_days_price))}\n')
print(average_b)

ninety_days_price = []
for i in range(1, 91):
    # print(f"{i} days price is: {json_data['data'][-i]['priceUsd']}")
    ninety_days_price.append(int(float(json_data['data'][-i]['priceUsd'])))
average_c =(f'The average of ninety days price is: {sum(ninety_days_price)/(len(ninety_days_price))}\n')
print(average_c)
