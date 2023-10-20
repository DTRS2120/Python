import math

while True:
    def sum():
        a=int(input("Enter First Number For Addition : "))
        b=int(input("Enter Second Number For Addition : "))
        c=a+b
        print("Addition Is : ",c)
    def mult():
        a=int(input("Enter First Number For Muliplication : "))
        b=int(input("Enter Second Number For Muliplication : "))
        c=a*b
        print("Multiplication Is : ",c)
    
    def sub():
        a=int(input("Enter First Number For Substraction : "))
        b=int(input("Enter Second Number For Substraction : "))
        c=a-b
        print("Substraction Is : ",c)

    def div():
        a=int(input("Enter First Number For Division : "))
        b=int(input("Enter Second Number For Division : "))
        c=a/b
        print("Division Is : ",c)
        
    def sqr():
        a=int(input("Enter Number For Taking Root : "))
        c=math.sqrt(a)
        print("Root Is : ",c)
        
    def evnodd():
        a=int(input("Enter Number To Verify Whether it is Even or Odd : "))
        if a%2==0:
            print("Number Is Even !")
        else:
            print("Number Is Odd")
    def posineg():
        a=int(input("Enter Number To Verify Whether it is Positive or Negative : "))
        if a>0:
            print("Number Is Positive !")
        else:
            print("Number Is Negative")
            
            
                
    print("\n What Operation Would You Like To Perform , \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Square Root \n 6.Even/Odd \n 7.Positive/Negative \n 8.Exit")
    choice=input("Enter Your Choice : ")

    if choice=="1":
        sum()
    elif choice=="2":
        sub()
    elif choice=="3":
        mult()
    elif choice=="4":
        div()
    elif choice=="5":
        sqr()
    elif choice=="6":
        evnodd()
    elif choice=="7":
        posineg()
    elif choice=="8":
        break
    else:
        print("\n Error: Enter An Appropriate Choice ")

    

