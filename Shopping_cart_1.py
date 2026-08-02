import time

print('Welcome to aTEAtude bakery(a boba and bakery shop)!')
print()

menu = ['Milk Tea ','Smoothie ', 'Ice Cream', 'Cookie   ', 'Brownie  ', 'Scones   ']
price = [14.99, 16.99, 9.99, 11.99, 13.99, 15.99]

print("ITEM", "UNIT PRICE, excl. Tax", sep = '\t\t\t\t')
for kk in range(len(menu)):
    print(str(kk+1)+'. '+menu[kk], "$", price[kk], sep ='\t\t\t')

print()  

shopping_cart = []
shopping_quant = []

shopping_complete = 0

while shopping_complete == 0:
    order = int(input("Enter 1 to 6 to select a bakery item, 7 to proceed to checkout.\n"))
    if order <= 6:
        if order >= 1:
            # User is shopping.
            print('You selected', menu[order-1])
            quant = int(input('How many units do you wish to purchase?\n'))
            if quant > 75:
                print("Sorry, we don't have that much quantity available.")
            else:
                if menu[order-1] in shopping_cart:
                    print('repeated selection')
                    idx = shopping_cart.index(menu[order-1])
                    print(idx)
                    # shopping_quant[idx] == shopping_quant[idx]+quant
                    shopping_quant[idx] += quant

                
                else:
                    print('new selection')
                    shopping_cart.append(menu[order-1])
                    shopping_quant.append(quant)
        else:
            print("This is an invalid input.")
    elif order == 7:
        print()
        print('Proceeding to checkout...')
        shopping_complete = 1
    else:
        print("This is not a valid input.")

print()

time.sleep(3)
print("Shopping is complete, displaying shopping cart...")
time.sleep(2)

print()

grand_tot = 0.0

print('ITEM', 'QUANTITY', 'UNIT PRICE', 'TOTAL PRICE', sep = '----------------------')
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = price[idx]
    tot_price = round(unit_price * shopping_quant[kk], 2)
    grand_tot += tot_price
    print(str(shopping_cart[kk]) + "|", str(shopping_quant[kk]) + "|", "$" + str(unit_price) + "|", "$" + str(tot_price) + "|", sep = '\t\t\t')

    grand_tot = round(grand_tot, 2)

print()
print("Your total order is $",round(grand_tot, 2))
