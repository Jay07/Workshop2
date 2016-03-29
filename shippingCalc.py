
itemNo=int(input('Number of items:'))

while itemNo<=0:
    print('Invalid number of items!')
    itemNo=int(input('Number of items:'))

costPerItem=float(input('Shipping cost per item:'))

total=itemNo*costPerItem

if total>100:
    total-=(total*10/100)
print('Total shipping cost:${:,.2f}'.format(total))