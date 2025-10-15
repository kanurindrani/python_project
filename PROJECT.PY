print("welcome to abc bank")
print("1.new account")
print("2.deposit")
print("3.withdrawl")
print("4.balance inquiry")
print("5.exit")
choice=int(input("enter the choice"))
if choice==1:
    a=input("enter the a/c holder name:")
    b=int(input("enter the pin number:"))
    c=int(input("enter the deposit number:"))
    print("successfully account created....!!!")
elif choice==2:
    a = input("Enter the A/C holder name: ")
    b = int(input("Enter the PIN number: "))
    currentbalance = 2000
    print("Current balance:", currentbalance)
    depositbalance = int(input("Enter the amount to deposit: "))
    v = currentbalance + depositbalance
    print("Updated balance:", v)
     
elif choice==3:
     a=input("enter the a/c holder name:")
     b=int(input("enter the pin number:"))
     currentbalance = 2000
     print("Current balance:", currentbalance)
     withdrawl=int(input("enter the amount"))
     if withdrawl <= currentbalance:
         print("amountvalid")
         print("sucess")
         v = currentbalance - withdrawl
         print("Updated balance:", v)
     else:
         print("insff balance")
elif choice==4:
     a=input("enter the a/c holder name:")
     b=int(input("enter the pin number:"))
     if a == "indrani" and b == 123:
         print("vaild details")
         currentbalance = 2000
         print("Current balance:", currentbalance)
        
     else:
        print("incorrect a/c details")
    
else:
    print("exit applicaton")
    
