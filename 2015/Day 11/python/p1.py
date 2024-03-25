f = open('2015/Day 11/test.txt')
expPass = f.readline()
expPass = 'ghijklza'

def isValid(passwd):
    if any(x in ['i', 'l', 'o'] for x in passwd):
        return False 
    
    for x in range(len(passwd)):
        if x == len(passwd)-2:
            return False
        if ord(passwd[x])-ord(passwd[x+1]) == ord(passwd[x+1])-ord(passwd[x+2]):
            break
    
    isSec = False
    for x in range(len(passwd)):
        if x == len(passwd)-1:
            return False
        if passwd[x] == passwd[x+1]: 
            if isSec:
                break
            else:
                isSec = True 
                continue
    return True

def incPasswd(password):
    password = password[:-1] + chr(ord(password[-1])+1)
    
    if ord(password[-1]) >= ord('z'):
        password = password[:-1] + 'a'
        return incPasswd(password[:-1]) + password[-1]
    else:
            return password
    

    
# print(isValid(expPass))
print(incPasswd(expPass))
# while(True):
#     expPass = incPasswd(expPass)
#     if isValid(expPass):
#         print(expPass)
#         break