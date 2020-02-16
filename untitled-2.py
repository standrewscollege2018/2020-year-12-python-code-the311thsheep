# even or odd

def even_or_odd(num):
    if num // 2 == 0:
        return "even"
    elif num // 2 == 1:
        return "odd"
    
while True:
    num = int(input("enter a number"))
    print ("that number is ", even_or_odd(num))