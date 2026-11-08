import sys

def stock_prices():
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
        temp = sys.argv[1]
        key = temp.capitalize()
        if key in COMPANIES:
            value = COMPANIES[key]
            res = STOCKS[value]
            print(res)
        else:
            print("Unknown company")

if __name__ == '__main__':
     stock_prices() 