import sys
from random import randint
import logging
import requests

logging.basicConfig(
    filename='analytics.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Research:
    def __init__(self, path):
        logging.debug('research object created')
        self.path = path

    def file_reader(self, has_header = True):
        logging.debug('file_reader method started')
        with open(self.path, 'r') as f:
            lines = f.readlines()

        if len(lines) < 1:
            raise Exception("need more lines in file")
    
        if has_header:
            if len(lines) < 2:
                raise Exception("need more lines in file")
            header = lines[0].split(',')
            if len(header)!=2:
                raise Exception("incorrect file")

        res = []
        skip = 1 if has_header else 0
        for line in lines[skip:]:
            line = line.strip()
            values = line.split(',')

            if values!=['0','1'] and values!=['1','0']:
                raise Exception("incorrect file")
            res.append([int(values[0]), int(values[1])])
            
        logging.debug('file_reader completed')
        return res
    
    def send_telegram_message(self, success=True):
        logging.debug('send_telegram_message method started')
        if success:
            message = "The report has been successfully created"
        else:
            message = "The report hasn't been created due to an error."
        logging.debug('send_telegram_message completed')
    
class Calculations:
    def __init__(self, data):
        logging.debug('calculations object created')
        self.data = data

    def counts(self):
        logging.debug('counts method started')
        heads = 0
        tails = 0

        for value in self.data:
            if value[0] == 1:
                heads += 1
            else: 
                tails += 1

        logging.debug('counts completed: %d heads, %d tails', heads, tails)
        return heads, tails

    
    def fractions(self):
        logging.debug('fractions method started')
        count_l, count_r = self.counts()
        s = count_l + count_r
        logging.debug('fractions completed: %.2f%%, %.2f%%', count_l*100, count_r*100)
        return count_l/s, count_r/s

class Analytics(Calculations):
    def __init__(self, data):
        logging.debug('analytics object created')
        super().__init__(data)

    def predict_random(self, count):
        logging.debug('predict_random method started for %d predictions', count)
        res = []
        for i in range(count):
            if randint(0,1)==1:
                res.append([1,0])
            else: res.append([0,1])
        logging.debug('predict_random generated %d predictions', len(res))
        return res

    def predict_last(self):
        logging.debug('predict_last method started')
        logging.debug('predict_last returned: %s', self.data[-1])
        return self.data[-1]
    
    def save_file(self, data, filename, extension):
        logging.debug('save_file method started for %s.%s', filename, extension)
        with open(f"{filename}.{extension}", 'w') as f:
            f.write(data)
        logging.debug('save_file completed')