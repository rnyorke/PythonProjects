print "Hello"
print "Enter your name and then two integers, one at a time"
name = raw_input()
numberone = int(raw_input())
numbertwo = int(raw_input())
print name
print numberone + numbertwo

print 'Would you like to add or subtract the two numbers? Press 1 to add, 2 to subtract'
userchoice = int(raw_input())
if userchoice == 1:
    ad = numberone + numbertwo
    print ad
if userchoice == 2:
    sub = int(numberone - numbertwo)
    print sub