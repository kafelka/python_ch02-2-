# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:57:45 2018

@author: nahas
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        options = int(input("Please select an option: 1 for credit balance request, 2 for purchase data bundle."))
        if options == 1:
#           
            return ("Your balance is {}.".format(balance))
        elif options == 2: 
          if checkBalance(balance) > 0:
              return "You can order data bundle"
          else:
            return ("Your balance is not sufficient: {}.".format(balance))
        
        else:
            return "Incorrect option. Please try again."
      
#        
#        if checkBalance(balance):
#            return ("Your balance is {}.".format(balance))
#        else:
#            return ("Your balance is not sufficient: {}.".format(balance))
##        return "Password OK"
    else: 
        return "Wrong password"


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
    
#def askTransaction(balance):
#    options = input("Please select an option: 1 for credit balance request, 2 for purchase data bundle.")
#    
#    if options == 1:
##        exit()
#        return ("Your balance is {}.".format(balance))
#    elif options == 2:
##        exit()
#        return "Service is unavailable"
#    else:
##        exit()
#        return "Select 1 for credit balance request, 2 for purchase data bundle."
    