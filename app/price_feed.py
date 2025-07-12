import requests

def fetch_current_price(symbol: str) -> float:
    response = requests.get("https://api.example.com/price/"+symbol)
    if response.status_code == 200:
        return response.json()["price"]
    else:
        return response.json()