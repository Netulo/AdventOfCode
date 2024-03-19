f = open('2023/Day 4/test.txt', 'r')
text = f.read().split('\n')

cardsId = [1]
currentCard = 0
for line in text:
    s = 0
    line = line[line.find(':')+1:]
    nums = line.split('|')
    nums[0] = [i for i in nums[0].split(' ') if i != ''] 
    nums[1] = [i for i in nums[1].split(' ') if i != '']
    
    if len(cardsId) == currentCard:
        cardsId.append(1)
    for num in nums[0]:
        if num in nums[1]:
            s += 1
               
    if s > 0:       
        for card in range(s):
            if len(cardsId) == card+1+currentCard:
                cardsId.append(2)
            else:
                cardsId[currentCard+card+1] += cardsId[currentCard]
    currentCard += 1

    print(cardsId)
    
    #Nie działa