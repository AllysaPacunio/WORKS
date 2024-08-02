from Inventory import  Product_Inventory
from search_details import Cart
import os

class Customer_Cart:
  remaining_unit= {}
  itm= []
  total_sum= 0
  count= 0
    
  @staticmethod
  def cart():
    os.system('clear')
    print('\n------------------------------\n')
    print('PROCESSING....')
    print('\nScanning items in cart.... ')
    
  @staticmethod
  def punch_item():
    print('\nPunching items....\n')
    print('\n------------------------------\n')
 
  def item_in_cart(self,price):
    self.itm.append(price)
   
  @staticmethod
  def pyment():
    payment = 0

    total= sum(Customer_Cart.itm)
    print(f'\nSUB-TOTAL            {total} ')
    Customer_Cart.total_sum= total
    
    while payment < Customer_Cart.total_sum:
      payment= int(input(f'PAYMENT:             '))
      
    Customer_Cart.count += 1
    chnge= int(payment) - int(Customer_Cart.total_sum)
    print(f'CHANGE:              {chnge}')
    
    pd= Product_Inventory()
    data= pd.get_record()
    details= data['Transac_Number']= Customer_Cart.count
    pd.save()

    crt= Cart()
    to_update_unit= crt.access_dictionary()
    print(to_update)

    for code, quantity in to_update_unit.items():
      inventory_unit= crt.get_unit(code)
      new_update= inventory_unit-quantity
      
      if  new_update == 0:
        del data['Product'][code]
        pd.save()
      
      else:
        data['Product'][code]['Unit']= new_update
        pd.save()
          
    counting= crt.get_transacNumber()

    print(f'\nTRANSACTION COMPLETE: RECEIPT NO. {counting}')      

  @staticmethod
  def check_out():
    Customer_Cart.cart()
    Customer_Cart.punch_item()
    Customer_Cart.pyment()
    

    

