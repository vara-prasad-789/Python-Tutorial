
if 5 > 2:
	print("5 is greater than two!")
if 5 > 2:
	      print("5 is greater than two!")

x = 5

y = "Hello, World!"
print(x)
print(y)
#comments
"""
hbiuuvbwuv
dkvnov
wvwovoklv
"""
z = 6
z = "hi"
print(z)

x = str(3)
y = int(3)
z = float(3)
print(x,type(x),y,type(y),z,type(z))

x = "str"
y = 'str'
print(x,y)

X = 3
x = 4
print(x,X)

myvar = 'john'
myVar = 'Doe'
print(myvar,myVar)

myVarName = 'john'
MyVarName = 'Doe'
my_var_name = 'Python'
print(myVarName,MyVarName,my_var_name)

x,y,z = 'orange','banana','cherry'
print(x,y,z)

x=y=z='orange'
print(x,y,z)

fruits = ['apple','banana','cherry']
x,y,z = fruits
print(x,y,z)


x = "awesome"
print("Python is "+ x)

x = 'python is '
y = 'awesome'
z = x+y
print(z)

x = 5
y = 10
print(x +  y)


x = 5
y = 'john'
#print(x + y) ERROR


x = 'awesome'
z = 'hard'
print('python is '+z)
def myfunc():
	x = 'fantastic'
	global y
	y = "fantastic"
	global z
	z = 'easy'
	print("python is "+x)

myfunc()

print("python is "+x , "python is "+y,"python is "+z)



x = "Hello World"
print(x)
print(type(x))

x = 20
print(x)
print(type(x))

x = 20.5
print(x)
print(type(x))

x = 1j
print(x)
print(type(x))

x = ['apple','banana','cherry']
print(x)
print(type(x))

x = ('apple','banana','cherry')
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {'name' : 'john','age' : 36}
print(x)
print(type(x))

x = {'apple','banana','cherry'}
print(x)
print(type(x))

x = frozenset({'apple','banana','cherry'})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b'hello'
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))


print("Setting the Specific Data Type")

x = str("hello world")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(x)
print(type(x))

x = complex(1j)
print(x)
print(type(x))

x = list(('apple','banana','cherry'))
print(x)
print(type(x))

x = tuple(('apple','banana','cherry'))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict(name='john', age=36)
print(x)
print(type(x))

x = set(('apple','banana','cherry'))
print(x)
print(type(x))

x = frozenset(('apple','banana','cherry'))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))


x = float(1)
y = int(2.8)
z = complex(1)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

print("Random Number :")
import random
print(random.randrange(500,10000))


x = int(1)
y = int(2.8)
z = int("3")
print("int(1) : ")
print(x)
print("int(2.8) :")
print(y)
print("int('3') :")
print(z)


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print("float(1) :")
print(x)
print("float(2.8) :")
print(y)
print("float('3') :")
print(z)
print("float('4.2') :")
print(w)


x = str("s1")
y = str(2)
z = str(3.0)
print("str('s1') :")
print(x)
print("str(2) :")
print(y)
print("str(3.0) :")
print(z)

a = "hello"
print(a)

a =''' You can assign a multiline string
 to a variable by using three quotes'''
print(a)

print("Strings are Arrays")
a = '''a = "Hello, World"
print(a[1])'''
print(a)

a = "Hello, World"
print(a[1])

print("Looping Through a String")
for x in "banana":
	print(x)

print("String Length")
a = "hello, world"
print(len(a))

b ='''Check String
 To check if a certain phrase or character
 is present in a string, we can use the keyword in.'''
print(b)

txt = "the best things in life are free!"
print('free' in txt)

print("Use it in an if statement")
txt = "the best things in life are free!"
if "free" in txt:
	print("yes, 'free' is present.")

print("Check if NOT")
print("To check if a certain phrase or character is NOT present in a string")
txt = "the best things in life are free!"
print("expensive" not in txt)

print("Use it in an if statement:")
if 'expensive' not in txt:
	print("No, 'expensive' is NOT present")

print("Slicing Strings")
b = "Hello, World!"
print(b[2:5])
print(b[7:13])

print("Slice From the Start")
print(b[:5])
print(b[:12])

print("Slice To the End")
print(b[2:])
print(b[7:])

print("Negative Indexing")
print(b[-5:-2])
print(b[-13:-7])


print("Modify Strings")
print("Upper Case")
a = "hello world!"
print(a.upper())
print("Lower Case")
a = "HEllo WORld!"
print(a.lower())

print("Remove Whitespace")
print("Whitespace is the space before and/or after the actual text")
a = "    Hello     ,      World      !     "
print(a.strip())

print("Replace String")
a = "Hello, World!"
print(a.replace("H","B"))

print("Split String")
print("The split() method returns a list where the text between the specified separator becomes the list items.")
a = "Hello, World!"
print(a.split(","))


print("String Concatenation")
a = "Hello"
b = "World"
c = a+b
print(c)

print("Adding Space")
c = a+" "+b
print(c)

print("String Format")
print("The format() method takes the passed arguments, formats them, and places them in the string where the placeholders { }")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("format() method takes unlimited number of arguments")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

print("You can use index numbers { 0} to be sure the arguments are placed in the correct placeholders")
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity,itemno,price))

print("Escape Characters")
txt = "We are the so-called \"vikings\" from the north"
print(txt)

print("Single Quote \' \' ")
print("Backslash \\ ")
print("New Line HELLO\nWORLD")
print("Carriage\rreturn ")
print("Tab HELLO\tWORLD")
print("Backspace HELLO\bWORLD ")
print("Form Feed \f ")
print("OCTAL VALUE \110 \145 \154 \154 \157")
print("HEX VALUE \x48 \x65 \x6c \x6c \x6f")


txt = "hello, and welcome to my world."
print(txt.capitalize())
txt = "Hello, and Welcome To My World"
print(txt.casefold())
txt = " Welcome USER "
print(txt.center(150))
print(txt.center(80,"O"))

txt = "I love apples, apple are my favourite fruit"
print(txt.count("apple"))
txt = "I love åpples, Åpplë are my fÆvourite fruit"
print(txt.encode())
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.endswith("my world.")
print(x)
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
print(txt)

txt = "Hello, welcome to my world"
x = txt.find("welcome")
print(x)
x = txt.find("e")
print(x)
x = txt.find("e",5,10)
print(x)
print(txt.find("q"))


print("two-decimal format:")
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I,m {1}".format("John",36)
txt3 = "My name is {}, I,m {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
print("Left Align")
txt = "we have {:<8} chickens."
print(txt.format(49))
print("Right Align")
txt = "we have {:>8} chickens."
print(txt.format(49))
print("Center Align")
txt = "we have {:^8} chickens."
print(txt.format(49))
print("Use '=' to place the plus/minus sign at the left most position")
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
print("Use '+' to always indicate if the number is positive or negative")
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
print("Use '-' to always indicate if the number is negative")
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
print('Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:')
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
print("Use ',' to add a comma as a thousand separator")
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
print('Use "_" to add a underscore character as a thousand separator')
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
print('Use "b" to convert the number into binary format')
txt = "The binary version of {0} is {0:b}"
print(txt.format(500))
print('Use "c" to Converts the value into the corresponding unicode character')
txt = "hello world {:c}"
print(txt.format(560))
print('Use "d" to convert a number, in this case a binary number, into decimal number format')
txt = "We have {:d} chickens."
print(txt.format(0b101))
print('Use "e" to convert a number into scientific number format (with a lower-case e)')
txt = "We have {:e} chickens."
print(txt.format(5))
print('Use "E" to convert a number into scientific number format (with an upper-case E)')
txt = "We have {:E} chickens."
print(txt.format(5))
print('Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals')
txt = "The price is {:.2f} dollars."
print(txt.format(45))
print('without the ".2" inside the placeholder, this number will be displayed like this')
txt = "The price is {:f} dollars."
print(txt.format(45))
print('Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN')
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
print('same example, but with a lower case f')
txt = "The price is {:f} dollars."
print(txt.format(x))
print('Use "%" to convert the number into a percentage format')
txt = "You scored {:%}"
print(txt.format(0.25))
print('Or, without any decimals:')
txt = "You scored {:.0%}"
print(txt.format(0.25))

'''
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

print('Check if all the characters in the text are alphanumeric:')
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)

print('Check if all the characters in the text are letters:')
txt = "CompanyX"
x = txt.isalpha()
print(x)
txt = "Company10"
x = txt.isalpha()
print(x)
print('Check if all the characters in the text are ascii characters:')
txt = "Company123"
x = txt.isascii()
print(x)
print('Check if all the characters in the unicode object are decimals:')
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())
print('Check if all the characters in the text are digits:')
txt = "50800"
x = txt.isdigit()
print(x)
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

print('The isidentifier() method returns True if the string is a valid identifier, otherwise False.\n\n A string is considered a valid identifier if it only contains\n alphanumeric letters (a-z) and (0-9), or underscores (_).\n A valid identifier cannot start with a number, or contain any spaces.')
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

print('Check if all the characters in the texts are in lower case:')
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

print('The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.\nExponents, like ² and ¾ are also considered to be numeric values.\n"-1" and "1.5" are NOT considered numeric values, because all the\n characters in the string must be numeric, and the - and the . are not.')
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

print('Check if all the characters in the text are printable:')
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
print('Check if all the characters in the text are whitespaces:')
txt = "   "
x = txt.isspace()
print(x)
txt = "   s   "
x = txt.isspace()
print(x)
print('The istitle() method returns True if all words in a text start with a\n upper case letter, AND the rest of the word are lower case letters,\n otherwise False.\nSymbols and numbers are ignored.')
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


myTuple = ("John","Peter","Vicky")
x = "#".join(myTuple)
print(x)
x = " ".join(myTuple)
print(x)

print('Join all items in a dictionary into a string, using a the word "TEST" as separator \n When using a dictionary as an iterable, the returned values are the keys, not the values')
myDict = {"name":"John","country":"Norway"}
mySeparator = "Test"
x = mySeparator.join(myDict)
print(x)

print('Return a 20 characters long, left justified version of the word "banana"')
txt = "banana"
x = txt.ljust(20)
print(x,'is my favourite fruit')
print('Using the letter "O" as the padding character')
txt = "banana"
x = txt.ljust(20, "0")
print(x)
print('Remove spaces to the left of the string')
txt = "      banana       "
x = txt.lstrip()
print('of all fruits',x,'is my favourite')

txt = ',,,,,,,,,,,,ssssaaaawww.....banana'
x = txt.lstrip(',saw.')
print(x)

print('Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character')
txt = "Hello Sam!"
mytable = txt.maketrans("S","P")
print(txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
z = "Hi "
mytable = txt.maketrans(x,y,z)
print(txt.translate(mytable))

print('Partition Method : \nSearch for the word "bananas", and return a tuple with three elements:\n1 - everything before the "match"\n2 - the "match"\n3 - everything after the "match"')
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print('If the specified value is not found, the partition() method returns a tuple\n containing: 1 - the whole string, 2 - an empty string, 3 - an empty string')
x = txt.partition ("apples")
print(x)

print('Replace the word "bananas"')
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

print('rfind method from last')
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
print('rindex() method \n rjust() method \n rpartition() method \n rsplit() method \n rstrip() method')
print('split() Method')
txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

print('splitlines() Method : \n Split a string into a list where each line is a list item')
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
x = txt.splitlines(True)
print(x)

print('startswith() Method \n Check if the string starts with "Hello"')
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

print('strip() Method \n Remove spaces at the beginning and at the end of the string')
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

print('swapcase() Method \n Make the lower case letters upper case and the upper case letters lower case')
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))


print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b>a:
	print("b is greater than a")
else:
	print("b is less than a")

print(bool("Hello"))
print(bool(15))

print('Most Values are True\nAlmost any value is evaluated to True if it has some sort of content.\nAny string is True, except empty strings.\nAny number is True, except 0.\n Any list, tuple, set, and dictionary are True, except empty ones.')
print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
	def __len__(self):
		return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x,int))

print(10+6)
print(10-6)
print(10*6)
print(10/6)
print(10%6)
print('To the power')
print(10**6)
print('the floor division // rounds the result down to the nearest whole number')
print(10//6)

print("Assignment Operaters")
x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x = 98
x %= 5
print(x)
x = 47
x //= 5
print(x)
x **= 3
print(x)
print('Bitwise nad')
x &= 3
print(x)
print('Bitwise OR')
x = 729
x |= 3
print(x)
print('Bitwise XOR')
x = 729
x ^= 3
print(x)
x = 79
print(~x)
x >>= 5
print(x)
x <<= 5
print(x)

print('Comaparision Operator')
x = 5
print(x == 6)
print(x != 7)
print(x > 10)
print(x < 10)
print(x >= 5)
print(x <= 4)

print('Logical Operators')
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

print('Identity Operators \n is \n Returns True if both variables are the same object')
x = ["apple","banana"]
y = ["apple","banana"]
z = x
print(x is y)
print(x is z)
print(x == y)

print("is not \n Returns True if both variables are not the same object")
print(x is not z)
print(x is not y)
print(x != y)

print('Menbership Operators \n in \n Returns True if a sequence with the specified value is present in the object \n is not \n Returns True if a sequence with the specified value is not present in the object')
x = ["apple","banana"]
print("banana" in x)
print("pineapple" not in x)


print('Lists are used to store multiple items in a single variable.\n Lists are created using square brackets \n List items are ordered, changeable, and allow duplicate values.\n List items are indexed, the first item has index [0], the second item has index [1] etc.\nIf you add new items to a list, the new items will be placed at the end of the list.\n')
mylist = ["apple","banana","cherry"]
print(mylist)
print("Append Method (ADD ElEMENT)")
fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
b = ["ford","BMW","Volvo"]
fruits.append(b)
print(fruits)

print("clear method\n remove all items in list")
fruits = ["apple","banana","cherry"]
fruits.clear()
print(fruits)

print('Copy Method\nCopy the fruits list')
fruits = ["apple","banana","cherry","Orange"]
x = fruits.copy()
print(x)

print('Another way of copy')
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print('COUNT METHOD\nReturn the number of times the value "cherry" appears in the fruits list')
fruits = ["apple","banana","cherry","Orange"]
x = fruits.count("cherry")
print(x)

print('Index Method\nposition of the value')
fruits = ["apple","banana","cherry","Orange"]
x = fruits.index("cherry")
print(x)

print('Extend Method \n Add the elements of cars to the fruits list')
fruits = ["apple","banana","cherry","Orange"]
cars = ["ford","BMW","Volvo"]
fruits.extend(cars)
print(fruits)
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

print('Insert Method\n insert element with position')
fruits = ["apple","banana","cherry"]
fruits.insert(1,"orange")
print(fruits)

print('Pop Method\nremove the element with position')
x = fruits.pop(1)
print(fruits)
print(x)

print('If you do not specify the index, the pop() method removes the last item.')
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print('Remove Method \n Remove the first occurence of the element with value')
fruits = ["apple","banana","cherry"]
fruits.remove("banana")
print(fruits)

print('del Keyword\nThe del keyword also removes the specified index:')
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print('The del keyword can also delete the list completely.')
thislist = ["apple", "banana", "cherry"]
#del thislist
#print(thislist)

print('Reverse Method')
fruits = ["apple","banana","cherry"]
fruits.reverse()
print(fruits)

print('Sort Method')
cars = ['Ford','BMW','Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print('Sort the list by the length of the values:')
def myFunc(e):
	return len(e)
cars = ["Ford","Mitsubishi","BMW","VW"]
cars.sort(key=myFunc)
print(cars)
print('Sort a list of dictionaries based on the "year" value of the dictionaries')
def myFunc1(e):
	return e['year']
cars = [
	{"car":"ford","year":2005},
	{"car":"Mitsubshi","year":2000},
	{"car":"BMW","year":2019},
	{"car":"VW","year":2011}]
cars.sort(key=myFunc1)

print(cars)

print('List Allow Duplicates')
thislist = ["apple","banana","cherry","apple","banana"]
print(thislist)

print('List Length')
print(len(thislist))

print('List items can be of any data type')
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

print('A list can contain different data types')
list1 = ["abc",34,True,40,"male"]
print(list1)

print("type()\nFrom Python's perspective,\n lists are defined as objects with the data type 'list': \n <class 'list'>")
print(type(list1))

print('It is also possible to use the list() constructor when creating a new list.\nUsing the list() constructor to make a List')
thislist = list(("apple","banana","cherry"))
print(thislist)

print('Python Collections (Arrays)\nThere are four collection data types in the Python programming language:\nList is a collection which is ordered and changeable. Allows duplicate members.\nTuple is a collection which is ordered and unchangeable. Allows duplicate members.\nSet is a collection which is unordered and unindexed. No duplicate members.\n Dictionary is a collection which is ordered* and changeable. No duplicate members.')
print('Access Items')
thislist = ["apple","banana","cherry"]
print(thislist[1])
print('Negative Indexing')
print(thislist[-1])
thislist = ["apple","banana","cherry","Orange","Kiwi","melon","mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[3:])
print(thislist[-4:-1])

if "apple" in thislist:
	print("yes, 'apple' is in this list ")
print('Change Item Value')
thislist[1] = "balckcurrant"
print(thislist)

print('Change a Range of Items Values')
thislist[1:3] = ["balckcurrant","watermelon"]
print(thislist)

print('If you insert more items than you replace, the new items will be inserted\n where you specified, and the remaining items will move accordingly')
thislist = ["apple","banana","cherry"]
thislist[1:2] = ["balckcurrant","watermelon"]
print(thislist)
print('If you insert less items than you replace, the new items will be inserted\n where you specified, and the remaining items will move accordingly')
thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print('Insert Items\nTo insert a new list item, without replacing any of the existing values, we can use the insert() method.')
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

print('Add Any Iterable\nThe extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)')
thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

print('The clear() method empties the list.\nThe list still remains, but it has no content.')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print('Loops throuh a list')
thislist = ['apple','banana','cherry']
for x in thislist:
	print(x)

print('Loops thorugh the index numbers\nUse the range() and len() functions to create a suitable iterable')
thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
	print(thislist[i])

print('using Wihle loop')
thislist = ["apple","banana","cherry"]
i = 0
while i < len(thislist):
	print(thislist[i])
	i=i+1

print('Looping Using List Comprehension\nshortest syntax for looping through lists')
thislist = ["apple","banana","cherry"]
[print(x) for x in thislist]

print('List Comprehension another example')
fruits = ["apple","banana","cherry","Kiwi","mango"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

print('syntax')
print('newlist = [expression for item in iterable if condition == True]')
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple","banana","cherry"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["Hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

def myFunc2(n):
	return abs(n - 50)

thislist = [100,50,65,82,23]
thislist.sort(key=myFunc2)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print('Join List')
list1 = ["a","b","c","d"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

list1.append(list2)
print(list1)
list1 = ["a","b","c","d"]
for x in list2:
	list1.append(x)
print(list1)

list1 = ["a","b","c","d"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)


print('Tuples\nA tuple is a collection which is ordered and unchangeable.\nTuples are written with round brackets.')
thistuple = ("apple","banana","cherry")
print(thistuple)
print('Tuples allow duplicate values\nTuples items are indexed')
print('Since tuples are indexed, they can have items with the same value')
thistuple = ("apple","banana","cherry","apple","cherry")
print(thistuple)
print(len(thistuple))
print('To create a tuple with only one item, you have to add a comma after the item,\n otherwise Python will not recognize it as a tuple.')
#NOT a tuple
thistuple = ("apple")
print(thistuple)
print(type(thistuple))

thistuple = ("apple",)
print(thistuple)
print(type(thistuple))

print('Tuple items can be of any data type')
tuple1 = ("apple","banana","cherry")
tuple2 = (1,2,56,89,65)
tuple3 = (True,False,True)
print(tuple1,tuple2,tuple3)

print('A tuple can contain different data types')
tuple1 = ("abc",34,True,40,"male")
print(tuple1)

print('tuple Constructor')
thistuple = (("apple","banana","cherry"))
print(thistuple)

print('Access Tuple Items')
thistuple = ("apple","banana","cherry","orange","kiwi","watermelon","mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
if "apple" in thistuple:
	print("yes ,'apple is there in tuple'")

print("Once a tuple is created, you cannot change its values.\nBut there is a workaround. You can convert the tuple into a list,\n change the list, and convert the list back into a tuple. ")
x = ("apple","banana","cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)

print(x)

print('Add Items')
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("Orange")
thistuple = tuple(y)
print(thistuple)

print('Add Items to Tuple \n Add tuple to a tuple.\n You are allowed to add tuples to tuples,\n so if you want to add one item, (or many), create a new tuple with the item(s),\n and add it to the existing tuple')
thistuple = ("apple","banana","cherry")
y = ("Orange",)
thistuple += y
print(thistuple)

print('Remove Items in Tuple\nTuples are unchangeable\nbut you can use the same workaround as\n we used for changing and adding tuple items')
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#print('OR you can delete tuple completely')
#thistuple = ("apple","banana","cherry")
#del thistuple
#print(thistuple)

print('Unpack Tuples\nWhen we create a tuple, we normally assign values to it.\n This is called "packing" a tuple')
fruits = ("apple","banana","cherry")
print(fruits)

print('But, in Python, we are also allowed to extract\n the values back into variables. This is called "unpacking"')
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green," ",yellow," ",red)

print('If the number of variables is less than the number of values,\n you can add an * to the variable name and\n the values will be assigned to the variable as a list')
fruits = ("apple","banana","cherry","Orange","strawberry","Raspberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)

(green,*yellow,red) = fruits
print(green)
print(yellow)
print(red)

print('Loops Through a Tuple')
thistuple = ("apple","banana","cherry")
for x in thistuple:
	print(x)

print('Loops thorough index numbers')
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
	print(thistuple[i])

print("Using While Loop")
thistuple = ("apple","banana","cherry")
i = 0
while i < len(thistuple):
	print(thistuple[i])
	i = i+1

print('Join Tuples')
tuple1 = ('a','b','c')
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

print("Multiply Tuples \n If you want to multiply the content of a tuple a given number of times, you can use the * operator")
fruits = ("apple","banana","cherry")
mytuple = fruits*2
print(mytuple)

print('Tuple Count Method\nReturn the number of times the value 5 appears in the tuple')
thistuple = (1,2,6,4,8,9,75,6,1,3,466)
x = thistuple.count(1)
print(x)

print("index method\nSearch for the first occurrence of the value 8, and return its position")
thistuple = (1,2,3,6,5,4,7,8,9,5,4,6,62,62,4,6484,0,481,1,8451,548,15,181)
x = thistuple.index(8)
print(x)


print('Python Sets\nA set is a collection which is both unordered and unindexed.\nSets are written with curly brackets.')
thisset = {"apple","banana","cherry"}
print(thisset,"\n")
print('Note: Sets are unordered, so you cannot be sure in which order the items will appear.\n')
print('Set items are unordered, unchangeable, and do not allow duplicate values.\n')

print('Sets cannot have two items with the same value.')
thisset = {"apple","banana","cherry","apple","banana"}
print(thisset)

print('length of set')
thisset = {"apple","banana","cherry"}
print(len(thisset))

print("Data Types\n Set items can be of any data type")
set1 = {"apple","banana","cherry"}
set2 = {1,5,6,7,9,4,3}
set3 = {True,False,True}
print(set1,set2,set3)

print('A set can contain different data types')
set1 = {"abc",34,True,40,"male"}
print(set1)
print('type of set')
print(type(set1))

print('Set Constructor')
thisset = set(("apple","banana","cherry"))
print(thisset)

print('Access Set items')
thisset = {"apple","banana","cherry"}
for x in thisset:
	print(x)
if "banana" in thisset:
	print("Banana is in Set")
print("banana" in thisset)

print("change items\nOnce a set is created, you cannot change its items, but you can add new items\n")
print('To add one item to a set use the add() method')
thisset = {"apple","banana","cherry"}
thisset.add("Orange")
print(thisset)

print('Add Sets\nTo add items from another set into the current set, use the update() method.')
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

print("Add Any Iterable\nThe object in the update() method does not have to be a set,\n it can be any iterable object (tuples, lists, dictionaries etc.).")
thisset = {"apple","banana","cherry"}
mylist = ["Kiwi","orange"]
thisset.update(mylist)
print(thisset)

print("REmove Item\n To remove an item in a set, use the remove(), or the discard() method.")
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("apple")
print(thisset)
print('Note: If the item to remove does not exist, remove() will raise an error.')
thisset.discard("pineapple")
print(thisset)
print('Note: If the item to remove does not exist, discard() will NOT raise an error.\n')

print("You can also use the pop() method to remove an item, but this method will remove the last item.\n Remember that sets are unordered, so you will not know what item that gets removed.\nThe return value of the pop() method is the removed item.")
thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(x)
print(thisset)

print('The clear() method empties the set:')
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)

#print('The del keyword will delete the set completely:')
#thisset = {"apple","banana","cherry"}
#del thisset
#print(thisset)

print('Loop Items')
thisset = {"apple","banana","cherry"}
for x in thisset:
	print(x)

print("Join Two Sets\nThere are several ways to join two or more sets in Python.\nYou can use the union() method that returns a new set containing all items from both sets,\n or the update() method that inserts all the items from one set into another")
print("\n The union() method returns a new set with all items from both sets:")
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

print('The update() method inserts the items in set2 into set1:')
set1.update(set2)
print(set1)

print('Note: Both union() and update() will exclude any duplicate items.')

print("Keep ONLY the Duplicates\nThe intersection_update() method will keep only the items that are present in both sets.")
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.intersection_update(y)
print(x)

print("The intersection() method will return a new set, that only contains the items that are present in both sets.")
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.intersection(y)
print(z)

print('Keep All, But NOT the Duplicates\nThe symmetric_difference_update() method will keep only the elements that are NOT present in both sets.')
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.symmetric_difference_update(y)
print(x)

print("The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.")
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.symmetric_difference(y)
print(z)

print("Difference Method \nReturn a set that contains the items that only exist in set x, and not in set y:")
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.difference(y)
print(z)

print('copy method')
fruits = {"apple","banana","cherry"}
x = fruits.copy()
print(x)

print('Difference Update method\nThe difference_update() method removes the items that exist in both sets.\nthe difference() method returns a new set, without the unwanted items,\n and the difference_update() method removes the unwanted items from the original set.')
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.difference_update(y)
print(x)

print('The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.')
x = {"apple","banana","cherry"}
y = {"google","microsoft","facebook"}

z = x.isdisjoint(y)
print(z)

print('issubset Method\nThe issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.')
x = {"a","b","c"}
y = {"f","e","d","c","b","a"}
z = x.issubset(y)
print(z)

print("issuperset Method\nThe issuperset() method returns True if all items in the specified set exists in the original set,\n otherwise it retuns False.")
x = {"f","e","d","c","b","a"}
z = x.issuperset(y)
print(z)

print('Python Dictionaries\nDictionaries are used to store data values in key:value pairs.\nA dictionary is a collection which is ordered*, changeable and does not allow duplicates.')
print("Dictionaries are written with curly brackets, and have keys and values:")
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
print(thisdict)
print(thisdict["brand"])

print('Dictionaries cannot have two items with the same key:\nDuplicate values will overwrite existing values')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964,
	"year": 2020
}
print(thisdict)
print(len(thisdict))

print('Data types')
thisdict = {
	"brand": "ford",
	"electric": "False",
	"year": 1964,
	"colors": ["red","white","blue"]
}

print(thisdict)
print(type(thisdict))

print('Access items')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

print('Get Keys\nThe keys() method will return a list of all the keys in the dictionary.')
x = thisdict.keys()
print(x)
thisdict["color"] = "white"
print(x)

print('get values')
x = thisdict.values()
print(x)

car = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

car["color"] = "red"
print(x)

print('Get Items\nThe items() method will return each item in a dictionary, as tuples in a list.')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
x = thisdict.items()
print(x)

thisdict["year"] = 2020
print(x)

thisdict["color"] = "red"
print(x)

if "model" in thisdict:
	print("yes,'model' is one of the keys in the thisdict dictionary")

print("Change Values")
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
thisdict["year"] = 2018
print(thisdict)

print("Update Dictionary")
thisdict.update({"year": 2020})
print(thisdict)

print("adding dict items")
thisdict = {
	'brand': "Ford",
	"model": "Mustang",
	"year": 1964
}
thisdict["color"] = "red"
print(thisdict)

print("update dictionary")
thisdict.update({'color': "white"})
print(thisdict)

print('Remove Items\nThere are several methods to remove items from a dictionary:\nThe pop() method removes the item with the specified key name:')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
thisdict.pop("model")
print(thisdict)

print("popitem method(REMOVE LAST ITEM)")
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
thisdict.popitem()
print(thisdict)

print('DEL keyword')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
del thisdict['model']
print(thisdict)

print('del keyword')
#del thisdict
#print(thisdict)

print('clear keyword')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
thisdict.clear()
print(thisdict)

print('Loop through a dictionary\nPrint all key names in the dictionary, one by one')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964,
	"color": "red"
}
for x in thisdict:
	print(x)

print("Print all values in the dictionary, one by one")
for x in thisdict:
	print(thisdict[x])

print('You can also use the values() method to return values of a dictionary:')
for x in thisdict.values():
	print(x)

print("You can use the keys() method to return the keys of a dictionary:")
for x in thisdict.keys():
	print(x)

print('Loop through both keys and values, by using the items() method:')
for x in thisdict.items():
	print(x)

print('copy dictionaries')
thisdict = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964,
	"color": 'red'
}
mydict = thisdict.copy()
print(mydict)

print("Another Way of copying\nMake a copy of a dictionary with the dict() function:")
mydict = dict(thisdict)
print(mydict)

print('Nested dictionaries')
myfamily = {
	"child1": {
	"name": "Emil",
	"year": 2014
	},
	"child2": {
	"name": "Tobias",
	"year": 2007
	},
	"child3": {
	"name": "linus",
	"year": 2011
	}
}
print(myfamily)

print('adding dicitonaries to dictionaries')
child1 = {
	"name": "emil1",
	"year": 2005
}
child2 = {
	"name": "Tobias1",
	"year": 2008
}
child3 = {
	"name": "linus1",
	"year": 2012
}
myfamily1 = {
	"child1": child1,
	"child2": child2,
	"child3": child3
}
print(myfamily1)

print("Fromkeys method\nThe fromkeys() method returns a dictionary with the specified keys and the specified value.")
print('without specifying the value')
x = ('key1','key2','key3')
thisdict = dict.fromkeys(x)
print(thisdict)

print('Create a dictionary with 3 keys, all with the value 0:')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)


print("Conditions And IF statements\nPython supports the usual logical conditions from mathematics:\nEquals: a == b\nNot Equals: a != b\nLess than: a < b\nLess than or equal to: a <= b\nGreater than: a > b\nGreater than or equal to: a >= b")
print("if Statement\nELIF STATEMENT\nElse Statement")
a = 33
b = 20
if b > a:
	print("b is Greater than a")
elif a == b:
	print("a is equal to b")
else:
	print("a is Greater than b")

print('Shorthand IF')
a = 30
b = 20
if a > b: print("a is Greater than b")

print('Shorthand IF ... Else')
a = 2
b = 330
print("A>B") if a > b else print("B>A")

print('One line if else statement, with 3 conditions')
a = 330
b = 330
print("A>B") if a > b else print("A=B") if a == b else print("B>A")

print("AND operator")
a = 200
b = 33
c = 500
if a > b and c > a:
	print("Both Conditions are True")

print('OR operator')
a = 200
b = 33
c = 500
if a > b or b > c:
	print("At least one of the condition is True")

print("nested if")
x = 41

if x > 10:
	print("Above ten")
	if x > 20:
		print("Also Above 20")
	else:
		print("But not Above 20")

print("Pass Statement\nif statements cannot be empty, but if you for some reason have an if statement with no content,\n put in the pass statement to avoid getting an error.")
a = 33
b = 200
if b > a:
	pass

print("While Loops")
i = 1
while i < 6:
	print(i)
	i = i + 1

print("Break Statement")
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i = i + 1

print("Continue Statement\n Only 3 is not printed")
i = 0
while i < 6:
	i = i + 1
	if i == 3:
		continue
	print(i)

print("esle Statement for While Loops")
i = 1
while i < 6:
	print(i)
	i = i + 1
else:
	print("i is no longer less then 6")

print('For Loops')
fruits = ["apple","banana","cherry"]
for x in fruits:
	print(x)

print("Loop through a String")
for x in "banana":
	print(x)

print('Break in For loop')
fruits = ["apple","banana","cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break

print('Break before banana comes')
fruits = ["apple","banana","cherry"]
for x in fruits:
	if x == "banana":
		break
	print(x)

print("Skip banana Using CONTINUE statement")
fruits = ["apple","banana","cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)

print('Range Function\nNote that range(6) is not the values of 0 to 6, but the values 0 to 5.')
for x in range(6):
	print(x)

print("using the start parameter in range function\nrange(2, 6), which means values from 2 to 6 (but not including 6):")
for x in range(2,6):
	print(x)

print('The range() function defaults to increment the sequence by 1,\n however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):')
for x in range(2,40,4):
	print(x)

print("else in for loop\nNote: The else block will NOT be executed if the loop is stopped by a break statement.")
for x in range(6):
	print(x)
else:
	print("Finally finished")

print("using Break in else in for loop")
for x in range(6):
	if x == 3:
		break
	print(x)
else:
	print("Finally finished")

print('nested Loops')
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
	for y in fruits:
		print(x,y)

print("pass statements\nfor loops cannot be empty, but if you for some reason have a for loop with no content,\n put in the pass statement to avoid getting an error.")
for x in [0,1,2]:
	pass

print('Python Functions\nA function is a block of code which only runs when it is called.\nYou can pass data, known as parameters, into a function.\nA function can return data as a result.')
print("creating a Function\nIn Python a function is defined using the def keyword:")
def my_function():
	print("hello from a function")
my_function()

print("Arguments\nInformation can be passed into functions as arguments.\nArguments are specified after the function name, inside the parentheses.")
def my_function1(fname):
	print(fname + " Google")
my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

print('Arguments are often shortened to args in Python documentations.')
print('A parameter is the variable listed inside the parentheses in the function definition.\nAn argument is the value that is sent to the function when it is called.')

def my_function2(fname,lname):
	print(fname+" "+lname)
my_function2("Emil","google")
print('your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.')
#my_function2("Emil")


print('\nArbitrary Arguments, *args\n\nIf you do not know how many arguments that will be passed into your function,\n add a * before the parameter name in the function definition.\n\nThis way the function will receive a tuple of arguments, and can access the items accordingly:')
print('If the number of arguments is unknown, add a * before the parameter name:')
def my_function3(*kids):
	print("The youngest child is "+kids[2])
my_function3("Emil","Tobias","Linus")
print('\nArbitrary Arguments are often shortened to *args in Python documentations.\n')


print("Keyword Arguments\nYou can also send arguments with the key = value syntax.\nThis way the order of the arguments does not matter.")
def my_function4(child3,child2,child1):
	print("The youngest child is "+ child3)
my_function4(child1 = "Emil",child2 ="Tobias",child3 ="Linus")
print('\nThe phrase Keyword Arguments are often shortened to kwargs in Python documentations.')

print("\nArbitrary Keyword Arguments, **kwargs\nIf you do not know how many keyword arguments that will be passed into your function,\n add two asterisk: ** before the parameter name in the function definition.\nThis way the function will receive a dictionary of arguments, and can access the items accordingly:")
print('\nIf the number of keyword arguments is unknown, add a double ** before the parameter name:')
def my_function5(**kid):
	print("His last name is "+ kid["lname"])
my_function5(fname = "Tobias",lname = "Google")
print("\nArbitrary Kword Arguments are often shortened to **kwargs in Python documentations.\n")

print("Default Parameter Value\nIf we call the function without argument, it uses the default value:")
def my_function6(country = "Norway"):
	print('I am from '+country)
my_function6("sweden")
my_function6()
my_function6("India")
my_function6("Brazil")

print('Passing a List as an Argument\nYou can send any data types of argument to a function (string, number, list, dictionary etc.),\n and it will be treated as the same data type inside the function.')
def my_function7(food):
	for x in food:
		print(x)
fruits = ["apple","banana","cherry"]
my_function7(fruits)

print("Return Values")
def my_function8(x):
	return 5 * x
print(my_function8(10))
print(my_function8(7))
print(my_function8(3))

print("pass statement")
def my_function9():
	pass
my_function9()

print("Recursion\nfunction can call itself.")
def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecursion Example Results")
tri_recursion(15)


print("Python Lambda\nA lambda function is a small anonymous function.\nA lambda function can take any number of arguments, but can only have one expression.\n")
print('Syntax :\nlambda arguments : expression')
print("\nAdd 10 to argument a, and return the result:")
x = lambda a : a + 10
print(x(5))
print('Lambda functions can take any number of arguments:')
x = lambda a,b: a*b
print(x(5,6))
print("with three arguents")
x = lambda a,b,c: a + b + c
print(x(5,6,2))

print("Why Use Lambda Functions?\nThe power of lambda is better shown when you use them as an anonymous function inside another function.\nSay you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:")
def myfunc(n):
	return lambda a : a * n
print('\nUse that function definition to make a function that always doubles the number you send in:')
mytripler = myfunc(3)
mydoubler = myfunc(2)
print(mydoubler(11))
print("\nuse the same function definition to make a function that always triples the number you send in")
print(mytripler(11))
print("\nuse the same function definition to make both functions, in the same program")

print('\nPython Arrays\nNote: Python does not have built-in support for Arrays, but Python Lists can be used instead.\nArrays are used to store multiple values in one single variable:')
cars = ["Ford","Volvo","BMW"]
print(cars)
print("Access Array elements")
x = cars[0]
print(x)
print("modify Array")
cars[0] = "Toyato"
print(cars)
print("length of an array")
x = len(cars)
print(x)
print("Looping Array Elements\nFor Loop")
for x in cars:
	print(x)
print("adding Array Elements\nUsing Append() Method")
cars.append("Honda")
print(cars)
print('Remove Array Elements\n Using POP() Method')
cars.pop(1)
print(cars)
print("Remove Array Elements\n Using Remove() Method")
cars.remove("BMW")
print(cars)
print("Clearing Array")
cars.clear()
print(cars)
print("copy Of array")
fruits = ["apple","banana","cherry","orange"]
x = fruits.copy()
print(x)
print("Extend method\nThe extend() method adds the specified list elements (or any iterable) to the end of the current list.")
cars = ["Ford","BMW","Volvo"]
fruits.extend(cars)
print(fruits)

print("\nPython Classes / Objects\nPython is an object oriented programming language.\nAlmost everything in Python is an object, with its properties and methods.\nA Class is like an object constructor, or a 'blueprint' for creating objects.")
print("creating a class")
class MyClass:
	x = 5
print(MyClass)
print("\nCreate Object\nNow we can use the class named MyClass to create objects\nCreate an object named p1, and print the value of x")
p1 = MyClass()
print(p1.x)

print("\nThe __init__() Function\nTo understand the meaning of classes we have to understand the built-in __init__() function.\nAll classes have a function called __init__(), which is always executed when the class is being initiated.\nUse the __init__() function to assign values to object properties,\n or other operations that are necessary to do when the object is being created")
print("Create a class named Person, use the __init__() function to assign values for name and age")
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
p1 = Person("John",36)
print(p1.name)
print(p1.age)
print("\nThe __init__() function is called automatically every time the class is being used to create a new object.")

print('\n Object Methods\nObjects can also contain methods. Methods in objects are functions that belong to the object.')
print('\nInsert a function that prints a greeting, and execute it on the p1 object\n')
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is "+ self.name)
p1 = Person("John",36)
p1.myfunc()
print("\nThe self Parameter \nThe self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.")
print('\nIt does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class')
print('Use the words mysillyobject and abc instead of self')
class Person1:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age
	def myfunc(abc):
		print("Hello my name is "+ abc.name)
p1 = Person1("John",36)
p1.myfunc()

print("Modify Object Properties")
p1.age = 40
print(p1.age)

print("Delete Object Properties")
#del p1.age
print(p1.age)

print("Delete Objects")
print(p1)
del p1
#print(p1)

print("pass statement")
class Person:
	pass

print("\nPython Inheritance\nInheritance allows us to define a class that inherits all the methods and properties from another class.\nParent class is the class being inherited from, also called base class.\nChild class is the class that inherits from another class, also called derived class.")
print('Create a Parent Class\nAny class can be a parent class, so the syntax is the same as creating any other class:')

class Person2:
	def __init__(self,fname,lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
x = Person2("John","Doe")
x.printname()

print("Create a Child Class\nTo create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:")
print('Note: Use the pass keyword when you do not want to add any other properties or methods to the class.\n\nNow the Student class has the same properties and methods as the Person class.')

class Student(Person2):
	pass
x = Student("Mike","Olsen")
x.printname()

print("\nAdd the __init__() Function\nwe have created a child class that inherits the properties and methods from its parent.\nWe want to add the __init__() function to the child class (instead of the pass keyword).\n\nThe __init__() function is called automatically every time the class is being used to create a new object.")
print("\nWhen you add the __init__() function, the child class will no longer inherit the parent's __init__() function.\nNote: The child's __init__() function overrides the inheritance of the parent's __init__() function\n\nTo keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:")
class Student1(Person2):
	def __init__(self,fname,lname):
		Person2.__init__(self,fname,lname)
z = Student1("Mike","Olsen")
x.printname()
print("\nNow we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.")

print("Use Super() Function\nPython also has a super() function that will make the child\n class inherit all the methods and properties from its parent:")
class Student2(Person2):
	def __init__(self,fname,lname):
		super().__init__(fname,lname)
i = Student2("Mike","Olsen")
i.printname()

print("Adding Properties")
class Student3(Person2):
	def __init__(self,fname,lname):
		super().__init__(fname,lname)
		self.graduationyear = 2019
x = Student3("Mike","Olsen")
print(x.graduationyear)

print(" add another parameter in the __init__() function")
class Student4(Person2):
	def __init__(self,fname,lname,year):
		super().__init__(fname,lname)
		self.graduationyear = year
y = Student4("Mike","Olsen",2019)
print(y.graduationyear)

class Student5(Person2):
	def __init__(self,fname,lname,year):
		super().__init__(fname,lname)
		self.graduationyear = year
	def welcome(self):
		print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
x = Student5("Mike","Olsen",'2019')
x.welcome()


print("Python Iterators\nAn iterator is an object that contains a countable number of values.\nAn iterator is an object that can be iterated upon, meaning that you can traverse through all the values.\nTechnically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().")
print("\nIterator vs Iterable\nLists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.\nAll these objects have a iter() method which is used to get an iterator")
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

print("Even Strings are iterable")
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("Create an Iterator\nTo create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.\nAs you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.\nThe __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.\nThe __next__() method also allows you to do operations, and must return the next item in the sequence.")
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
	print(x)

print("python Scope\nLocal Scope\nA variable created inside a function belongs to the local scope of that function, and can only be used inside that function.")
def myfunc():
	x = 300
	print(x)
myfunc()

print('function inside function\nthe variable x is not available outside the function, but it is available for any function inside the function')
def myfunc():
	x = 300
	def myinnerfunc():
		print(x)
	myinnerfunc()
myfunc()

print("global Scope\nA variable created in the main body of the Python code is a global variable and belongs to the global scope.")
x = 300
def myfunc():
	print(x)
myfunc()
print(x)

print("Naming Variables")
x = 300
def myfunc():
	x = 200
	print(x)
myfunc()
print(x)

x = 200
print("Global Keyword\nThe global keyword makes the variable global.")
def myfunc():
	global w
	w = 300
myfunc()
print(w)

print("Python Modules\nConsider a module to be the same as a code library.\nA file containing a set of functions you want to include in your application.")
print("Create a Module\nTo create a module just save the code you want in a file with the file extension .py\ndef greeting(name):\n  print('Hello, ' + name)\nSave this code in a file named mymodule.py")
print("Use a Module\nwe can use the module we just created, by using the import statement")
import mymodule
mymodule.greeting("Jonathan")

print("Variables in Module\nThe module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)")
a = mymodule.person1["age"]
print(a)

print("\nNaming a Module\nYou can name the module file whatever you like, but it must have the file extension .py\nRe-naming a Module\nYou can create an alias when you import a module, by using the as keyword:")
print("Create an alias for mymodule called mx:")
import mymodule as mx

a = mx.person1["age"]
print(a)

print("Built-in Modules\nThere are several built-in modules in Python, which you can import whenever you like.")
print("Import and use the platform module:")
import platform
y = platform.system()
print(y)

print("Using the dir() Function\nThere is a built-in function to list all the function names (or variable names) in a module. The dir() function")
import platform
y = dir(platform)
print(y)
print("The dir() function can be used on all modules, also the ones you create yourself.")

print("\nImport From Module\nYou can choose to import only parts from a module, by using the from keyword.")
from mymodule import person1
print(person1["age"])

print('When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]')



print("python Datetime\n Dates : ")
import datetime
x = datetime.datetime.now()
print(x)

print('date output\nThe datetime module has many methods to return information about the date object.\nReturn the year and name of weekday:')
print(x.year)
print(x.strftime("%A"))

print("Creating Date Objects\nTo create a date, we can use the datetime() class (constructor) of the datetime module.\nThe datetime() class requires three parameters to create a date: year, month, day.")
import datetime
x = datetime.datetime(2020,5,17)
print(x)

print("strftime() Method\nThe datetime object has a method for formatting date objects into readable strings.\nThe method is called strftime(), and takes one parameter, format, to specify the format of the returned string")
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))
print(x.strftime("%a"),"      week shotday") 
print(x.strftime("%A"), "     week Full version")
print(x.strftime("%w"), "     weekday as a number 0-6,0 is sunday")
print(x.strftime("%d"), "     today numberdate")
print(x.strftime("%b"), "     month name short")
print(x.strftime("%B"), "     month Full Name")
print(x.strftime("%m"), "     month as a number")
print(x.strftime("%y"), "     YEAR SHORTCUT VERSION")
print(x.strftime("%Y"), "     year Full")
print(x.strftime("%H"), "     Hour 00-23")
print(x.strftime("%I"), "     Hour 00-12")
print(x.strftime("%p"), "     AM/PM")
print(x.strftime("%M"), "     Minutes")
print(x.strftime("%S"), "     Seconds")
print(x.strftime("%f"), "     Microsecond")
print(x.strftime("%z"), "     UTC offset")
print(x.strftime("%Z"), "     Timezone")
print(x.strftime("%j"), "     no of days in year")
print(x.strftime("%U"), "     Week no of the year(Sunday as first day of week)")
print(x.strftime("%W"), "     Week no of the year(Monday as first day of week)")
print(x.strftime("%c"), "     Local Version of date and time")
print(x.strftime("%x"), "     Local version of date")
print(x.strftime("%X"), "     Local version of time")
print(x.strftime("%%"), "     A % character")
print(x.strftime("%G"), "     ISO 8601 YEAR")
print(x.strftime("%u"), "     ISO 8601 weekday (1-7)")
print(x.strftime("%V"), "     ISO 8601 weeknumber (01-53)")

print("Python Math\nPython has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.")
x = min(5,10,15,20,25)
y = max(5,10,15,20,25)
print("Min Number : ",x)
print("Max Number : ",y)

print("\nThe abs() function returns the absolute (positive) value of the specified number")
x = abs(-7.25)
print(x)
print("\nThe pow(x, y) function returns the value of x to the power of y.")
x = pow(4,3)
print(x)

print("The Math Module\nPython has also a built-in module called math, which extends the list of mathematical functions.\nWhen you have imported the math module\nThe math.sqrt() method for example, returns the square root of a number")
import math
x = math.sqrt(64)
print(x)

print("The math.ceil() method rounds a number upwards to its nearest integer,\n and the math.floor() method rounds a number downwards to its nearest integer")
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

print("The math.pi constant, returns the value of PI (3.14...)")
x = math.pi
print(x)

print("There is MATH MODULE METHODS Reference in W3schools see there")



print("Python JSON\nJSON is a syntax for storing and exchanging data.\nJSON is text, written with JavaScript object notation.")
print("JSON in Python\nPython has a built-in package called json, which can be used to work with JSON data.")
print("\nConvert from Python to JSON\nIf you have a Python object, you can convert it into a JSON string by using the json.dumps() method.")
import json
x = {
	"name": "John",
	"age": 30,
	"city": "New York"
}

#convert into JSON
y = json.dumps(x)
print(y)

print("\nConvert from JSON to Python\nIf you have a JSON string, you can parse it by using the json.loads() method.")
import json

#Some JSON:
x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x:
y = json.loads(x)

#the result is a python dictionary:
print(y["age"])

print("convert Python objects of the following types, into JSON strings:\ndict,list,tuple,string,int,float,True,False,None")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\nPython objects are converted into the JSON (JavaScript) equivalent\nConvert a Python object containing all the legal data types")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = print(json.dumps(x))
print(y)
print("\nJSON string, but it is not very easy to read, with no indentations and line breaks.\nThe json.dumps() method has parameters to make it easier to read\nUse the indent parameter to define the numbers of indents\n\n You can also define the separators, default value is (', ', ': '), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values\nUse the sort_keys parameter to specify if the result should be sorted or not")
print("\nPython Indentation\nIndentation refers to the spaces at the beginning of a code line.")
print(json.dumps(x, indent=1))
print("Separators Method")
print(json.dumps(x, indent=2, separators=(". "," = ")))
print("Sorting Method")
print(json.dumps(x, indent=4,separators=("."," = "), sort_keys=True))


print("Python RegEx\nRegular Expression, is a sequence of characters that forms a search pattern.\nRegEx can be used to check if a string contains the specified search pattern.")
print("\nRegEx Module\nPython has a built-in package called re, which can be used to work with Regular Expressions.")
print("\nSearch the string to see if it starts with 'The' and ends with 'Spain'")
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
if x:
	print("YES! We have a match!")
else:
	print("No Match")
#print(x)

print("RegEx Functions\nThe findall() Function\nThe findall() function returns a list containing all matches.")
x = re.findall("ai",txt)
print(x)
x = re.findall("Portugal", txt)
print(x)
print("The list contains the matches in the order they are found.\nIf no matches are found, an empty list is returned")

print("\nThe search() Function\nThe search() function searches the string for a match, and returns a Match object if there is a match.\nIf there is more than one match, only the first occurrence of the match will be returned")
x = re.search("a",txt)
print("The first a character is located in position:",x.start())
x = re.search("\s",txt)
print("The first white-space character is located in position:",x.start())
x = re.search("Portugal",txt)
print(x)

print("The split() Function\nThe split() function returns a list where the string has been split at each match")
x = re.split("\s",txt)
print(x)
print("ou can control the number of occurrences by specifying the maxsplit parameter\nSplit the string only at the first occurrence")
x = re.split("\s",txt,1)
print(x)

print("The sub() Function\nThe sub() function replaces the matches with the text of your choice")
x = re.sub("\s","\n",txt)
print(x)
print("You can control the number of replacements by specifying the count parameter")
x = re.sub("\s","0",txt,2)
print(x)

print("Match Object\nA Match Object is an object containing information about the search and the result\n\nIf there is no match, the value None will be returned, instead of the Match Object")
x = re.search("ai",txt)
print(x)
print("Span() Method\nPrint the position (start- and end-position) of the first match occurrence. ")
x = re.search(r"\bS\w+",txt)
print(x.span())
print(".string returns the string passed into the function")
print(x.string)
print(".group() returns the part of the string where there was a match")
print(x.group())

print("Metacharacters properties with special meaning\n search a set of characters")
x = re.findall("[a-m]",txt)
print(x)

txt = "That will be 59 dollars"
print("Signala special sequence")
x = re.findall("\d",txt)
print(x)

print("Start with")
txt = "Hello World"
x = re.findall("He..o",txt)
print(x)

print("Ends With")
txt = "hello world"
x = re.findall("^hello",txt)
if x:
	print("Yes,the string starts with 'hello'")
else:
	print("No match")

print("Zero or more occurrences")
txt = "The rain in Spain falls mainly in the plain!"
#check if the string contains "ai" followed by 0 or more "x" characters :
x = re.findall("aix*",txt)
print(x)

print("one or more occurrences")
x = re.findall("aix+",txt)
print(x)

print("Exactly the specified number of occurrences")
x = re.findall("al{2}",txt)
print(x)

print("Either or")
x = re.findall("falls|stays",txt)
print(x)

print("Special Sequences\nReturns a match if the specified characters are at the beginning of the string")
x = re.findall("\AThe",txt)
print(x)

print("Returns a match where the specified characters are at the beginning or at the end of a word")
x = re.findall(r"\bain",txt)
y = re.findall(r"ain\b",txt)
print(x)
print(y)

print("Check if 'ain' is present, but NOT at the beginning of a word")
x = re.findall(r"\Bain",txt)
print(x)

print("Return a match at every no-digit character")
x = re.findall("\D",txt)
print(x)

print("Return a match at every white-space character")
x = re.findall("\s",txt)
print(x)

print("Return a match at every NON white-space character")
x = re.findall("\S",txt)
print(x)

print("Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)")
x = re.findall("\w",txt)
print(x)

print("Return a match at every NON word character (characters NOT between a and Z. Like '!', '?'' white-space etc.)")
x = re.findall("\W",txt)
print(x)

print("Check if the string ends with 'Spain':")
x = re.findall("Spain\Z",txt)
print(x)

print("SETS\nReturns a match where one of the specified characters (a, r, or n) are present")
x = re.findall("[arn]",txt)
print(x)

print('Check if the string has other characters than a, r, or n')
x = re.findall("[^arn]",txt)
print(x)

print("Check if the string has any 0, 1, 2, or 3 digits")
x = re.findall("[0123]",txt)
print(x)

print("Check if the string has any two-digit numbers, from 00 to 59")
txt = "8 Times before 11:45 AM"
x = re.findall("[0-5][0-9]",txt)
print(x)

x = re.findall("[:]",txt)
print(x)



print("PIP\nPIP is a package manager for Python packages, or modules if you like.")
print("\nA package contains all the files you need for a module.\nModules are Python code libraries you can include in your project.")
#install camelcase using pip in command prompt
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))


print("Python Try Expect\nThe try block lets you test a block of code for errors.\nThe except block lets you handle the error.\nThe finally block lets you execute code, regardless of the result of the try- and except blocks.")
print("\nException Handling\nWhen an error occurs, or exception as we call it, Python will normally stop and generate an error message.\nThese exceptions can be handled using the try statement")
try:
	print(x)
except:
	print("An exception occured")

print("\nMany Exceptions\nYou can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error")
try:
	print(x)
except NameError:
	print("Variable is not defined")
except:
	print("Something else went wrong")

print("\nElse\nYou can use the else keyword to define a block of code to be executed if no errors were raised")
try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

print("\nFinally\nThe finally block, if specified, will be executed regardless if the try block raises an error or not.")
try:
	print(x)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")

print('This can be useful to close objects and clean up resources')
#try:
#	f = open("demofile.txt")
#	f.write("Lorum Ipsum")
#except:
#	print("Something went wrong when writing to the file")
#finally:
#	f.close()

print("\nRaise an exception\nAs a Python developer you can choose to throw an exception if a condition occurs.\nTo throw (or raise) an exception, use the raise keyword.")
#x = -1
#if x < 0:
#	raise Exception("Sorry, no numbers below zero")

print("The raise keyword is used to raise an exception.\nYou can define what kind of error to raise, and the text to print to the user.")
#x = "hello"
#if not type(x) is int:
#	raise TypeError("Only integers are allowed")

print("Python User Input\nPython allows for user input.\nThat means we are able to ask the user for input.\nThe method is a bit different in Python 3.6 than Python 2.7.\nPython 3.6 uses the input() method.\nPython 2.7 uses the raw_input() method.")
username = input("Enter Username : ")
print("Username is : " + username)

print("String Formatting\nstring will display as expected, we can format the result with the format() method.\n\nString format()\nThe format() method allows you to format selected parts of a string.\nSometimes there are parts of a text that you do not control, maybe they come from a database, or user input?\nTo control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:2f} dollars"
print(txt.format(price))
txt = "For only {price:.2f} dollars"
print(txt.format(price = 49))

print("The format() method formats the specified value(s) and insert them inside the string's placeholder.\nThe placeholder is defined using curly brackets: {}.")

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print("\nNamed Indexes")
print(txt1)
print("Numbered Indexes")
print(txt2)
print("Empty Placeholders")
print(txt3)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity,itemno,price))

print("Python File Handling\nFile handling is an important part of any web application.\nPython has several functions for creating, reading, updating, and deleting files. ")
print('\nThe key function for working with files in Python is the open() function.\nThe open() function takes two parameters; filename, and mode.\n\nThere are four different methods (modes) for opening a file:\n"r" - Read - Default value. Opens a file for reading, error if the file does not exist\n"a" - Append - Opens a file for appending, creates the file if it does not exist\n"w" - Write - Opens a file for writing, creates the file if it does not exist\n"x" - Create - Creates the specified file, returns an error if the file exists\n\nIn addition you can specify if the file should be handled as binary or text mode\n"t" - Text - Default value. Text mode\n"b" - Binary - Binary mode (e.g. images)')
f = open("E:\learning\webpages\HTML\Python\demofile.txt","rt")
print(f.read())

print("Read Only Parts of the File\nBy default the read() method returns the whole text, but you can also specify how many characters you want to return")
f = open("E:\learning\webpages\HTML\Python\demofile.txt","r")
print(f.read(5))

print("Read Lines\nYou can return one line by using the readline() method")
f = open("E:\learning\webpages\HTML\Python\demofile.txt","r")
print(f.readline())
print(f.readline())

print("Loopinf the lines in files for print")
f = open("E:\learning\webpages\HTML\Python\demofile.txt","r")
for x in f:
	print(x)

print("Close Files\nIt is a good practice to always close the file when you are done with it.")
f.close()
#print(f.read())

print('Python File Write\nWrite to an Existing File\nTo write to an existing file, you must add a parameter to the open() function:\n"a" - Append - will append to the end of the file\n"w" - Write - will overwrite any existing content')
f = open("E:\learning\webpages\HTML\Python\demofile.txt","a")
#f.write("Think First and Talk")
f.close()

#open and read the file after the appending:
f = open("E:\learning\webpages\HTML\Python\demofile.txt","r")
print(f.read())
f.close()

print('the "w" method will overwrite the entire file.')
f = open("E:\learning\webpages\HTML\Python\demofile.txt","w")
f.write("Oops! content is overwrite")
f.close()
f = open("E:\learning\webpages\HTML\Python\demofile.txt","r")
print(f.read())

print('Create a New File\nTo create a new file in Python, use the open() method, with one of the following parameters:\n"x" - Create - will create a file, returns an error if the file exist\n"a" - Append - will create a file if the specified file does not exist\n"w" - Write - will create a file if the specified file does not exist')
#f = open("myfile.txt","x")
f.close()
#Error file exists
#f = open("myfile.txt","x")

print("Create a new file if it does not exist:")
#f = open("myfile.txt","w")
#f.close()

print("Delete a File\nTo delete a file, you must import the OS module, and run its os.remove() function:")
import os
#if os.path.exists("myfile.txt"):
#	os.remove("myfile.txt")
#else:
#	print("the file does not exist")

#print('\nDelete Folder\nTo delete an entire folder, use the os.rmdir() method:\nimport os\nos.rmdir("myfolder")\n\nYou can only remove empty folders.')
'''
