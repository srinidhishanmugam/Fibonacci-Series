a=int(input("Enter the terms"))
f=0                                         
s=1                                         
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        n=f+s                           
        print(n,end=" ")
        f=s
        s=n
