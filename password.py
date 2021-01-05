alpha=input("enter a alphabet")
if alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    digit=int(input("enter a digit"))
    if digit>1 and digit<100000:
        sym=input("enter symbol")
        if sym=="@" or sym=="#" or sym=="$":
            print("ok")
            print(alpha+str(digit)+sym)
        else:
            print("wrong")  
    else:
        print("wrong")
else:
    print("wrong")                  