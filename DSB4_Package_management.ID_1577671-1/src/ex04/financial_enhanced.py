#!/usr/bin/env python3
import sys
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def get_data(ticker, field):
    session = HTMLSession()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    response = session.get(url)
    response.html.render(sleep=2)
    html = response.html.html
    try:
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find('div', class_='rowTitle', string = field)
        if not name:
            raise Exception(f"Failed to find {field}")

        parent_name = name.find_parent('div', class_='row')

        elements = parent_name.find_all('div', class_='column')
        values = [elem.get_text(strip=True) for elem in elements[1:]]

        return (field,) + tuple(values)
    except Exception as e:
        raise Exception(f"Error: {e}")
        
    finally:
        session.close()

def main():
    if len(sys.argv)!=3:
        print('Incorrect request')
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    result = get_data(ticker, field)

    print(result)

if __name__ == '__main__':
    main()