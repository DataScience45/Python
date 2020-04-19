# Numarical Variables
a=True
b=400
c=10.50
d=123
f=255
e=0xff
g=5+2j


#multiple variable dclaration

# String
name="Python learning"
print(name)
print(name[2:6])#upper bound is not 
print(name[1:-2])
print(name+name)
print(name*4)
print(name[::-1])
print(name[1:-2:2])
# List

mylist=['apple',True,10,10.56,10+1J]
print(mylist[0])
print(mylist[-1])
mylist=2*mylist
print(mylist)


#Tuples Read only Immutable

mytuple=('apple',True,10,10.56,10+1J)
#mytuple[0]=10
mytuple1=(1) #consider as Int
print(type(mytuple1))
mytuple1=(1,)#conider as Tuple
print(type(mytuple1))

#Dictionary

course ={1:['Phython'],2:'C',3:'java'}
print(course[2])
print(course[3])
print(course.keys())
print(course.values())

#SET Unique values with out index

myset={10,20,30,60,50}

print(myset)
myset1={10}
print(type(myset1))





