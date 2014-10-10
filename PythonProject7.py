# 25 pts

loopNumber = 0
while (loopNumber <= 300):
    if loopNumber %2 == 1:
        print loopNumber
    loopNumber = loopNumber + 1
    
   
# 25 pts

list1 = [2, 3, "Hello", "haha", "CS is awesome", 17, "lol", "hello", 727, 7, 10]
x = 0
while (x <= 10):
    print list1[x]
    x = x + 1


# 50 pts

import random
rand = random.randint(0,50)

lol = True
c = 5
while(lol):
    c = c - 1
    userInput = int(raw_input())
    if userInput == rand:
        print "That's exactly right!"
        lol = False
    if userInput < rand:
        print "Too low!"
        if c == 0:
            lol = False
    if userInput > rand:
        print "Too high!"
        if c == 0:
            c = False