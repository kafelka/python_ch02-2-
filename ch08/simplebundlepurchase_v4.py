# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:10:24 2018

@author: nahas
"""
def DataBundlePurchase(truePasscode, balance):
    if threeAttempt(truePasscode):       
        options = int(askTransaction())             
        if options == 1:
            print("Your balance is £{}.".format(balance))
        elif options == 2:
            purchaseTopUp(balance)     
            return "happy now"             
    else:
        return "Too many attempts. Come back in 15 minutes."
        

def askTransaction():
    options = input(
"""
Please select an option:
    * 1 for credit balance request 
    * 2 for purchase data bundle 
""")
    if options == "1" or options == "2":
        return options
    else: 
        return askTransaction()


def threeAttempt(truePasscode):
    if passwordCheck(truePasscode):
        return True
    else:
        print("Please try your 2nd attempt.")
    if passwordCheck(truePasscode):
        return True
    else:
        print("Please try your last attempt.")
    if passwordCheck(truePasscode):
        return True
    else:
        return False


def passwordCheck(truePasscode):
    attempt = input("Please enter your PIN: ")
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
    if checkBalance(balance):
        verifyPhone() 
        print("The top up must be a multiple of 5 pounds and be no greater than £25.")               
        topup = getTopUpAmount()   
        maxTopup = 25
        if topup > maxTopup:
            print("Your topup exceeds the maximum topup allowed. Try again.")
            getTopUpAmount()
        elif topup > balance:
            print("Amount exceeds your current balance.")
            print("Request rejected.")
        else:
            print("You have topped up successfully. Thank you!")
            print("Your new balance is: £{}".format(round(balance - topup,3)))
    else:
         print("Your balance is not sufficient: {}.".format(balance))
         return "Request rejected"

       
def verifyPhone():
    phone = input("Please provide your phone number: ")
    phone2 = input("Please confirm your phone number: ")
    
    if phone == phone2:
        return True
    else:
        print("Please try again.")
        return verifyPhone()



def getTopUpAmount():
    topup = int(input("Select a bundle: 10, 15, 20 or 25: "))
    
    if topup % 5 == 0 & topup <= 25:
        return topup
    else:
        print("Wrong bundle")
        return getTopUpAmount()
        
