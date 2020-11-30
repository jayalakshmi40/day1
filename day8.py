#1
print("enter 1 for add,2 for subtraction,3 for multiply,4 for division")
try:
    ans=int(input("option:"))
    if ans==1:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first+second)
    elif ans==2:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first-second)
    elif ans==3:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first*second)
    elif ans==4:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first/second)
    else:
        print("enter a valid integer")
except NameError:
    print("please use numbers only")
except SyntaxError:
    print("please use numbers only")
except TypeError:
    print("please use numbers only")
except AttributeError:
    print("please use numbers only")
except ValueError:
    print("please use numbers only")
#2
#1
print("enter 1 for add,2 for subtraction,3 for multiply,4 for division")
try:
    ans=int(input("option:"))
    if ans==1:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first+second)
    elif ans==2:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first-second)
    elif ans==3:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first*second)
    elif ans==4:
        first=float(input("first number:"))
        second=float(input("second number:"))
        print(first/second)
    else:
        print("enter a valid integer")
except NameError:
    print("please use numbers only")
except SyntaxError:
    print("please use numbers only")
except TypeError:
    print("please use numbers only")
except AttributeError:
    print("please use numbers only")
except ValueError:
    print("please use numbers only")
 #3
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
#4
#we use try-except for checking and validation purpose.
#apat from these, try-except is not needed.
#5
try:
    n=int(input("enter the number"))
    print("sucessfully")
except ValueError:
    print("not an integer")
