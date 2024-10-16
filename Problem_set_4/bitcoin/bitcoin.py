import sys
import requests
import json

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        number = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
    else:
        price = float(response.json()['bpi']['USD']['rate'].replace(',', ''))
        print(f"${number*price:,.4f}")