#!/usr/bin/env python3

import os
import sys

def check_virt():
    if 'tricksts' not in os.environ.get('VIRTUAL_ENV', ''):
        raise Exception("Error: Run this script in the 'tricksts' virtual environment!")

def use_command(command):
    flag = os.system(command)
    if flag != 0:
        sys.exit(f"command failed: {command}")

def main():
    check_virt()
    use_command(f"{sys.executable} -m pip install -r requirements.txt")
    with os.popen(f"{sys.executable} -m pip freeze") as f:
        libraries = f.read()
    print(libraries.strip())
    with open("requirements.txt", 'w') as f:
        f.write(libraries)

if __name__ == '__main__':
    main()