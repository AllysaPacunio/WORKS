import json

class Product_Inventory:
  def __init__(self):
    self.__product_inventory= 'inventory.json'

    try:
      with open(self.__product_inventory, 'r') as old:
        self.__record = json.load(old)
        old.close()
    except:
      with open(self.__product_inventory, 'w') as new:
        self.__record = {'Product':{}}
        new.write(json.dumps(self.__record))
        new.close()

  @staticmethod
  def update_data():
    with open('inventory.json', 'w') as update:
       update.write(json.dumps(Product_Inventory.__record))
       update.close()
  
  def save(self):
    with open(self.__product_inventory, 'w') as update:
       update.write(json.dumps(self.__record))
       update.close()

  @staticmethod
  def change_record(recrd):
    Product_Inventory.__record= recrd
    
  def set_record(self,record):
    self.__record = record

  def get_record(self):
    return self.__record
    
  @staticmethod
  def access_record():
    with open('inventory.json', 'r') as old:
        Product_Inventory.__record = json.load(old)
        old.close()
    return Product_Inventory.__record

 
class Add_Product(Product_Inventory):
  def __init__(self,product_code,product_name, brand_name,unit,price):
    self.__product_code= product_code
    self.prdct= {'Code': self.__product_code, 'Product Name':product_name.upper(), 'Brand Name': brand_name.upper(),'Unit':unit, 'Price':price, 'Transac. Num': 0}
    super().__init__()

    data = self.get_record()
    if data['Product'] == {}:
      data['Product'][self.__product_code] = self.prdct
      self.set_record(data)
      self.save()
    else:
      try:
        data['Product'][self.__product_code]
        
      except:
        data['Product'][self.__product_code] = self.prdct
        self.set_record(data)
        self.save()


