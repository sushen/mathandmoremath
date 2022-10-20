"""
Gather possible decimal point
Market Forcats : https://coincap.io/assets/bitcoin
Api Documentation : https://docs.coincap.io/
"""

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


def all_data(json_data):
    price_list = []
    for price in json_data:
        price_list.append(int(float(price['priceUsd'])))
    print(price_list)
    return price_list


price_list = all_data(json_data['data'])


def day_data(price_list, days):
    for btc_price in range(days):
        # print(len(price_list))
        print(price_list[len(price_list)-1-btc_price])
        print(-1-btc_price)
        # print(btc_price)

day_data(price_list, 7)

i = 1


# def appended():
#     x = (seven_days_price.append(int(float(json_data['data'][-i]['priceUsd']))))
#     return x


def average(a):
    seven_days_price = []
    for i in range(1, 8):
        # appended()
        seven_days_price.append(int(float(json_data['data'][-i]['priceUsd'])))
    y = (f'Day {a} to previous seven days price average is: {sum(seven_days_price) / (len(seven_days_price))}\n')
    print(y)
    return sum(seven_days_price) / (len(seven_days_price))

# average(1)
# average(2)
# average(3)
# average(4)


# average1 = average(2, 9)
# print(average1)
#
#
# average1 = average(3, 10)
# print(average1)
#
# average1 = average(4, 11)
# print(average1)
