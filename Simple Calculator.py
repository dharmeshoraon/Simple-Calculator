a=int(input("Enter a Number:"))
b=input("1.)/ for division\n2.)* for multiplication\n3.)+ for addition\n4.)- for substraction\n5.)^ for power\nEnter the operator you want to use:")
c=int(input("Enter a second number"))
d=int(input("Do you want to continue? 1 for \"yes\"\nor press any number to exit:"))
if d==1:
    while d==1:
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
        break
else:
    exit("You have exited the program")

