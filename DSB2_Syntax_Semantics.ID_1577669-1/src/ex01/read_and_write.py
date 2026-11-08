def readWrite():

    with open('ds.csv', 'r') as csv_file:
        content = csv_file.read()   

        with open('ds.tsv', 'w') as tsv_file:
            for line in content.splitlines():
                res = ""
                quotes = 0
                for c in line:
                    if c == '"':
                        quotes += 1
                        res += c
                    elif quotes % 2 == 0 and c == ',':
                        res += '\t'
                    else:
                        res += c
                tsv_file.write(res + '\n')
            
if __name__ == '__main__':
    readWrite()