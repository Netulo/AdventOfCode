with open('2023/Day 8/input.txt', 'r') as file:
    text = file.read().split('\n\n')

keys = {}
currentKeys = []
for x in text[1].split('\n'):
    key, value = x[:3], x[7:-1]
    keys[key] = value
    if x[2] == 'A':
        currentKeys.append(key)

# while not all(key[-1] == 'Z' for key in currentKeys):
for i in range(len(currentKeys)):
    turn = 0
    count = 0
    while True:
        if text[0][turn] == 'L':
            currentKeys[i] = keys[currentKeys[i]][:3]
        else:
            currentKeys[i] = keys[currentKeys[i]][-3:]

        count += 1
        if currentKeys[i][-1] == 'Z':
            currentKeys[i] = count
            break
            
        turn = (turn + 1) % len(text[0])
    

print(f"Total iterations: {currentKeys}")