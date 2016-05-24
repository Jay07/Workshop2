# input number of items
itemNo=int(input('Number of items:'))

# loop
while itemNo<=0:
    print('Invalid number of items!')
    itemNo=int(input('Number of items:'))

# input cost of item
costPerItem=float(input('Shipping cost per item:'))

# calculate total cost of items
total=itemNo*costPerItem

# discount
if total>100:
    total-=(total*10/100)

# print statement
print('Total shipping cost:${:,.2f}'.format(total))