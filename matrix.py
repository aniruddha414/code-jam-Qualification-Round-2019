t = int(input())
testCases = []
for i in range(0,t):
    size = int(input())
    inp = input()
    testCases.append([size,inp])

def invert(moves):
    newMoves = ""
    for move in moves:
        if move == 'S':
            newMoves += 'E'
        elif move == 'E':    
            newMoves += 'S'
    return newMoves        

count = 1

for test in testCases:
    result = invert(test[1])
    print("Case #"+str(count)+": "+result)
    count+=1