def turnintolist(n1,n2,n3):
    list1 = [n1,n2,n3]
    print list1
    return list1
    
def getfirstinlist(list1):
    return list1[0]

#print as getfirstinlist([])

def getlastinlist(list2):
    return list2[len(list2) - 1]
    
#print as getlastinlist([])

def swapfirstandlast(list3):
    firstItem = getfirstinlist(list3)
    lastItem = getlastinlist(list3)
    print firstItem
    print lastItem
    list3[0] = lastItem
    list3[len(list3) - 1] = firstItem
    return list3