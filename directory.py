d1={'a':200,'b':100}
d2={'x':200,'y':300}
d=d1.copy()
d.update(d2)
print(d)

directory={'x':1,'y':2,'z':3}
print(directory)
if 'z' in directory:
 del directory['z']
print(directory)

keys=['red','tomato','coral']
values=['#FF0000','#FF6347','#FF7F50']
color_dictionary=dict(zip(keys,values))
print(color_dictionary)

a=set([1,2,3,4,5,6])
print(len(a))

sn1={7,8,9,10,11,12}
sn2={11,12,13,14,15}
print(sn1)
print(sn2)
print(sn1-sn2)