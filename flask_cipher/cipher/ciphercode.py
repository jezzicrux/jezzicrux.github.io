def cipher_code():
    code=[]
    get_message()
    get_key()
    make_code()

def get_message():
    print ("Please enter your message.")
    message = input(">>")
    code = list(str.lower(message))
    return code

def get_key():
    print ("Please enter your key")
    key = int(input(">>"))
    if key < 27:
        make_code()
    else:
        print("WRONG KEY!")
        get_key()
    return key

def make_code():
    letters = list('abcdefghijklmnopqrstuvwxyz')
    new_message=code
    for q in range (0,len(code)):
        i = letters.index(code[q])
        if code[q] == letters[i]:
            new_index=i+key
            new_message[q] = letters[new_index]
        else:
            pass
        print ("".join(new_message))

cipher_code()
