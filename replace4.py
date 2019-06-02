T = int(input())
testCases = []
for i in range(0,T):
    inp = int(input())
    testCases.append(inp)

def removeFour(num):
    stringNum = str(num)
    n1 = int(stringNum.replace('4','3'))
    n2 = num - n1
    l = []
    l.append(n1)
    l.append(n2)
    return l        
count = 1
for test in testCases:
    result = removeFour(test)
    print("Case #"+str(count)+": "+str(result[0])+" "+str(result[1]))
    count+=1;