
def averageOfThree(li: list):
    if(len(li) == 3):
        return (sum(li) / 3)
    else:
        listLength = len(li)
        raise ValueError(f"List length is not 3 it is {listLength}")
    
def addNumber( li: list, num: int):
    if (len(li) > 2):
        li.append(num)
        li.pop(0)
    elif(len(li) < 2):
        li.append(num)
    else:
        listLength = len(li)
        raise ValueError(f"List length is not 3 or less; it is {listLength}")

def test(runningSet, streamList):
    average = averageOfThree(runningSet) 
    print(str(runningSet) + " Average = " + str(average))
    addNumber(runningSet, streamList[0])
    average = averageOfThree(runningSet)
    print(str(runningSet) + " Average = " + str(average))
    
if __name__ == '__main__':
    # handle the problem setup
    testList0 = []
    testList1 = [1,2,3]
    testList2 = [4,5,6,7]
    
    try:
        test(testList1, testList2)
        
    except ValueError as e:
        print(e)
    