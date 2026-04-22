import math
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiplicate(a,b):
    return a * b
def division(a,b):
    if b == 0:
        print('cannot possible to dividing by zero')

    return a / b

    
print('1.add')
print('2.substract')
print('3.multiplicate')    
print('4.division')
print('5.sqrt')


choice=int(input('choose anyone'))
if choice == 5:
               num=float(input('enter a number'))
               if num >=0:
                 print('result',math.sqrt(num))
         
    
a=float(input('enter first number'))
b=float(input('enter second number'))

if choice == 1:
    
    print('result :',add(a,b))
elif choice == 2:
    print('result :',substract(a,b))
elif choice == 3:
    print('result :',multiplicate(a,b))
elif choice == 4:
    print('result :',division(a,b))


else:
    print('invalid choice')
   






















