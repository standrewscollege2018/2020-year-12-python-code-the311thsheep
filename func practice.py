#GST

def GST(price):
    gst = price*0.15
    return gst

while True:
    price = int(input("Enter a price: "))
    print ("the item costs $",  price, " and the GST is $", GST(price))