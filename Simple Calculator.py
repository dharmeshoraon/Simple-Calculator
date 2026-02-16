a=int(input("Enter a Number:"))
b=input("/ for division/n * for multiplication /n + for addition /n - for substraction/n ^ for power")
c=int(input("Enter a second number"))
if b=="/":
    print("Answer:",a/c)
elif b=="*":
    print("Answer:",a*c)
elif b=="+":
    print("Answer:",a+c)
elif b=="-":
    print("Answer:",a-c)
elif b=="^":
    print("Answer:",a**c)
else:
    print("Invalid Operator")
