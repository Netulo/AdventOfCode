file = open('2018/Day 5/input.txt', 'r')
text = file.read()


while True:
    temp = text
    for i in range(ord('a'), ord('z')+1):
        text = text.replace(chr(i)+chr(i).swapcase(), '') 
        text = text.replace(chr(i).swapcase()+chr(i), '')
    
    if temp == text:
        break
        
print(len(text))
            
        
            