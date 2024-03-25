# Good
def testCaseOne(text):
    if any(x in ['i', 'l', 'o'] for x in text):
        return False
    return True

# Good
def testCaseTwo(text):
    for x in range(len(text)):
        if x == len(text)-2:
            return False
        if ord(text[x]) == ord(text[x+1])-1 and ord(text[x+1]) == ord(text[x+2])-1:
            break
    return True

# Not working properly #
def testCaseThree(text):
    pairs = dict()
    for x in range(len(text)-1):
        if text[x] == text[x+1]:
            pairs[text[x]+text[x+1]] = 1
            if x < len(text):
                text = text[:x] + '*' +text[x+1:]
        if len(pairs) == 2:
            return True
    return False        
########################

def isValid(passwd):
    if testCaseOne(passwd) and testCaseTwo(passwd) and testCaseThree(passwd):
        return True
    return False

def incPasswd(password):
    if ord(password[-1]) >= ord('z'):
        password = password[:-1] + 'a'
        return incPasswd(password[:-1]) + password[-1]
    else:
        password = password[:-1] + chr(ord(password[-1])+1)
        return password

f = open('2015/Day 11/test.txt')
expPass = f.readline()
expPass = 'cqjxjnds'

# print(testCaseOne(expPass))
# print(testCaseTwo(expPass))
# print(testCaseThree(expPass))

while(True):
    expPass = incPasswd(expPass)
    if isValid(expPass):
        print(expPass)
        break
    
    
# WRONG
# - cqkaabcc
# - 

# RIGHT -  cqjxxyzz