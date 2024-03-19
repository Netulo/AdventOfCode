f = open('2023/Day 4/input.txt', 'r')
text = f.read().split('\n')

cardsId = dict()
currentCard = 1
for line in text:
    s = 0
    line = line[line.find(':')+1:]
    nums = line.split('|')
    nums[0] = [i for i in nums[0].split(' ') if i != ''] 
    nums[1] = [i for i in nums[1].split(' ') if i != '']
    
    if currentCard not in cardsId:
        cardsId[currentCard] = 1
    for num in nums[0]:
        if num in nums[1]:
            s += 1
               
    for card in range(s):
        try:
            cardsId[currentCard+card+1] += cardsId[currentCard]
        except:
            cardsId[currentCard+card+1] = cardsId[currentCard]+1
    currentCard += 1

print(sum(cardsId.values()))