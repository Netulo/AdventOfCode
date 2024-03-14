f = open("2015/Day 1/input.txt","r")
text = f.read()
print(text.count('(') - text.count(')'))