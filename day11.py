#1
list1=["python","java","cprogramming"]
list2=['1','2','3']
x=zip(list1,list2)
print(tuple(x))
#2
x=list(range(1,8))
y=['A','B','C','D','E','F','G','H']
z=zip(x,y)
print(tuple(x))
#3
list1=[21,8,65,1,7,32]
x=sorted(list1)
print(x)
#4
def fun(num):
    if(num%2!=0):
        return True
    else:
        return False
seq=[31,46,36,54,16,63,9,42,81]
filtered_list=filter(fun,seq)
print("the filter odd number are",list(filtered_list))
