
def md(a):
    import hashlib
    print hashlib.md5(a).hexdigest()

def b64(bchooser,b):
    import base64
    if bchooser == 1:
        result = base64.b64decode(b)
        print result
    elif bchooser == 2:
        result = base64.b64encode(b)
        print result

def caesar(a):

    phrase = a
    shift = int(raw_input("Shift: "))

    result = ''
    for char in phrase:
        x = ord(char)

        if char.isalpha():
            x = x + shift

            offset = 65
            if char.islower():
                offset = 97

            while x < offset:
                x += 26

            while x > offset+25:
                x -= 26

            result += chr(x)

    print result

def main():
    Chooser = int(raw_input("Action: 1. Caesar; 2. 2-way BASE64; 3. MD5 sum of string;  "))
    if Chooser == 1:
        a = str(raw_input("String to shift: "))
        caesar(a)
    elif Chooser == 2:
        bchooser = int(raw_input("1. Decode or 2. Encode: "))
        b = str(raw_input("Base64(or string) input: "))
        b64(bchooser,b)
    elif Chooser == 3:
        a = str(raw_input("String to convert: "))
        md(a)
    else:
        quit()
    
if __name__ == '__main__':
    main()
