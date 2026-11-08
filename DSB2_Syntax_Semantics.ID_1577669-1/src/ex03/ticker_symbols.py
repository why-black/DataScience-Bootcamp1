import sys

def ticker_symbols():
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }


    if len(sys.argv) == 2:
        key = sys.argv[1].upper()

        TICKERS = {}
        for company, keyx in COMPANIES.items():
            TICKERS[keyx] = company

        if key in TICKERS:
            print(f"{TICKERS[key]}: {STOCKS[key]}")
        else:
            print("Unknown ticker")

if __name__ == '__main__':
     ticker_symbols()