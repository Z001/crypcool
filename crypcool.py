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
    Chooser = int(raw_input("Choose encryption: 1. Caesar; 2. BASE64; "))
    if Chooser == 1:
        a = str(raw_input("caesar encoded string: "))
        caesar(a)
    elif Chooser == 2:
        bchooser = int(raw_input("decode or encode: "))
        b = str(raw_input("Base64(or string) input: "))
        b64(bchooser,b)
    else:
        quit()
    
if __name__ == '__main__':
    main()
