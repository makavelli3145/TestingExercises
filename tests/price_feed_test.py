from unittest import mock

import app

def test_fetch_current_price(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        def json(self):
            return self.json_data

    def mock_get(url, headers=None, params=None):
        # TODO: check if the symbol is valid, if not return an invalid data response
        valid_symbols = ['BTCUSD', 'ETHUSD', 'ADAUSD', 'LINKUSD']

        requested_symbol = url.split('/')[-1]

        if requested_symbol in valid_symbols:
            if "https://api.example.com/price/" in url:
                return MockResponse({"price": 100.0}, 200)