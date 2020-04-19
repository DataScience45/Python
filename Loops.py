#in not in
a='naveenlakkam@gmail.com'
print('@' in a)
print('#' not in a)


#is isnot
x=2
y=4
print(x is y)
x+=2 #x = x+2
print(x is y)

#is ==

print(x==y)
print(x is y)

a=[]
b=[]
c=a
print(a==b)
print(a is b)
print(id(a),id(b),id(c))

#while (condition based)

i=0
while i < 10:
    print(i)
    i+=1

#for (value)


for x in range(5):
    print(x)

for x in range(2,5):
    print(x)
    
for x in range(2,10,3):
    print(x)

x=[9,6,5,4]
for i in x:
    print(i)

x='naveen'
for i in x:
    pass
    #print(i)
print(i)


for x in range(2,10,3):
    print(x)
else:
    print('completed')













