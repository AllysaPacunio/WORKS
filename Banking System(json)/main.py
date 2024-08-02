import json
import random

class Customer:
  def __init__(self, account):
    self.__account = account + ".json"

    try:
      with open(self.__account, 'r') as db:
        self.__data = json.load(db)
        db.close()
        print('Data loaded from', self.__account)
    except:
      print('Not an existing contact')

  def get_data(self):
    return self.__data

  def set_data(self, data):
    self.__data = data

  def save(self):
    with open(self.__account, 'w') as data:
      data.write(json.dumps(self.__data))
      data.close()

class User(Customer):
  amount= 0
  account_balance= 0
  stop= True
  account_owner= {}
  ac= random.randint(100000, 1000000)

  def account_user(self,option):
    self.option = option
  
    if option == "1":
      while self.stop == True:
        data = self.get_data()
        name= input("\nEnter your Name: ")
        passwrd= input ("Enter your Password: ")

        for names, passw in data.items():
          if name == name and passwrd == str(passw[0]): 
            self.stop = False
            for a,b in data.items():
              if name in a:
                self.account_owner[name]= b[1]
                print("\nYou are now logged in....\n")
            return
          
          else:
            self.stop= True

    else:
      data = self.get_data()
      newname= input("\nEnter your Name: ")
      newpassword= input("Set Password: ")
      
      self.account_owner[newname]= self.ac
      data[newname] = [newpassword,self.ac]
      
      self.save()
      print("\nYou have successfully made an account.")

  def act_owner(self):
    return self.account_owner
     
  def deposit(self,amount,account_num):
    self.amount= amount
    self.account_num= account_num
    
    balance = int(self.amount) + int(self.account_balance)
    self.account_balance = balance

    for i,j in self.account_owner.items():
      if self.account_num == str(j):
        print("\nYour account balance has been updated 😕")
        print("Your current balance is:", balance)
      
      else:
        print("Wrong Account Number.Cannot process transaction.")
    
          
  def withdraw(self,amount,account_num):
    self.amount = amount
    self.account_num= account_num
    
    for i,j in self.account_owner.items():
      if self.account_num == str(j):
        if int(self.amount) > int(self.account_balance):
          print("\nInsufficient fund. Please try again")
          print("Your current balance is  ", self.account_balance)

        else:
          blnce = int(self.account_balance) - int(self.amount)
          print("\nYour account balance has been updated")
          print("current balance = ", blnce)
          self.account_balance= blnce
      else:
        print("Wrong Account Number.Cannot process transaction.")
 
  def view_balance(self):
    print("Your available account balance is : ", self.account_balance)

class Application:
  account_owner= []
  ask= "y"
  
  def bank_name(self):
    print("\n**** WELCOME TO BSCS BANK OF UNIVERSE ****\n")

  def __verify_account(self):
    
    print("     ***** TRANSACTIONS *****     \n")
    print("            Menu:              ")
    print("          1. Log-in                  ")
    print("          2. Sign-up                 \n")
    
    option = input("Enter your choice: ")
    self.user.account_user(option)
  
  def __account_details(self):
    print("\n----------ACCOUNT INFORMATION----------")

    for a,b in self.user.act_owner().items():
      print(f"Account Name: {a.upper()}")
      print(f"Account Number: {b}")
      

  def __user_transac_menu(self):
    while self.ask == "y":
      print("\n     ***** TRANSACTION *****       \n")
      print("               Menu:                     ")
      print("            1. Deposit                   ")
      print("            2. Withdraw                  ")
      print("            3. Check Balance              ")

      transaction = input("\nEnter your Transaction: ")
      if transaction == "1":
        amount = input("Enter Amount: ")
        account_num= input('Enter Account Number: ')
        self.user.deposit(amount,account_num)

      elif transaction == "2":
        amount = input("Enter Amount: ")
        account_num= input('Enter Account Number: ')
        self.user.withdraw(amount,account_num)

      else:
        self.user.view_balance()
        
      self.ask = input("\nAnother transaction? y/n: ")
      
      if self.ask == "n":
          print("\n************************************")
          print("Transaction is now complete.")
          print("Thanks for choosing us as your bank")

  def transactions(self,user:User):
    self.user= user
    
    self.bank_name()
    self.__verify_account()
    self.__account_details()
    self.__user_transac_menu()

app= Application()
user= User('Accounts')
app.transactions(user)