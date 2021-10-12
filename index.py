from datetime import datetime
name=input("Enter your Name")
list='''
#list of itmes
rice     Rs 49/Kg
ice      Rs 19/Kg
drink    Rs 18/Kg
water    Rs 59/Kg
chips    Rs 39/Kg
sweets   Rs 69/Kg
pine     Rs 49/Kg
apple    Rs 29/Kg
water l  Rs 47/Kg

'''
price=0
priceList=[]
totslprice=0
finalprice=0
ilist=[]
plist=[]
plist=[]

#rates for items
items={'rice':49,
'ice':19,
'dink':18,
'water':59,
'chips':39,'sweets':69,'pine':49,'apple':29,'water':47}
option=int(input("for list of items press 1"))
if option==1:
    print(list)
    for i in range(len(items)):
        inp1=int(input("if you want to buy press 1 or 2 to exit"))
        if inp1==2:
            break
        if inp1==1:
            item=input("enter your items")
            quantity=int(input("enter quantity:"))
if item in items.keys():
    price=quantity*(items[item])
    
   
print(price)