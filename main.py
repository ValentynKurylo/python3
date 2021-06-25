'''1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
#################################################################################'''
'''
st = input('Enter string: ')
for i in range(len(st)):
    if st[i].isdigit():
        print(st[i],  end=', ')
'''

'''
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
#################################################################################
'''
'''
st = input('Enter string: ')
#st = st.split()
print(st)
l = ''
for i in range(len(st)):
    if st[i].isdigit():
        l += st[i]
    else:
        if len(l) != 0:
            if l[len(l)-1].isdigit():
                l += ', '

print(l)
'''
'''
1)есть строка:
greeting = 'Hello, world'
записать каждый символ в лист поменяв его на верхний регистр
пример:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
'''
'''
greeting = 'Hello, world'

greet = [greeting[i].upper() for i in range(len(greeting))]
print(greet)
'''
'''
2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
пример:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
'''
'''
list = [i**2 for i in range(0,50,2)]
print(list)
'''


'''
- створити функцію яка виводить ліст
'''
'''
def show(list):
    for i in range(len(list)):
        print(list[i])
        
list = [5, 9, 3, 67, 23]
show(list)
'''
'''
- створити функцію яка приймає три числа та виводить та повертає найменьше.
'''
'''
def min(a, b, c):
    if a <= b and a <= c:
        print(a)
        return a
    elif b <= a and b <= c:
        print(b)
        return b
    else:
        print(c)
        return c
m = min(7,3,9)
'''
'''
- створити функцію яка приймає три числа та виводить та повертає найбільше.
'''
'''
def max(a, b, c):
    if a >= b and a >= c:
        print(a)
        return a
    elif b >= a and b >= c:
        print(b)
        return b
    else:
        print(c)
        return c
m = max(7,3,9)
'''
'''
- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
'''
'''
def min_max(*args):
    print(min(args))
    return max(args)

max = min_max(7, 4, 90, 56, 2, 39)
print(max)
'''
'''
- створити функцію яка повертає найменьше число з ліста
'''
'''
def min_l(list = []):
    return min(list)

min = min_l([78, 56, 34, 90])
print(min)
'''

'''
- створити функцію яка повертає найбільше число з ліста
'''
'''
def max_l(list=[]):
    return max(list)

max = max_l([67, 45, 566, 89, 34])
print(max)
'''

'''
- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
'''
'''
def sum(list=[]):
    s = 0
    for i in range(len(list)):
        s += list[i]
    return s
s = sum([56, 34, 78, 2, 9, 67])
print(s)
'''
'''
- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
'''
'''
def avr(list=[]):
    s = 0
    for i in range(len(list)):
        s += list[i]
    a = s / len(list)
    return a
a = avr([56, 34, 78, 2, 9, 67])
print(a)
'''

'''
decorators
- є функція: 
def pr(): 
    return 'Hello_boss_!!!'
 написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
'''

def decor(func):
    def wrap(s, *args, **kwargs):
        func(s, *args, **kwargs)
        st = ' '
        st = s
        st = st.replace('_', ' ')
        return st
    return wrap

s = 'Hello_boss_!!!'

@decor
def pr(s):
    return s

st = pr(s)
print(st)