from Inventory import Product_Inventory

class Cart:
  def get_Code(self,entered_code):
    return entered_code
  
  def get_Productname(self,entered_code):
    inventory= Product_Inventory.access_record()
    details= (inventory['Product'][entered_code])
    
    product_name= details.get('Product Name')
    return product_name

  def get_Brandname(self,entered_code):
    inventory= Product_Inventory.access_record()
    details= (inventory['Product'][entered_code])
    
    brand_name= details.get('Brand Name')
    return brand_name

  def get_unit(self,entered_code):
    inventory= Product_Inventory.access_record()
    details= (inventory['Product'][entered_code])
    
    product_unit= details.get('Unit')
    return product_unit

  def get_price(self,entered_code):
    inventory= Product_Inventory.access_record()
    details= (inventory['Product'][entered_code])
    
    product_price= details.get('Price')
    return product_price

  def get_transacNumber(self):
    inventory= Product_Inventory.access_record()
    details= inventory['Transac_Number']
    return details

  def get_dictionary(self, code, quantity):
    if self.d == {}:
      self.d[code]= quantity
      
    else:
      for key,value in self.d.items():
        if code == key:
          self.duplicate_key.append(quantity)
          new= sum(self.duplicate_key)
          new_unit= int(value) + int(new) 
          self.d[key]= new_unit
        
        else:
          self.d[code]= quantity
          break

  