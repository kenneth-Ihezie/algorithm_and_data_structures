arr = [1, 2, 2, 4]
for i in arr:
    print(i)


x, y = 10, 20
print(x)
print(y)

#list comprehesion
print([i for i in range(20)])

#printing out the memory location of x variable.
print(hex(id(x)))

# a = input("Enter a numer: ")
# #convert the input of sting to number
# b = eval(input("Enter a number: "))
# print(a)

print(3/2)


#################################################################
#strings in python

stri = "Apple"
print(stri)

sen = "it's an apple"
print(sen)

sent = 'my name is "kenneth"'
print(sent)

fname = 'Kenneth'
lname = 'ihezie'

#addition in string or concatenation
name = fname + " " + lname
print(name)

#multiplication string
print(name * 3)

#slicing
fruit = "Mango"
#from 0 to 5
print(fruit[0:5])
#from 2 to 4
print(fruit[2:4])
#return all element
print(fruit[:])


#negative indexing
print(fruit[-1])
#returns all element in the fruit variable
print(fruit[-5 : ])


#double column. the first is where u start counting and the last element is step size
print(fruit[0::2])

len(fruit)
fruit.upper()
fruit.lower()

#lists are mutable
list = [1, 2, 4, 6, 7, [True, True, False], "ff", 'yy']
list[5][0]
#slicing
print(list[5 : 6])
print(list[6 : 8])

#double column
print(list[0 :: 5])

list_one = [1, 2, 3]
list_two = [4, 5, 6]
list_three = list_one + list_two
print(list_three)
list_three[4] = 10
list_three.remove(3)
max(list_three)
min(list_three)
#to know how many times an item occured in a list
list_three.count(3)

#Tuples are immutable
ti = (10, 12, 14, 16)
type(ti)
print(ti[0])
#slicing
ti[2 : 3]
ti[0 :: 2]

# multiple list iteration.
for i, j in [0, 2], [1, 4]:
    print(i , j)


class test:
    def __init__(self):
        pass

    def sumNumbers(self, a, b):
        return a + b


testin = test()
print(testin.sumNumbers(2, 4))