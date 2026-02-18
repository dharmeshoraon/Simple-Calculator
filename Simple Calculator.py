num_1=int(input("Enter a Number:"))
operation=input("1.)/ for division\n2.)* for multiplication\n3.)+ for addition\n4.)- for substraction\n5.)^ for power\nEnter the operator you want to use:")
num_2=int(input("Enter a second number"))
flow=int(input("Do you want to continue? 1 for \"yes\"\nor press any number to exit:"))
if flow==0:
    exit("You have exited the program.")
elif flow==1:
    if operation=="/":
            print("Answer:",num_1/num_2)
    elif operation=="*":
            print("Answer:",num_1*num_2)
    elif operation=="+":
            print("Answer:",num_1+num_2)
    elif operation=="-":
            print("Answer:",num_1-num_2)
    elif operation=="^":
            print("Answer:",num_1**num_2)
else:
    print("Invalid input. Please enter 0 or 1.")