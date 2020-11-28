#1
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(i+2)
print(list2)
#2
for i in range(0,5):
    for j in range(5-i,0,-1):
        print(j,end="")
        print()
#3
n=int(input("enter the  n value:"))
a=0
b=1
sum=0
count=1
print("fibonacci series:",end="")
while(count<=n):
    print(sum,end="")
    count +=1
    a=b
    b=sum
    sum= a+b
#4
num=int(input("enter the number:"))
sum=0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num ==sum:
    print(num,"is an armstrong number")
else:
    print(num,"not an armstrong number")
#5
num=9
for i in range(1,11):
    print(num,'x',i,'=',num*i)
#6
num=int(input("enter the number:"))
if num>0:
    print("positive number")
else:
    print("negative number")
#7
a=int(input("enter the number of days:"))
yr=int(a/365)
dy=a%365
print("the age is:",yr,"year(s) and ",dy, "days")
#8
import math
a=math.pi/6
b=3
c=4
print("the value of sine of pi/6 is:",end="")
print(math.sin(a))
print("the value of cosine of pi/6 is:",end="")
print(math.cos(a))
print("the value of tangent of pi/6 is:",end="")
print(math.tan(a))
#9
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter Choice(1-4): "))
if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")

