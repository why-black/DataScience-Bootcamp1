import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header = True):
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
            
        return res
    
class Calculations:
    def __init__(self, data):
        self.data = data

    def counts(self):
        heads = 0
        tails = 0

        for value in self.data:
            if value[0] == 1:
                heads += 1
            else: 
                tails += 1
        return heads, tails

    
    def fractions(self):
        count_l, count_r = self.counts()
        s = count_l + count_r
        return count_l/s, count_r/s

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, count):
        res = []
        for i in range(count):
            if randint(0,1)==1:
                res.append([1,0])
            else: res.append([0,1])
        return res

    def predict_last(self):
        return self.data[-1]
    
    def save_file(self, data, filename, extension):
        with open(f"{filename}.{extension}", 'w') as f:
            f.write(data)