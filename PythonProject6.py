# First 25 pts

total = 0
print "Enter how many items you want to add:"
userInput = int(raw_input())
for x in range(userInput):
    print "Please enter a number:"
    s = int(raw_input())
    total = total + s
print "The total is...... "
print total


# Second 25 pts

totalList = []
print "Enter how many numbers you want to add"
userI = int(raw_input())
for x in range(userI):
    print "please enter a number:"
    num = int(raw_input())
    totalList.append(num)
print sum(totalList)


# Third 25 pts

def factorial(num2):
    if num2 == 0:
        return 1
    else:
        return num2 * factorial(num2-1)


#Write a program, using a for loop, that will find all the factors of a given number.
#A factor is something that will divide evenly into our given number. For example, the factors of 10 are 1, 2, 5 and 10, as each of these numbers divides evenly into 10.

print "Enter a number to get the factors"

factorList = [1,n]
def factors(n):