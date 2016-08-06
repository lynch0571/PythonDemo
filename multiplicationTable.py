def printMultiplicationTableFunA():
    for x in range(1,10):
        for y in range(x,10):
            result=" "+str(x*y) if x*y<10 else str(x*y)
            print(str(x)+"*"+str(y)+"="+result,end="    ")
        print("")
        
def printMultiplicationTableFunB():
    for x in range(1,10):
        for y in range(1,x+1):
            result=" "+str(x*y) if x*y<10 else str(x*y)
            print(str(y)+"*"+str(x)+"="+result,end="    ")
        print("")
        
printMultiplicationTableFunB()
print("------------------------------------------------------------------------------------------")
printMultiplicationTableFunA()