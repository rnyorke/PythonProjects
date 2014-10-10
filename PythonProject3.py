def printmax(num,num1):
    if num > num1:
        print num
    elif num1 > num:
        print num1
        
def printmaxmin(num2,num3,num4):
    if num2 < num3 and num2 < num4:
        print num2
    elif num3 < num4:
        print num3
    else:
        print num4
    if num2 > num3 and num2 > num4:
        print num2
    elif num3 > num4:
        print num3
    else:
        print num4
        
def evenorodd(num5):
    if num5 % 2 == 0:
        print "Even"
    else:
        print "Odd"
        
def printmaxoflist(num, num1, num2):
    list = [num,num1,num2]
    if num > num1 and num > num2:
        print num
    elif num1 > num2:
        print num1
    else:
        print num2
    