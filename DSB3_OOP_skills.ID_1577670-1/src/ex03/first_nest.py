import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header = True):
        if not os.path.exists(self.path):
            raise Exception("file not found")
        
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
        def counts(self, values):
            count_l = 0
            count_r = 0

            for value in values:
                if value[0] == 0:
                    count_r += 1
                else: count_l += 1

            return count_l, count_r
        def fractions(self, count_l, count_r):
            s = count_l + count_r
            return count_l/s, count_r/s

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("input error")
        sys.exit()
    
    path = sys.argv[1]
    obj = Research(path)
    data = obj.file_reader(True)
    print(data)

    counting = Research.Calculations()
    l, r = counting.counts(data)
    print(f"{l} {r}")

    frac_l, frac_r = counting.fractions(l, r)
    print(f"{frac_l:.4f} {frac_r:.4f}")