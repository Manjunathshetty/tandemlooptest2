#program when user gives the input
lst = []
n= int(input("no of elements:"))
for i in range(0,n):
    no=int(input())
    lst.apppend(no)
print(lst)
even=0
odd=0
for num in lst:
	if num % 2 ==0:
		even+=1
    else:
    	odd+=1
print("even=",even)
print("odd=",odd)
	

#program when elements of list is given

list=[3,5,6,8,13,15,100,111]
ecount=0
ocount=0
for n in list:
	if n% 2==0:
		ecount+=1
	else:
		ocount+=1
print("EVEN=",ecount)
print("ODD=",ocount)

