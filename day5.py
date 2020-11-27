def add_num(x,y):
    sum=x+y;
    return sum;
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the sum is",add_num(num1,num2))

def sub_num(x,y):
    sub=x-y;
    return sub;
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the sub is",sub_num(num1,num2))

def mul_num(x,y):
    mul=x*y;
    return mul;
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the mul is",mul_num(num1,num2))

def div_num(x,y):
    div=x/y;
    return div;
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the div is",div_num(num1,num2))

def covid(x,y):
    print("the patient name is "+x+" and the temperature is "+str(y))
x=input("enter the patient name:")
y=int(input("enter the temperature in degree:"))
if(y>=98):
    covid(x,y)
else:
    print("your body temperature is normal")