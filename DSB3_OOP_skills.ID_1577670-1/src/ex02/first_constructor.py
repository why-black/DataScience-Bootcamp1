import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.path.exists(self.path):
            raise Exception("file not found")
        
        with open(self.path, 'r') as f:
            lines = f.readlines()

        if len(lines) < 2:
            raise Exception("need more lines in file")
    
        header = lines[0].split(',')
        if len(header)!=2:
            raise Exception("incorrect file")
        
        for line in lines[1:]:
            line = line.strip()
            values = line.split(',')

            if values!=['0','1'] and values!=['1','0']:
                raise Exception("incorrect file")
                  
        return ''.join(lines)

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("input error")
        sys.exit()
    
    path = sys.argv[1]
    obj = Research(path)

    print(obj.file_reader())