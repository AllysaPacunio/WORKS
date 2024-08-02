print("Hi!\n")
print("Welcome to budgetlicious Restaurant!\n")
print("Where you can find Delicious but Budget friendly meals\n")
print("Here's our Menu:\n")
print("1. Burger - 35 Pesos\n2. Fries - 25 Pesos\n3. Spaghetti - 50 Pesos \n4. Chicken - 75 Pesos\n5. Coke - 15 Pesos\n")

print("May i take your order?\n")

menu = ["Burger","Fries","Spaghetti","Chicken","Coke"]
prices= ["35","25","50","75","15"]

total_order= []

for i in range(len(menu)):
  order= input(f"Do you want {menu[i]}? y/n?: ")

  if order == "y":
    quantity= int(input("How many?: "))
    quantity= int(quantity)
    order= prices[i]
    print(f"That would be {order} pesos.")
    print("\n")
    order= int(order)
    order= order * quantity
    total_order.append(order)
    total= sum(total_order)

print("\n")

print(f"Total is P {total:0.2f}")
print("\n")
payment = 0

while payment < total:
  payment= int(input("ENTER PAYMENT: "))

print("\n")

change = int(payment - total)

if change == 0:
  print("Thank you for your patronage!")

else:
  print(f"Your change is {change}!")
  print("Thank you for your patronage!")



    


    



    

  
    


    

     
  
  


