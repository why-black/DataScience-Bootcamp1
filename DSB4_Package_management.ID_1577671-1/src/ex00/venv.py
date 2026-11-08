#!/usr/bin/env python3
import os

def main():
    path = os.environ.get('VIRTUAL_ENV')
    if path:
        print(f"Your current virtual env is {path}")
    else: print("No virtual environment is currently activated")

if __name__ == '__main__':
    main()