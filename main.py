# importing libraries
import random
import time
import os

# subs
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
    
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
  return()

# ==============================================================main code=========================================================
# main screen
startup()
print("ToothFairyBankingSolutionsATM v2.6.5\n \n")

customerNumber = ""
line = -1
while len(customerNumber) != 6:
  customerNumber = input("Please enter your customer number:  ").strip()
with open("customerDatabase.txt") as file:
  filecontent = file.readlines()
  file.close()
for ln in range(0,len(filecontent)):
  userinf = filecontent[ln]
  vid = userinf[0:6]
  line += 1 

print(filecontent)

