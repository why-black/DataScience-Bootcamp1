import sys

def caesar():
    if len(sys.argv)!=4:
        return
    mode = sys.argv[1]
    shift = int(sys.argv[3])
    text = sys.argv[2]
    res = ""
        
    for ch in text:
        if ch.isalpha() and not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
            raise Exception("The script does not support your language yet.")
        
        if ch.isalpha():
            if ch.isupper():
                base = 'A'
            else:
                base = 'a'

            if mode == 'encode':
                ch = chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
            elif mode == 'decode':
                ch = chr((ord(ch) - ord(base) - shift) % 26 + ord(base))
        res = res + ch
    print(res)

if __name__ == '__main__':
    caesar()