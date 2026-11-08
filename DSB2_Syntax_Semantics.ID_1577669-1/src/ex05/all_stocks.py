import sys

def all_stocks():
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
        args = sys.argv[1].split(',')

        for arg in args:
            if arg.strip() == '':
                return
            
        TICKERS = {}
        for company, ticker in COMPANIES.items():
            TICKERS[ticker] = company
        
        for arg in args:
            arg = arg.strip()
            company = arg.capitalize()
            key = arg.upper()
            if company in COMPANIES:
                print(f"{company} stock price is {STOCKS[COMPANIES[company]]}")
            elif key in TICKERS:
                print(f"{key} is ticker symbol for {TICKERS[key]}")
            else:
                print("Unknown company")

if __name__ == '__main__':
     all_stocks()