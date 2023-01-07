n=int(input("enter a number:"))
a=[]
while(n>0):
    d=n%2
    a.append(d)
    n=n//2
a.reverse()
print("binary equivalent is:")
for i in a:
    print(i,end=" ")
