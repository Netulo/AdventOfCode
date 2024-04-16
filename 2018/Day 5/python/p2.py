file = open('2018/Day 5/input.txt', 'r')
text = file.read()

lowestLen = len(text)
for i in range(ord('a'), ord('z')+1):
    tempText = text
    tempText = tempText.replace(chr(i), '')
    tempText = tempText.replace(chr(i).swapcase(), '')
    while True:
        temp = tempText
        for i in range(ord('a'), ord('z')+1):
            tempText = tempText.replace(chr(i)+chr(i).swapcase(), '')
            tempText = tempText.replace(chr(i).swapcase()+chr(i), '')
        
        if temp == tempText:
            break
    if len(tempText) < lowestLen: lowestLen = len(tempText)
        
print(lowestLen)