class Must_Read:
    def print():
        with open('data.csv', 'r') as f:
            print(f.read())

if __name__ == '__main__':
    Must_Read.print()