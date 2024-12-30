print("choose the action")
print("                 ")
print("1.addition","\n2.subtraction","\n3.multiplication","\n4.division")

choice=input("whats your choice? (1-2-3-4) :  ")
number1=int(input("1.number:"))
number2=int(input("2.number:"))


if choice =="1":
    print(number1,"+",number2,"=",number1+number2)
elif choice =="2":
    print(number1, "-",number2,"=",number1-number2)
elif choice =="3":
    print(number1,"x",number2,"=",number1*number2)
elif choice =="4":
    print(number1,"/",number2,"=",number1/number2) 