print ("Please enter your message.")
message = input(">>")
code = list(str.lower(message))
print ("Please enter your key")
key = int(input(">>"))
letters = list('abcdefghijklmnopqrstuvwxyz')
letters.reverse()
new_message=code
for q in range (0,len(code)):
    if new_message[q] in letters:
        i = letters.index(code[q])
        if code[q] == letters[i]:
            new_index=i+key
            new_message[q] = letters[new_index]
        else:
            pass
    else:
        pass
print ("".join(new_message))
