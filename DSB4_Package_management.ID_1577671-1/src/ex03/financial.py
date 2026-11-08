#!/usr/bin/env python3
import sys
import time
#import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def get_data(ticker, field):
    time.sleep(5)

    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=firefox_options) #создание драйвера 
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}/financials"
        
        driver.get(url)
        #response = requests.get(url)
        time.sleep(10)
        if "yahoo" not in driver.current_url.lower():
            raise Exception(f"Failed to load page for {ticker}")

        # if response.status_code != 200:
        #     raise Exception(f"Ticker {ticker} not found")
        # html = response.text
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        name = soup.find('div', class_='rowTitle', string = field)
        if not name:
            raise Exception(f"Failed to find {field}")

        parent_name = name.find_parent('div', class_='row')

        elements = parent_name.find_all('div', class_='column')
        values = [elem.get_text(strip=True) for elem in elements[1:]]

        return (field,) + tuple(values)
    finally:
        driver.quit()

def main():
    if len(sys.argv)!=3:
        print('Incorrect request')
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]
    print(get_data(ticker, field))

if __name__ == '__main__':
    main()