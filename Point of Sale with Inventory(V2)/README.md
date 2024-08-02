## POS v2

Create a Point-of-Sales systems for a small convenience store in Pandi.


### Main

```
WELCOME TO POINT-OF-SALES v2

What do you want to do?

[1] Login
[2] Sign-up
[3] Exit
```

### Login Screen

```

LOGIN POS v2

To login, enter your username and password:

Username: 
Password:

```

if user fails to login,
```
Invalid login credentials. Forgot your password? contact your admin.
```

### Signup

```

CREATE AN ACCOUNT

Username:
Full Name:
Role (ADMIN/CASHIER):
Password:
Re-type Password:

Your account has been created. You may now login.

```


### POS Menu

```
Welcome, {username}!

[1] New Customer
[2] Inventory
[3]] Logout
```

### Inventory

```
CODE      NAME          BRAND  UNIT  PRICE

00001     Bear Brand    Nestle   10     15
...
00010     Nescafe Pack  Nestle   20     8


OPTIONS

[1] Add Product
[2] Back

Enter Choice: 


```

#### Add Product

```

ADD NEW PRODUCT

Product Code:
Product Name:
Brand Name:
Unit:
Price (PHP):

```

If user completed the form, it should add the product to the database.

```

New product was added to inventory.
Do you want to add another product? (y/n)

```

If user responds `n`, return to **POS Menu**


### New Customer

```

NEW ORDER

ITEMS IN CART

CODE      NAME          BRAND  UNIT  PRICE

00001     Bear Brand    Nestle    1    10


ENTER CODE: {1}

Bear Brand Added to Cart!

```

If code was empty, it should complete the punching of items then would display the payment section.

```

SUB-TOTAL        10.00
PAYMENT:         {userinput;20}
CHANGE:          10.00

TRANSACTION COMPLETE: RECEIPT NO. {1}

[Press ENTER to continue]
```

Once enter is pressed, it should go back to **POS Menu**