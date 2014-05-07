

print "Choose encryption: 1. Caesar; 2. BASE64"

def base64(b):
    import base64
    print "encode or decode"
    result = base64.b64decode(b)
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


Chooser = int(raw_input())
if Chooser == 1:
    a = str(raw_input("caesar encoded string: "))
    caesar(a)
elif Chooser == 2:
    b = str(raw_input("base64 string: "))
    base64(b)
    



else:
    quit()
