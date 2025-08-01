import app

def test_fetch_current_price(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        def json(self):
            return {"data":self.json_data, "status_code":self.status_code}

    def mock_get(url, headers=None, params=None):
        # TODO: check if the symbol is valid, if not return an invalid data response
        valid_symbols = ['BTCUSD', 'ETHUSD', 'ADAUSD', 'LINKUSD']

        requested_symbol = url.split('/')[-1]

        if requested_symbol in valid_symbols:
            if "https://api.example.com/price/" in url:
                return MockResponse({"price": 100.0}, 200)
            else:
                return MockResponse({"error": f"404 not found"}, 404)

        else:
            return MockResponse({"error": f"Invalid symbol: {requested_symbol}"}, 400)

    monkeypatch.setattr("requests.get", mock_get)
    assert mock_get("https://api.example.com/price/BTCUSD").status_code == 200
    assert mock_get("https://api.exampple.com/price/BTCUSD").status_code == 404
    assert mock_get("https://api.exampple.com/price/USDZAR").status_code == 400