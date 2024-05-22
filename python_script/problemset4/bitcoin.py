# import sys
# import requests
# if len(sys.argv) == 1:
#     print("missing command-line arguement")
    
# elif len(sys.argv) == 2:
#     if type(sys.argv[1]) == int or type(sys.argv[1]) == float:
#         response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json"+sys.argv[1])
#         print(response)
        
        
        
import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except (requests.RequestException, ValueError, KeyError) as e:
        print("Error fetching Bitcoin price:", e)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number of Bitcoins.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price
    print(f"{bitcoins} Bitcoins will cost ${total_cost:.2f} at the current rate of ${bitcoin_price:.2f} per Bitcoin.")

if __name__ == "__main__":
    main()
