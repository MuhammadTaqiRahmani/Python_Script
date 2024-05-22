import json
import requests
import sys
if len(sys.argv)!=2:
    sys.exit()
    
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json"+sys.argv[1])
# print(json.dumps(response.json(),indent=2))

obj = response.json()
for result in obj["results"]:
    print(result["trackName"])