n=int(input("enter the number= "))
n1=n
c=0
k=int(n**(1/2))
for i in range(1,k+1):
    if(n1%i==0):
        if(n1%(i+1)==0):
            if(i*(i+1)==n):
                c=c+1
if(c==1):               
    print("pronic Number")
else:
    print("not pronic Number")