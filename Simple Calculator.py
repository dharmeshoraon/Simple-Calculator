a=int(input("Enter a Number:"))
b=input("/ for division/n * for multiplication /n + for addition /n - for substraction/n ^ for power")
c=int(input("Enter a second number"))
d=int(input("Do you want to continue? 1 for yes and 0 for no:"))
if d==0:
    exit()
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
