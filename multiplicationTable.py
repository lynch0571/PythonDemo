def printMultiplicationTableFunA():
    for x in range(1,10):
        for y in range(x,10):
            print('{0}*{1}={2}'.format(x,y,'{: >2}'.format(x*y)),end="    ")
        print("")
        
def printMultiplicationTableFunB():
    for x in range(1,10):
        for y in range(1,x+1):
            print('{0}*{1}={2}'.format(y,x,'{: >2}'.format(x*y)),end="    ")
        print("")
        
printMultiplicationTableFunB()
print("------------------------------------------------------------------------------------------")
printMultiplicationTableFunA()