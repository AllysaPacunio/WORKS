print('The menu:\n')
print(
    'Spaghetti        50.00\nBurger           35.00\nFries            35.00\nMilk Tea         60.00\nCoffee           50.00'
)

menu = {
    'Spaghetti': 50.00,
    'Burger': 35.00,
    'Fries': 35.00,
    'Milk Tea': 60.00,
    'Coffee': 50.00
}

count = 0
total_order = []
new_menu = {}
print('\n')

for menu, price in menu.items():
  customer_order = input(f"{menu}? (y/n): ")

  if customer_order == 'n':
    count += 1

    while count == 5:
      print('\nYou did not order anything. Please try again.\n')
      break

  if customer_order == "y":
    quantity = int(input("Quantity: "))
    how_much = int(quantity * price)
    customer_order = menu
    new_menu[customer_order] = quantity
    total_order.append(how_much)
    total = sum(total_order)

another_menu = {
    'Spaghetti': 50.00,
    'Burger': 35.00,
    'Fries': 35.00,
    'Milk Tea': 60.00,
    'Coffee': 50.00
}

print('\n')
print(f"Total is P {total:0.2f}")
print('\n')
payment = int(input("Enter your payment: "))

while payment < total:
  payment = int(input("Enter your payment:"))

print('\n')
print('Here'
      's your Receipt :')
print('\n')

# start of receipt
#look_up or search operation po ito
if 'Spaghetti' in new_menu:
  aaa = new_menu['Spaghetti']
  bbb = another_menu['Spaghetti']
  ccc = int(aaa * bbb)
  print(f'Spaghetti            50.00  X  {aaa} =  {ccc:0.2f}')
else:
  print(f'Spaghetti            50.00  X  0 =   0.00')

if 'Burger' in new_menu:
  ddd = new_menu['Burger']
  eee = another_menu['Burger']
  fff = int(ddd * eee)
  print(f'Burger               35.00  X  {ddd} =  {fff:0.2f}')
else:
  print(f'Burger               35.00  X  0 =   0.00')

if 'Fries' in new_menu:
  ggg = new_menu['Fries']
  hhh = another_menu['Fries']
  iii = int(ggg * hhh)
  print(f'Fries                35.00  X  {ggg} =  {iii:0.2f}')
else:
  print(f'Fries                35.00  X  0 =   0.00')

if 'Milk Tea' in new_menu:
  jjj = new_menu['Milk Tea']
  kkk = another_menu['Milk Tea']
  lll = int(jjj * kkk)
  print(f'Milk Tea             60.00  X  {jjj} =  {lll:0.2f}')
else:
  print(f'Milk Tea             60.00  X  0 =   0.00')

if 'Coffee' in new_menu:
  mmm = new_menu['Coffee']
  nnn = another_menu['Coffee']
  ooo = int(mmm * nnn)
  print(f'Coffee               50.00  X  {mmm} =  {ooo:0.2f}')
else:
  print(f'Coffee               50.00  X  0 =   0.00')

print('--------------------------------------------')

print(f'Subtotal:                           {total:0.2f} ')

Senior = input("Senior Citizen? (y/n): ")

if Senior == 'y':
  discount = total * 0.05

else:
  discount = 0.00

print(f'Discount  (5%):                      {discount:0.2f}')

print('--------------------------------------------')

over_all = total - discount

print(f'Grand Total:                        {over_all:0.2f}')

print('--------------------------------------------')

print(f'Payment:                            {payment:0.2f}')

change = payment - total
print(f'Change:                             {change:0.2f}')

print('\n')
print('         -------- THANK YOU --------               ')
