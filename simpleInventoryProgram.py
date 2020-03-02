def main():
    unitPrice = float(input('Please enter the unit price of the item. $'))
    quantityOfItem = int(input('Please enter the quantity of the item in stock. ' ))
    inventoryValue = unitPrice * quantityOfItem
    print('The inventory value of the item is $', format(inventoryValue,',''.2f'),sep='')
main()
 
