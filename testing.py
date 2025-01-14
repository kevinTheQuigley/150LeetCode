Input = ['add:laptop:5', 'ship:laptop:2', 'ship:laptop:4', 'add:mouse:3', 'ship:mouse:4']


storageDict = {}



def addItems(item,number):
    if item in storageDict:
        storageDict[item]+=number
        print(f"{number} " +item+ f" have been added. Total is now {storageDict[item]}")
        return True
    else:
        storageDict[item]=number
        print(f"{number} " +item+ f" have been added. Total is now {storageDict[item]}")
        return True

print(addItems("sausages",3))
print(addItems("sausages",3))

def shipItems(item,number):
    if not item in storageDict:
        print("Cant ship "+item+". It is not in stock")
        return False
    else:
        if storageDict[item]<number:
            print("Cant ship "+item+". There is not enough in stock")
            return False
        else:
            print(f"Successfully shipped {storageDict[item]} of "+item)
            storageDict[item]-=number
            return True



def takeIndividualInput(string):
    
    li = string.split(":")
    if li[0]=="add":
        valid = addItems(li[1],int(li[2]))
    elif li[0]=="ship":
        valid = shipItems(li[1],int(li[2]))
    else:
        print("Incorrect item")
    return valid

print(takeIndividualInput("add:laptop:5"))


def takeInput(inputList):
    validityList = []
    for string in inputList:
        validityList.append(takeIndividualInput(string))
    print(validityList)
    return validityList

takeInput(Input)