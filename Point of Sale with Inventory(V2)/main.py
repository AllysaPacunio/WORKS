from storingdata import StoreAccount, User
from POS_command import Command
from Inventory import Product_Inventory, Add_Product
from search_details import Cart
from cashier import Customer_Cart
from show_header import Iterator
import os

class Portal:
  greet_name= {}
  prd_cd= []
  how_many= []
  
  @staticmethod
  def show_login():
    Portal.UserName= input('\nUsername: ')
    Portal.PassWord= input('Password: ')

    Portal.owner = StoreAccount.access_record()
    user_info = Portal.owner.get('Account', {}).get(Portal.PassWord, None)
    
    if user_info and user_info.get('Username') == Portal.UserName:
      Portal.greet_name['Name']= (user_info.get('Username'))
      os.system('clear')
      Portal.menu()  
    
    else:
      print('\nInvalid login,credentials.Forgot your password? contact your admin\n')      
      Portal.signup_error()
  
  @staticmethod      
  def show_signup():
    print('CREATE AN ACCOUNT')

    usern= input('Username: ')
    fullnme= input('Full Name: ')
    role= input('Role (ADMIN/CASHIER): ')
    
    paswrd= input('Password: ')
    
    while True:
      retype= input('Re-type Password: ')
      
      if retype != paswrd:
        True  
      
      else:
        print('\nYour account has been created. You may now login.\n')
        Portal.acct_owner = User(usern,paswrd,fullnme,role)
        Portal.mainmenu()
        break

  @staticmethod
  def Exit():
    os.system('clear')
    return Portal.mainmenu()

  @staticmethod
  def mainmenu():
    os.system('clear')
    Cart.d= {}
    Portal.prd_cd= []
    Portal.how_many= []
    Customer_Cart.itm= []
    print('WELCOME TO POINT-OF-SALES v2\n')
    print('What do you want to do?\n')
    print('[1] Login')
    print('[2] Signup')
    print('[3] Exit')

    while True:
      chosenNumber = int(input('\nEnter: '))
      if chosenNumber == 1:
        os.system('clear')
        Portal.show_login()
        break
        
      elif chosenNumber == 2:
        os.system('clear')
        Portal.show_signup()
        break

      elif chosenNumber == 3:
        Portal.Exit()
        
      else:
        print('Invalid Number\n')

  @staticmethod
  def signup_error():
    print('\n[1] Log-in Again')
    print('[2] Exit')

    do= int(input('\nEnter: '))

    while True:
      if do == 1:
        Portal.show_login()
        break
      
      elif do == 2:
        Portal.Exit()
        break
      
      else:
        print('Invalid number\n')
    

  @staticmethod
  def get_name():
    a= Portal.greet_name['Name']
    return a
 
  @staticmethod
  def call():
    cmd= Command(Portal.SayWelcome,Portal.get_name())
    cmd()

  @staticmethod
  def SayWelcome(name):
    print(f"Welcome, {name}!")
    
  @staticmethod
  def asking():
    
    ask= str(input('Do you want to add another product? (y/n): ' ))
    
    if ask == 'y':
      Portal.add_product()
      
    else:
      Portal.menu()
    
  @staticmethod
  def add_product():
    os.system('clear')
    print('\nADD NEW PRODUCT')
    cod= str(input('\nProduct Code: '))
    pname= input('Product Name: ')
    bname= input('Brand Name: ')
    unt= int(input('Unit: '))
    price= int(input('Price (PHP): '))

    Portal.add_inventory = Add_Product(cod,pname,bname,unt,price)
    print('\nNew product was added to inventory\n')
    Portal.asking()
    
  def remove_product(self):
    os.system('clear')
    sub_item= Cart()
    product_details= Product_Inventory()
    data= product_details.get_record()
    
    print('\nREMOVE PRODUCT\n')
    remove_quanti= input('Product Code: ')
    
    less= sub_item.get_Productname(remove_quanti)
    brnd= sub_item.get_Brandname(remove_quanti)
    p_unit= sub_item.get_unit(remove_quanti) 
    p_price= sub_item.get_price(remove_quanti)
    
    print(f'\nProduct Name: {less} ')
    print(f'Brand Name: {brnd}')
    print(f'Unit: {p_unit}')
    print(f'Price (PHP): {p_price}')

    while True:
      quanti_remove= int(input('\nHow many items you want to remove? '))
      
      if quanti_remove > p_unit:
        True  
        print('\nInput exceeded the units available. Enter again. ')
      
      else:
        remaining_unit= p_unit - quanti_remove
        
        if remaining_unit == 0:
          del data['Product'][remove_quanti]
          product_details.save()
          
          ask_first= Portal()
          ask_first.remove_again()
          
        else:
          data['Product'][remove_quanti]['Unit']= remaining_unit
          product_details.save()
          
          ask_first= Portal()
          ask_first.remove_again()

    
  def remove_again(self):
    remove= Portal()
    another_remove= input('\nRemove another product? y/n?')

    if another_remove == 'y':
      remove.remove_product()
      
    else:
      remove.Inventory_options()
        
        
  @staticmethod  
  def Inventory_options():
    os.system('clear')
    iter= Iterator('CODE', 'NAME', 'BRAND', 'UNIT', 'PRICE')
    first_row= next(iter)
    second_row= next(iter)
    third_row= next(iter)
    fourth_row= next(iter)
    fifth_row= next(iter)
      
    print(f' {first_row}         {second_row}          {third_row}        {fourth_row}      {fifth_row}\n')
      
    product_invent= Product_Inventory()
    data= product_invent.get_record()
    details= data['Product']

    for key,value in details.items():
      # print(value)
      for i in range(len(value)):
        name= value.get('Product Name')
        brand_n= value.get('Brand Name')
        unit= value.get('Unit')
        price= value.get('Price')
        print(f' {key}     {name}       {brand_n}       {unit}       {price}')
        break
        
    print('\nOPTIONS')
    print('[1] Add Product')
    print('[2] Remove Product')
    print('[3] Back')

    chosen_option= int(input('\nEnter: '))

    while True:
      if chosen_option == 1:
        Portal.add_product()
        break
        
      elif chosen_option == 2:
         minus_product= Portal()
         minus_product.remove_product()
      
      elif chosen_option == 3:
        os.system('clear')
        Portal.menu()
        break

      else:
        print('Invalid number\n')

  @staticmethod
  def grand_total():
    Customer_Cart.check_out()
    input('\n[Press ENTER to continue]')
    Portal.mainmenu()
    

  @staticmethod
  def details_list():
    customersCart = Cart()

    for i in range(len(Portal.prd_cd)):
      for i in range(len(Portal.how_many)):
        cd= customersCart.get_Code(Portal.prd_cd[i])
        pd= customersCart.get_Productname(Portal.prd_cd[i])
        bn= customersCart.get_Brandname(Portal.prd_cd[i])
        unt= Portal.how_many[i]
        prc= customersCart.get_price(Portal.prd_cd[i])
        print(f' {cd}      {pd}      {bn}        {unt}       {prc} ')
      break

        
  @staticmethod 
  def header():
    iter= Iterator('CODE', 'NAME', 'BRAND', 'UNIT', 'PRICE')
    first_row= next(iter)
    second_row= next(iter)
    third_row= next(iter)
    fourth_row= next(iter)
    fifth_row= next(iter)

    print(f' {first_row}         {second_row}          {third_row}        {fourth_row}      {fifth_row}\n')
    
    Portal.details_list()
    Portal.newCustomer_Option()
    
  @staticmethod
  def newCustomer_Option():
    new_custo= ''
    c_cart= Cart()
    custo_cart= Customer_Cart()
    
    while True:
      new_custo = str(input("\nEnter Code:"))
      
      if new_custo != '':
        True
        quantity= str(input('More than 1 quantity? y/n? '))

        if quantity == 'y':
          hmany= int(input('Quantity: '))
          stock= c_cart.get_unit(new_custo)

          
          if hmany > stock:
            print(f'\nInput exceeded the total number of units available. Only {stock} units available.Enter again. ')
            Portal.newCustomer_Option()
            
          else:
            Portal.how_many.append(hmany)
            added= c_cart.get_Productname(new_custo)
            prdct_price= c_cart.get_price(new_custo)
            ttal= prdct_price * hmany
            custo_cart.item_in_cart(ttal)
            Portal.prd_cd.append(new_custo)
            c_cart.get_dictionary(new_custo, hmany)
            os.system('clear')
            print(f'{added} was added to cart!\n')
    
            Portal.header()
        
        else:
          hmany= 1
          Portal.how_many.append(hmany)
          added= c_cart.get_Productname(new_custo)
          prdct_price1= c_cart.get_price(new_custo)
          custo_cart.item_in_cart(prdct_price1)
          Portal.prd_cd.append(new_custo)
          c_cart.get_dictionary(new_custo, hmany)
          os.system('clear')
          print(f'{added} was added to cart!\n')
          Portal.header()
          
              
      else:
        Portal.grand_total()
      
    
  @staticmethod
  def menu():
    os.system('clear')
    Portal.call()

    print('\n[1] New Customer')
    print('[2] Inventory')
    print('[3] Logout\n')

    choose= int(input('Enter: '))

    while True:
      if choose == 1:
        os.system('clear')
        Portal.header()
        break
      
      elif choose == 2:
        Portal.Inventory_options()
        break

      elif choose == 3:
        os.system('clear')
        Portal.mainmenu()
        break

      else:
        print('Invalid number\n')
        break

  



Portal.mainmenu()








