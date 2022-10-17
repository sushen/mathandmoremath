
"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/
"""
i = 1
def appended():
    x = (seven_days_price.append(int(float(json_data['data'][-i ]['priceUsd']))))
    return x
def average(a, b):
    for i in range(1, 8):
        appended()
    y = (f'Day {a} to previous seven days price average is: {sum(seven_days_price)/(len(seven_days_price))}\n')
    return y

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
average1 = average(1, 8)
print(average1)

seven_days_price = []
average1 = average(2, 9)
print(average1)

seven_days_price = []
average1 = average(3, 10)
print(average1)

seven_days_price = []
average1 = average(4, 11)
print(average1)




