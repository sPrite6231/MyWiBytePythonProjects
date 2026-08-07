import time
import sys
print('Welcome to aTEAtude bakery(a boba and bakery shop)!')
print()

# Each menu item must have the same amount of characters.
# The prices can't be in strings. They must be floats or the code won't work.
menu = ['Milk Tea ','Smoothie ', 'Ice Cream', 'Cookie   ', 'Brownie  ', 'Scones   '] 
price = [8.99, 12.99, 11.00, 11.99, 10.99, 7.99]

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
        if order >= 1: # This code will only run if the user inputs a positive number 1 through 6.
            # User is shopping.
            print('You selected', menu[order-1])
            quant = int(input('How many units do you wish to purchase?\n'))
            if quant > 75:
                # This limits the inventory.
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

time.sleep(3) #This gives a pause of 3 seconds like how it takes some time to go to checkout online.
print("Shopping is complete, displaying shopping cart...")
time.sleep(2) #This gives a dramatic pause.

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

print()

next_125 = 125*(grand_tot//125+1) #This finds next multiple of 150.
gap_125 = round(next_125 - grand_tot, 2) #This finds how much more money the customer will need to pay to get the 10% discount. 

print("If you purchase for $", gap_125, "more and reach $", next_125, "you get a 10% discount.")

add_quant = []

discount_wanted = input("Would you like to take this offer? Type Y/N\n")

#.lower() will convert the user"s inputs to lower case. This way both upper and lower case inputs will be accepted.
if discount_wanted.lower() in ('y', 'yes', 'ya', 'yeah'):
    print("User wants discount offer.")
    print('You have the following options:')
    for kk in range(len(menu)):
        add_quant.append(int(gap_125//price[kk]+1))
        print(str(kk+1), '\b. Add', menu[kk], add_quant[kk], 'units.')
    
    add_on = int(input('Please indicate your preference by typing in the number of one of the options above.\n'))
    if menu[add_on-1] in shopping_cart:
        print('Previously selected item chosen')
        idx = shopping_cart.index(menu[add_on-1])
        print(idx)
        # shopping_quant[idx] == shopping_quant[idx]+quant
        shopping_quant[idx] = shopping_quant[idx] + add_quant[add_on-1]
    else:
        print('new selection')
        shopping_cart.append(menu[add_on-1])
        shopping_quant.append(add_quant[add_on-1])

elif discount_wanted.lower() in ('n', 'no', 'nah'):
    print("No discount wanted, proceeding to final checkout...")

else:
    print("This isn't a valid statement, please pick your items and try again. Type Y, yes, N, or no next time.")
    sys.exit() #This stops the code, so the user has to try again and will not be shown the shopping cart.

print("Shopping is complete, displaying shopping cart...")
time.sleep(2) #This gives a dramatic pause of 2 seconds before the shopping cart is displayed.

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

dct_rate = 10 #Discount rate in percent.\
tax_rate = 10 # Tax rate
if discount_wanted.lower() in ('y', 'yes', 'ya', 'yeah'):
    discount = round(dct_rate/100.0*grand_tot, 2)
else:
    discount = 0.0

tax = round(tax_rate/100.0*(grand_tot-discount), 2)

time.sleep(2)
print("Your total order is $",round(grand_tot, 2))
print("Your discount is $", discount)
print("Your order value after discount is $", round(grand_tot-discount, 2))
print('Tax(10%) is $', tax)

time.sleep(2)
print("Total transaction amount needed to be paid is $", round(grand_tot-discount+tax, 2))

print("Thank you for shopping at aTEAtude bakery! Enjoy your order and come back soon!")
