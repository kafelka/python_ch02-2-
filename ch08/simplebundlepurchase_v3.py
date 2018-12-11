# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:10:24 2018

@author: nahas
"""
def DataBundlePurchase(truePasscode, balance):
    if checkPasswordXTimes(3, truePasscode):        
        options = int(askTransaction())              # TYLKO pobiera input od uzywkownika, ma byc 1 lub 2
        if options == 1:
            print("Your balance is {}.".format(balance))
        elif options == 2:
            purchaseTopUp(balance)                  # funkcja do kupowania
    else:
        print("Too many attempts at password")


def askTransaction():
    options = input("Please select an option: 1 for credit balance request, 2 for purchase data bundle.")
    if options == "1" or options == "2":
        return options
    else: 
        return askTransaction()


def checkPasswordXTimes(attemptLeft, truePasscode):
    if attemptLeft <= 0:
        return False
    elif passwordCheck(truePasscode):
        return True
    else:
        return checkPasswordXTimes(attemptLeft - 1, truePasscode)


def passwordCheck(truePasscode):
    attempt = input("Please provide your password ")
    if attempt == truePasscode:
        return True
    else:
        return False
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else: 
        return False
    
    
def purchaseTopUp(balance):
    if checkBalance(balance) == False:
      print("Your balance is not sufficient: {}.".format(balance))
      return 
     
       
def verifyPhone():
    phone = input("Please provide your phone number: ")
    phone2 = input("Please confirm your phone number: ")
    
    if phone == phone2:
        return True
    else:
        print("Please try again")
        return verifyPhone()



def getTopUpAmount():
    topup = int(input("Select bundle: 10, 15, 20, 25"))
    
    if topup % 5 == 0:
        return topup
    else:
        print("Wrong bundle")
        return getTopUpAmount()
        
if topup > balance:
     print("Magda robi")
else:
      print("Magda robi")