import time

import requests

response = requests.get("https://api.warframe.market/v1/items")
items = response.json()["payload"]["items"]
prices = ''
for item in items:
    print(item['item_name'])
    prices = prices + 'item_name=' + item['item_name'] + ','
    # try except for if item is not found

    response = requests.get('https://api.warframe.market/v1/items/' + item['url_name'] + '/statistics')
    newitems = response.json()['payload']['statistics_live']['48hours'][-1]['min_price']
    print(newitems)
    prices = prices + 'item_price=' + str(newitems) + '\n'
    time.sleep(1)
with open("Output.txt", "w") as text_file:
    text_file.write(prices)
