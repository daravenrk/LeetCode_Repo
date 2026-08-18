

class dPerIter():
    def __init__(self, startingValue: float, numIterations:int, multiple:float):
        self.startingValue = startingValue
        self.numIterations = numIterations
        self.multiple = multiple
        self.total = self.startingValue
        
    def calcToIterative(self, multiple) -> float:
        self.total = self.startingValue
        for i in range(0, self.numIterations):
            self.total = self.total * multiple
        return self.total 
    
if __name__ == '__main__':
    startingDollarValue = 1.00
    numIterations = 365
    multiple = 2
        
    startingDollar = dPerIter(startingDollarValue, numIterations, multiple)
    print(startingDollar.calcToIterative(startingDollar.multiple))    
        
    startingDollarValue = 1.00
    numIterations = 365
    multiple = 1.06    
        
    startingBillions = dPerIter(startingDollarValue, numIterations, multiple)
    print(startingBillions.calcToIterative(startingBillions.multiple))