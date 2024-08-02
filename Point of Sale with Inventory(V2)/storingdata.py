import json

class StoreAccount:
  def __init__(self):
    self.__account_storage = 'accounts.json'

    try:
      with open(self.__account_storage, 'r') as old:
        self.__record = json.load(old)
        old.close()
    except:
      with open(self.__account_storage, 'w') as new:
        self.__record = {'Account':{}}
        new.write(json.dumps(self.__record))
        new.close()

  def save(self):
    with open(self.__account_storage, 'w') as update:
       update.write(json.dumps(self.__record))
       update.close()

  def set_record(self, record):
    self.__record = record

  def get_record(self):
    return self.__record

  def get_username(self):
    acct = self.get_record()
    self.__username = acct['Account'] [self.__fullname]['Username']
    return self.__username

  def get_password(self):
    acct = self.get_record()
    self.__password= acct['Account'][self.__fullname]['Password']
    return self.__password

  @staticmethod
  def access_record():
    with open('accounts.json', 'r') as old:
        StoreAccount.__record = json.load(old)
        old.close()
    return StoreAccount.__record

class User(StoreAccount):
  def __init__(self,account_username, account_pass,fullname,role):
    self.__account_pass= account_pass
    self.user_acct= {'Username': account_username, 'Fullname': fullname.upper(), 'Role': role.upper()}
    super().__init__()
    
    data = self.get_record()
    if data['Account'] == {}:
      data['Account'][self.__account_pass] = self.user_acct
      self.set_record(data)
      self.save()
    else:
      try:
        data['Account'][self.__account_pass]
        
      except:
        data['Account'][self.__account_pass] = self.user_acct
        self.set_record(data)
        self.save()


  