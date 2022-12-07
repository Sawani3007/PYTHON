print(" Hello! Welcome to ABC Bank--")
print("Please wait while your card is being read-----")
print("Enter your details----")  #Adding details of user
name=input("Enter your name")
pin = int(input("Enter your pin:"))
balance= int(input("Total Balance in your Account:"))    
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
while(str!="n"):  
    print('Please Press 1 For Your Balance\n')
    print('Please Press 2 To Make a Withdrawl\n')
    print('Please Press 3 To Deposit in\n')
    print('Please Press 4 To Exit\n')
    option = int(input('What Would you like to choose?'))  #Giving user choice
    if option ==1:
        print("Your Balance is ",balance)  #printing the total available balance
    elif option ==2:
        withdrawl=int(input("enter amount needs to be withdrawl"))
        if withdrawl<balance:   
            left_balance=balance-withdrawl   
            print("Your balance now in account is:",left_balance)   #printing the total left balance after the withdrawl
            balance=left_balance
        else:
            print("Invalid amount")
    elif option==3:
        deposit=float(input("enter the amount you want to deposit"))
        balance=balance+deposit
        print("Total Amount in Your Account",balance)  #printing the total balance after depositing 
    elif option == 4: 
        break
if balance < 5000:       
    print("Low Balance")
    print("Have a good day---")
else:
    print("Thank you for the visit")
    print("Have a good day---")
