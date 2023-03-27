# importing libraries
import time
import os

# subs
# startup sequence
def startup():
  print("starting tfbsATM.iso ...")
  time.sleep(1)
  print("importing customerDatabase ...")
  time.sleep(1)
  print("loading libraries ...")
  time.sleep(1)
  print("logging in as 'user' ...")
  time.sleep(1)
  print("loading on Intel(R) driver 3.85942 ...")
  time.sleep(2)
  print("bootup complete ...")
  time.sleep(1)
  print("loading ...")
  time.sleep(4)
  cls()
  time.sleep(1)
  return()

# clears screen
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  return()

# displays balance
def displayBalance(customerList1):
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList1[1] + "!\n\n")
  print("Your current balance is "+"£"+customerList1[3])
  input("\n\nPress enter to return to the menu...")
  menu(customerList1)
  return()

# runs the withdraw screen
def withdrawMoney(customerList2):
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!")
  print("\n\nYour current balance is "+"£"+customerList2[3])
  print("Please select an option:\n1 - £10\n2 - £20\n3 - £50\n4 - £100\n5 - Other Amount\n")
  chosenMoney = input()
  # tests for option
  if chosenMoney == "1":
    cls()
    print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!\n\n")
    if float(customerList2[3]) >= 10:
      print("Withdrawn £10 from your account!")
      customerList2[3] = str(float(customerList2[3]) - 10)
      print("Your new balance is",customerList2[3])
      input("\nPress enter to return to the menu...")
      menu(customerList2)
    else:
      print("You do not have sufficient funds in your account.\n\n")
      input("Press enter to return to the menu...")
      menu(customerList2)
  if chosenMoney == "2":
    cls()
    print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!\n\n")
    if float(customerList2[3]) >= 20:
      print("Withdrawn £20 from your account!")
      customerList2[3] = str(float(customerList2[3]) - 20)
      print("Your new balance is",customerList2[3])
      input("\n\nPress enter to return to the menu...")
      menu(customerList2)
    else:
      print("You do not have sufficient funds in your account.\n\n")
      input("Press enter to return to the menu...")
      menu(customerList2)
  if chosenMoney == "3":
    cls()
    print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!\n\n")
    if float(customerList2[3]) >= 50:
      print("Withdrawn £50 from your account!")
      customerList2[3] = str(float(customerList2[3]) - 50)
      print("Your new balance is",customerList2[3])
      input("\n\nPress enter to return to the menu...")
      menu(customerList2)
    else:
      print("You do not have sufficient funds in your account.\n\n")
      input("Press enter to return to the menu...")
      menu(customerList2)
  if chosenMoney == "4":
    cls()
    print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!\n\n")
    if float(customerList2[3]) >= 100:
      print("Withdrawn £100 from your account!")
      customerList2[3] = str(float(customerList2[3]) - 100)
      print("Your new balance is",customerList2[3])
      input("\n\nPress enter to return to the menu...")
      menu(customerList2)
    else:
      print("You do not have sufficient funds in your account.\n\n")
      input("Press enter to return to the menu...")
      menu(customerList2)
  if chosenMoney == "5":
    cls()
    print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList2[1] + "!\n\n")
    otherAmount = float(input("Please enter an amount to withdraw...  "))
    if float(customerList2[3])%10 == 0:
      if float(customerList2[3]) >= otherAmount:
        print("Withdrawn",otherAmount,"from your account!")
        customerList2[3] = str(float(customerList2[3]) - otherAmount)
        print("Your new balance is",customerList2[3])
        input("\n\nPress enter to return to the menu...")
        menu(customerList2)
      else:
        print("You do not have sufficient funds in your account.\n\n")
        input("Press enter to return to the menu...")
        menu(customerList2)
    else:
      print("You must enter an amount that is divisible by ten.")
      input("Press enter to return to the menu...")
      menu(customerList2)
  return()

# runs the deposit screen
def depositMoney(customerList3):
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList3[1] + "!\n\n")
  addedMoney = float(input("Please enter an amount to deposit...  "))
  customerList3[3] = str(float(customerList3[3]) + addedMoney)
  moneyAdded = str(addedMoney)
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList3[1] + "!\n\n")
  print("You have deposited £" + moneyAdded + " into your account.")
  print("Your new balance is",customerList3[3])
  input("\n\nPress enter to return to the menu...")
  menu(customerList3)

# exits the atm
def exitCode(customerList4):
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\n\n")
  print("Now exiting...")
  database = open("testdata.txt","a")
  customerList4[3] = customerList4[3].replace("\n","")
  customerList5 = " ".join(customerList4)
  database.write("\n")
  database.write(customerList5)
  database.close()
  time.sleep(3)
  print("Logout complete.\nGoodbye,",customerList4[1] + "!")
  exit()

# runs the menu
def menu(customerList):
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\nWelcome", customerList[1] + "!")
  print("\n\nPlease select an option:\n1 - Display Balance\n2 - Withdraw Money\n3 - Deposit Money\n9 - Return Card and Logout\n")
  chosenOption = input()
  if chosenOption == "1":
    displayBalance(customerList)
  if chosenOption == "2":
    withdrawMoney(customerList)
  if chosenOption == "3":
    depositMoney(customerList)
  if chosenOption == "9":
    exitCode(customerList)
  return()
  
# =======================main code========================
# main screen
# runs the startup screen
startup()
runLogin = True
# loops the login screen until a valid id is given
while runLogin == True:
  cls()
  print("ToothFairyBankingSolutionsATM v2.6.5\n \n")
  customerNumber = ""
  line = -1
  while len(customerNumber) != 5:
    customerNumber = input("Please enter your customer number:  ").strip()

  # tests for exit code
  if customerNumber == "99999":
    exit()

  # searches for number in database, and deletes the line
  searchfile = open("testdata.txt", "r")
  for line in searchfile:
    if customerNumber in line: customerLoggedIn = line
  searchfile.close()
  customerLogList = customerLoggedIn.split(" ")
  deletefile = open("testdata.txt","r")
  lines2 = deletefile.readlines()
  deletefile.close()
  deletefile = open("testdata.txt","w")
  for line in lines2:
    if customerNumber not in line:
      deletefile.write(line)
  deletefile.close()

  # tests provided number against database
  if customerNumber == customerLogList[0]:
    print("Login success!\nPlease wait...")
    time.sleep(1)
    cls()
    runLogin = False
  menu(customerLogList)

