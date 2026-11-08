import sys

def letter_starter():
    if len(sys.argv)!=2:
        return
    email = sys.argv[1]

    with open('employees.tsv', 'r') as f:
        next(f)
        
        for line in f:
            names = line.strip().split('\t')
            if names[2] == email:
                name = line.split('\t')[0]
                print(f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")

if __name__ == '__main__':
    letter_starter()