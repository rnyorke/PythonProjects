def sum(num, num1):
    total = num + num1
    print total
sum(1, 2)
def subtract(num2, num3):
    answer = num2 + num3
    return answer
magic = subtract(3, 2)
print magic
def subtractSmaller(num4, num5):
    if num4 < num5:
        tot = num5 - num4
        print tot
    if num5 < num4:
        tota = num4 - num5
        print tota
ha = subtractSmaller(4,5)
print ha