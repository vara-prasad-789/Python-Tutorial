import numpy as np

print("NumPy Tutorial")
print('NumPy is a Python library.\nNumPy is used for working with arrays.\nNumPy is short for "Numerical Python".')
print("\nIt also has functions for working in domain of linear algebra, fourier transform, and matrices.\nNumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.")
print("\nWhy Use NumPy?\nIn Python we have lists that serve the purpose of arrays, but they are slow to process.\nNumPy aims to provide an array object that is up to 50x faster than traditional Python lists.\nThe array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.\nArrays are very frequently used in data science, where speed and resources are very important.")
print("\nData Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.")
print("\nWhy is NumPy Faster Than Lists?\nNumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.\nThis behavior is called locality of reference in computer science.\nThis is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.")
print("\nWhich Language is NumPy written in?\nNumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.")
print("\nInstallation of NumPy\npip install numpy")
print("Array numbers")

arr = np.array([1,2,3,4,5,6])
print(arr)

print("NumPy as np\nNumPy is usually imported under the np alias.")

arr = np.array([1,2,6,5,4,9,8,7,3])
print(arr)

print("Checking NumPy Version")
print(np.__version__)

print('NumPy Creating Arrays\nCreate a NumPy ndarray Object\nNumPy is used to work with arrays. The array object in NumPy is called ndarray.\nWe can create a NumPy ndarray object by using the array() function.')

print("\nNumPy Creating Arrays")
print("Create a NumPy ndarray Object\nNumPy is used to work with arrays. The array object in NumPy is called ndarray.\nWe can create a NumPy ndarray object by using the array() function.")
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print("To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:")
arr = np.array((1,2,3,4,5))
print(arr)

print("Dimensions in Arrays\nA dimension in arrays is one level of array depth (nested arrays).\nnested array: are arrays that have arrays as their elements.")
print("\n0-D Arrays\n0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.")
arr = np.array(42)
print(arr)
print(type(arr))

print("1-D Arrays\nAn array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.")
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print("NumPy has a whole sub module dedicated towards matrix operations called numpy.mat")
print("\n2-D Arrays\nAn array that has 1-D arrays as its elements is called a 2-D array.")
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))

print("\n3-D arrays\nAn array that has 2-D arrays (matrices) as its elements is called 3-D array.")
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr)

print("\nCheck Number of Dimensions?\nNumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.")
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.ndim,"\n",b.ndim,"\n",c.ndim,"\n",d.ndim)

print("Higher Dimensional Arrays\nAn array can have any number of dimensions.\nWhen the array is created, you can define the number of dimensions by using the ndmin argument.")
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print('number of dimensions : ',arr.ndim)

print("NumPy Array Indexing\nAccess Array Elements\nArray indexing is the same as accessing an array element.\nYou can access an array element by referring to its index number.\nThe indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.")
arr = np.array([1,2,3,4])
print(arr[0],arr[1],arr[2]+arr[3])

print("Access 2-D Arrays\nTo access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.")
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1],arr[1,3],arr[1,4])

print("Access 3-D Arrays\nTo access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.")
arr = np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])

print("Negative Indexing\nUse negative indexing to access an array from the end.")
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,-1])

print("NumPy Array Slicing\nSlicing in python means taking elements from one given index to another given index.\nWe pass slice instead of index like this: [start:end].\nWe can also define the step, like this: [start:end:step].\nIf we don't pass start its considered 0\nIf we don't pass end its considered length of array in that dimension\nIf we don't pass step its considered 1")
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print("\nNote: The result includes the start index, but excludes the end index.\n")
print(arr[4:])
print(arr[:6])
print(arr[-3:-1])
print("STEP\nUse the step value to determine the step of the slicing:")
print(arr[0:5:2])
print(arr[::2])

print("Slicing 2-D Arrays")
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
print(arr[0:2,2])
print(arr[0:2, 1:4])

print("\nNumPy Data Types\nData Types in Python\nBy default Python have these data types:\nstrings - used to represent text data, the text is given under quote marks. e.g. 'ABCD'\ninteger - used to represent integer numbers. e.g. -1, -2, -3\nfloat - used to represent real numbers. e.g. 1.2, 42.42\nboolean - used to represent True or False.\ncomplex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j")
print("\nData Types in NumPy\nNumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.\nBelow is a list of all data types in NumPy and the characters used to represent them.\ni - integer\nb - boolean\nu - unsigned integer\nf - float\nc - complex float\nm - timedelta\nM - datetime\nO - object\nS - string\nU - unicode string\nV - fixed chunk of memory for other type ( void )")
print("\nChecking the Data Type of an Array\nThe NumPy array object has a property called dtype that returns the data type of the array:")
arr = np.array([1,2,3,4])
print(arr.dtype)
arr = np.array(['apple','banana','cherry'])
print(arr.dtype)

print("Creating Arrays With a Defined Data Type\nWe use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:")
arr = np.array([1,2,3,4],dtype="S")
print(arr)
print(arr.dtype)

print('For i, u, f, S and U we can define size as well.')
arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)

print('If a type is given in which elements cant be casted then NumPy will raise a ValueError.')
#arr = np.array(["a","2","3"],dtype='i')
print(arr)
print(arr.dtype)

print("Converting Data Type on Existing Arrays")
print("The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.\nThe astype() function creates a copy of the array, and allows you to specify the data type as a parameter.\nThe data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.")
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

print("Change data type from float to integer by using int as parameter value:")
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

print('Change data type from integer to boolean:')
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print("The Difference Between Copy and View\nthat the copy is a new array, and the view is just a view of the original array.\nThe copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.\nThe view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.")

print('\nMake a copy, change the original array, and display both arrays:')
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print("Make a view, change the original array, and display both arrays:")
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
print('The view SHOULD be affected by the changes made to the original array.')
print('Make a view, change the view, and display both arrays:')
x[0] = 32
print(arr)
print(x)
print('The original array SHOULD be affected by the changes made to the view.')

print("\nCheck if Array Owns it's Data\ncopies owns the data, and views does not own the data, but how can we check this?\nEvery NumPy array has the attribute base that returns None if the array owns the data.")
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
print("The copy returns None.\nThe view returns the original array.")

print("NumPy Array Shape\nThe shape of an array is the number of elements in each dimension.\nNumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.")
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.shape)

print("NumPy Array Reshaping\nReshaping means changing the shape of an array.\nThe shape of an array is the number of elements in each dimension.\nBy reshaping we can add or remove dimensions or change number of elements in each dimension.")
print("Reshape From 1-D to 2-D")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)
print(newarr.shape)

print("Reshape From 1-D to 3-D")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)

print('Can We Reshape Into any Shape?\nYes, as long as the elements required for reshaping are equal in both shapes.\nWe can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.')
arr = np.array([1,2,3,4,5,6,7,8])
#newarr = arr.reshape(3,3)
#print(newarr)

print("Returns Copy or View?")
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
print('The example above returns the original array, so it is a view.')

print('Unknown Dimension\nYou are allowed to have one "unknown" dimension.\nMeaning that you do not have to specify an exact number for one of the dimensions in the reshape method.\nPass -1 as the value, and NumPy will calculate this number for you.')
newarr = arr.reshape(2,2,-1)
print(newarr)
print("We can not pass -1 to more than one dimension.")

print("Flattening the arrays\nFlattening array means converting a multidimensional array into a 1D array.\nWe can use reshape(-1) to do this.")
arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)

print("Iterating Arrays")
print("Iterate on the elements of the following 1-D array:")
arr = np.array([1,2,3])
for x in arr:
	print(x)

print("Iterating 2-D Arrays\nIn a 2-D array it will go through all the rows.")
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
	print(x)

print("To return the actual values, the scalars, we have to iterate the arrays in each dimension.")
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
	for y in x:
		print(y)

print("Iterating 3-D Arrays\nIn a 3-D array it will go through all the 2-D arrays.")
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
	print(x)

print("To return the actual values, the scalars, we have to iterate the arrays in each dimension.")
for x in arr:
	for y in x:
		for z in y:
			print(z)

print("Iterating Arrays Using nditer()\nThe function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.\nIterating on Each Scalar Element\nIn basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.")
for x in np.nditer(arr):
	print(x)

print('Iterating Array With Different Data Types\nWe can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.\nNumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=["buffered"].')
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(x)

print("Iterating With Different Step Size\nWe can use filtering and followed by iteration.")
print('Iterate through every scalar element of the 2D array skipping 1 element:')
for x in np.nditer(arr[:,::2]):
	print(x)
print("Array")
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:, ::2]):
	print(x)

print("Enumerated Iteration Using ndenumerate()\nEnumeration means mentioning sequence number of somethings one by one.\nSometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.")
for idx, x in np.ndenumerate(arr):
	print(idx,x)
print('3-D Array')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for idx, x in np.ndenumerate(arr):
	print(idx, x)

print("NumPy Joining Array")
print('Joining means putting contents of two or more arrays in a single array.\nIn SQL we join tables based on a key, whereas in NumPy we join arrays by axes.\nWe pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

print("Join two 2-D arrays along rows (axis=1):")
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis = 1)
print(arr)
arr = np.concatenate((arr1,arr2))
print(arr)

print("Joining Arrays Using Stack Functions\nStacking is same as concatenation, the only difference is that stacking is done along a new axis.\nWe can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.\nWe pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.")
arr = np.stack((arr1,arr2),axis = 1)
print(arr)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2),axis = 1)
print(arr)

print("Stacking Along Rows\nNumPy provides a helper function: hstack() to stack along rows.")
arr = np.hstack((arr1,arr2))
print(arr)

print("Stacking Along Columns\nNumPy provides a helper function: vstack()  to stack along columns.")
arr = np.vstack((arr1,arr2))
print(arr)

print("Stacking Along Height (depth)\nNumPy provides a helper function: dstack() to stack along height, which is the same as depth.")
arr = np.dstack((arr1,arr2))
print(arr)

print("Splitting NumPy Arrays\nSplitting is reverse operation of Joining.\nJoining merges multiple arrays into one and Splitting breaks one array into multiple.\nWe use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.")
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)

print('If the array has less elements than required, it will adjust from the end accordingly.')
newarr = np.array_split(arr,4)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print("Splitting 2-D Arrays\nUse the same syntax when splitting 2-D arrays.\nUse the array_split() method, pass in the array you want to split and the number of splits you want to do.")
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
newarr = np.array_split(arr,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print("Let's look at another example, this time each element in the 2-D arrays contains 3 elements.")
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.array_split(arr,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print("In addition, you can specify which axis you want to do the split around.\nThe example below also returns three 2-D arrays, but they are split along the row (axis=1).")
newarr = np.array_split(arr,3,axis=1)
print(newarr)

print("An alternate solution is using hsplit() opposite of hstack()")
newarr = np.hsplit(arr,3)
print(newarr)
print("Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().")


print("Searching Arrays\nYou can search an array for a certain value, and return the indexes that get a match.\nTo search an array, use the where() method.")
arr = np.array([1,2,2,3,3,3,4,4,5,5,5,6,6])
x = np.where(arr == 5)
print(x)

print("Find the indexes where the values are even:")
x = np.where(arr%2 == 0)
print(x)

print("Find the indexes where the values are odd:")
x = np.where(arr%2 == 1)
print(x)

print("Search Sorted\nThere is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.\nThe searchsorted() method is assumed to be used on sorted arrays.")
arr = np.array([6,7,2,8,9])
x = np.searchsorted(arr,7)
print(x)

print("Search From the Right Side\nBy default the left most index is returned, but we can give side='right' to return the right most index instead.")
x = np.searchsorted(arr,7,side='right')
print(x)

print("Multiple Values\nTo search for more than one value, use an array with the specified values.")
print("Find the indexes where the values 2, 4, and 6 should be inserted:")
x = np.searchsorted(arr,[2,4,6,1,10])
print(x)

print("NumPy Sorting Arrays\nSorting means putting elements in an ordered sequence.\nOrdered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.\nThe NumPy ndarray object has a function called sort(), that will sort a specified array.")
arr = np.array([3,2,5,6,4,8,9,0,1])
print(np.sort(arr))

print("You can also sort arrays of strings, or any other data type:")
arr = np.array(["banana","cherry","apple"])
print(np.sort(arr))

print("Sort a boolean array:")
arr = np.array([True,False,True])
print(np.sort(arr))

print("Sorting a 2-D Array\nIf you use the sort() method on a 2-D array, both arrays will be sorted:")
arr = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))

print("Filtering Arrays\nGetting some elements out of an existing array and creating a new array out of them is called filtering.\nIn NumPy, you filter an array using a boolean index list.")
print('If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.')
print("Create an array from the elements on index 0 and 2:")
arr = np.array([41,42,43,44])
x = [True,False,True,False]
newarr = arr[x]
print(newarr)

print("Creating the Filter Array\nIn the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.")
print('Create a filter array that will return only values higher than 42:')
arr = np.array([41,42,43,44])
filter_arr = []
for element in arr:
	if element > 42:
		filter_arr.append(True)
	else:
		filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print("Create a filter array that will return only even elements from the original array:")
arr = np.array([1,2,3,4,5,6,7,8,9])
filter_arr = []
for element in arr:
	if element % 2 == 0:
		filter_arr.append(True)
	else:
		filter_arr.append(False)
newarr = arr[filter_arr]

print(newarr)
print(filter_arr)

print("Creating Filter Directly From Array\nThe above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.\nWe can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.")
arr = np.array([41,42,43,44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print('Create a filter array that will return only even elements from the original array:')
arr = np.array([1,2,3,4,5,6,7,8,9])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

print("Random Numbers in NumPy")
print('What is a Random Number?\nRandom number does NOT mean a different number every time. Random means something that can not be predicted logically.')
print('Pseudo Random and True Random.\nComputers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.\nIf there is a program to generate random number it can be predicted, thus it is not truly random.\nRandom numbers generated through a generation algorithm are called pseudo random.\nCan we make truly random numbers?\nYes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.')
print("\nGenerate Random Number\nNumPy offers the random module to work with random numbers.")

from numpy import random

x = random.randint(100)
print(x)

print('Generate Random Float\nThe random module"s rand() method returns a random float between 0 and 1.')
x = random.rand()
print(x)

print("enerate Random Array\nIn NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.\nIntegers\nThe randint() method takes a size parameter where you can specify the shape of an array.")
print('\nGenerate a 1-D array containing 5 random integers from 0 to 100:')
x = random.randint(100,size = (5))
print(x)
print("\nGenerate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:")
x = random.randint(200,size=(3,5))
print(x)
print('\nFloats\nThe rand() method also allows you to specify the shape of the array.')
print('Generate a 1-D array containing 5 random floats:')
x = random.rand(5)
print(x)
print("Generate a 2-D array with 3 rows, each row containing 5 random numbers:")
x = random.rand(3,5)
print(x)

print('\nGenerate Random Number From Array\nThe choice() method allows you to generate a random value based on an array of values.\nThe choice() method takes an array as a parameter and randomly returns one of the values.')
print('Return one of the values in an array:')
x = random.choice([3,5,6,8,9,4,2,1])
print(x)

print('The choice() method also allows you to return an array of values.\nAdd a size parameter to specify the shape of the array.')
x = random.choice([3,5,7,9],size = (3,5))
print(x)

print("\n\nRandom Data Distribution")
print('What is Data Distribution?\nData Distribution is a list of all possible values, and how often each value occurs.\nSuch lists are important when working with statistics and data science.\nThe random module offer methods that returns randomly generated data distributions.')
print("Random Distribution\nA random distribution is a set of random numbers that follow a certain probability density function.\nProbability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.\nWe can generate random numbers based on defined probabilities using the choice() method of the random module.\nThe choice() method allows us to specify the probability for each value.\nThe probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.")
print("\n\nGenerate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.\nThe probability for the value to be 3 is set to be 0.1\nThe probability for the value to be 5 is set to be 0.3\nThe probability for the value to be 7 is set to be 0.6\nThe probability for the value to be 9 is set to be 0")
x =  random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(x)
print('The sum of all probability numbers should be 1.')
print('return a 2-D array with 3 rows, each containing 5 values.')
x =  random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(x)

print('Random Permutations')
print('Random Permutations of Elements\nA permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.\nThe NumPy Random module provides two methods for this: shuffle() and permutation().')
print('\nShuffling Arrays\nShuffle means changing arrangement of elements in-place. i.e. in the array itself.')
arr = np.array([1,2,3,4,5,6,7,8,9])
random.shuffle(arr)
print(arr)
print('The shuffle() method makes changes to the original array.')

print("\nGenerating Permutation of Arrays")
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))
print(arr)
print('The permutation() method returns a re-arranged array (and leaves the original array un-changed).')

print('\n\nSeaborn\nVisualize Distributions With Seaborn\nSeaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.')
print("NOT LEARNED, LEARN NEXT TIME")

print("\n\nNormal (Gaussian) Distribution\nNormal Distribution\nThe Normal Distribution is one of the most important distributions.\nIt is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.\nIt fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.\nUse the random.normal() method to get a Normal Data Distribution.\nIt has three parameters:\nloc - (Mean) where the peak of the bell exists.\nscale - (Standard Deviation) how flat the graph distribution should be.\nsize - The shape of the returned array.")
x = random.normal(size=(1))
print(x)

print("NUMPY RANDOM Distribution IS NOT LEARNED\nLEARN AFTER WARDS")


print("NumPy ufuncs\nWhat are ufuncs?\nufuncs stands for 'Universal Functions' and they are NumPy functions that operates on the ndarray object.\nWhy use ufuncs?\nufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.\nThey also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.\nufuncs also take additional arguments, like:\nwhere boolean array or condition defining where the operations should take place.\ndtype defining the return type of elements.\nout output array where the return value should be copied.")
print("What is Vectorization?\nConverting iterative statements into a vector based operation is called vectorization.\nIt is faster as modern CPUs are optimized for such operations.\nAdd the Elements of Two Lists\nlist 1: [1, 2, 3, 4]\nlist 2: [4, 5, 6, 7]\nOne way of doing it is to iterate over both of the lists and then sum each elements.")
print('Without ufunc, we can use Python`s built-in zip() method:')
x = [1,2,3,4]
y = [4,5,6,7]
z = []
for i, j in zip(x, y):
	z.append(i + j)
print(z)
print('NumPy has a ufunc for this, called add(x, y) that will produce the same result.')
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)

print('Create Your Own ufunc\nHow To Create Your Own ufunc\nTo create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.\nThe frompyfunc() method takes the following arguments:\nfunction - the name of the function.\ninputs - the number of input arguments (arrays).\noutputs - the number of output arrays.')
def myadd(x,y):
	return x+y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))

print("Check if a Function is a ufunc\nCheck the type of a function to check if it is a ufunc or not.\nA ufunc should return <class 'numpy.ufunc'>.")
print(type(np.add))
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

print("Simple Arithmetic\nYou could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.\nArithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.\nAll of the discussed arithmetic functions take a where parameter in which we can specify that condition.")
print("Addition\nThe add() function sums the content of two arrays, and return the results in a new array.")
arr1 = np.array([1,2,3,4,5,6,7,8])
arr2 = np.array([20,21,22,23,24,25,26,27])
print("arr1 = ",arr1)
print("arr2 = ",arr2)
newarr = np.add(arr1,arr2)
print("Addition\n",newarr)
newarr = np.subtract(arr2,arr1)
print("Subtract\n",newarr)
newarr = np.multiply(arr2,arr1)
print("Multiply\n",newarr)
newarr = np.divide(arr2,arr1)
print("Divide\n",newarr)
newarr = np.power(arr2,arr1)
print("Power\n",newarr)
newarr = np.mod(arr2,arr1)
print("Modulus\n",newarr)
newarr = np.remainder(arr2,arr1)
print("Reaminder\n",newarr)

print('Quotient and Mod\nThe divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.')
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1,arr2)
print(newarr)

print('Absolute Values\nBoth the absolute() and the abs() functions functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python`s inbuilt math.abs()')
arr = np.array([-1,-2,1,2,3,-4])
newarr = np.absolute(arr)
print(newarr)

print('Rounding Decimals\nThere are primarily five ways of rounding off decimals in NumPy:\ntruncation\nfix\nrounding\nfloor\nceil')
print("Truncation\nRemove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.")
arr = np.trunc([-3.66666, 3.666667])
print("Truncation = ",arr)
arr = np.fix([-3.66666, 3.666667])
print("Fix = ",arr)

print('Rounding\nThe around() function increments preceding digit or decimal by 1 if >=5 else do nothing.\nE.g. round off to 1 decimal point, 3.16666 is 3.2')
arr = np.around(3.16666,3)
print(arr)

print('Floor\nThe floor() function rounds off decimal to nearest lower integer.\nE.g. floor of 3.166 is 3.')
arr = np.floor([-3.1666,3.666667])
print(arr)

print('Ceil\nThe ceil() function rounds off decimal to nearest upper integer.\nE.g. ceil of 3.166 is 4.')
arr = np.ceil([-3.16666,3.66666667])
print(arr)

print("NumPy Logs\nNumPy provides functions to perform log at the base 2, e and 10.\nWe will also explore how we can take log for any base by creating a custom ufunc.\nAll of the log functions will place -inf or inf in the elements if the log can not be computed.")
print("Log at Base 2\nUse the log2() function to perform log at the base 2.")
arr = np.arange(1,10)
print(np.log2(arr))

print("Log at Base 10\nUse the log10() function to perform log at the base 10.")
arr = np.arange(1,21)
print(np.log10(arr))

print("Natural Log, or Log at Base e\nUse the log() function to perform log at the base e.")
arr = np.arange(1,10)
print(np.log(arr))

from math import log

print('Log at Any Base\nNumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:')
nplog = np.frompyfunc(log,2,1)
print(nplog(100,15))

print("NumPy Summations\nWhat is the difference between summation and addition?\nAddition is done between two arguments whereas summation happens over n elements.")
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
newarr = np.add(arr1,arr2)
print(newarr)
newarr =np.sum([arr1,arr2])
print(newarr)
print('Summation Over an Axis\nIf you specify axis=1, NumPy will sum the numbers in each array.')
newarr = np.sum([arr1,arr2],axis=1)
print(newarr)
print("Cummulative Sum\nCummulative sum means partially adding the elements in array.\nE.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].\nPerfom partial sum with the cumsum() function.")
arr = np.array([1,2,3,4,5,6,7,8,9,10])
newarr = np.cumsum(arr)
print(newarr)

print("NumPy Products\nTo find the product of the elements in an array, use the prod() function.")
arr1 = np.array([1,2,3,4])
x = np.prod(arr1)
print(x)
arr2 = np.array([5,6,7,8])
x = np.prod([arr1,arr2])
print(x)

print("Product Over an Axis\nIf you specify axis=1, NumPy will return the product of each array.")
newarr = np.prod([arr1,arr2], axis = 1)
print(newarr)

print("Cummulative Product\nCummulative product means taking the product partially.\nE.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]\nPerfom partial sum with the cumprod() function.")
arr = np.array([5,6,7,8])
newarr= np.cumprod(arr)
print(newarr)

print("NumPy Differences\nDifferences\nA discrete difference means subtracting two successive elements.\nE.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]\nTo find the discrete difference, use the diff() function.")
arr = np.array([10,15,25,5])
newarr = np.diff(arr)
print(newarr)
print("Returns: [5 10 -20] because 15-10=5, 25-15=10, and 5-25=-20")
print('We can perform this operation repeatedly by giving parameter n.\nE.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]')
arr = np.array([10,15,25,5])
newarr = np.diff(arr,n =2)
print(newarr)
print("Returns: [5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30")

print("NumPy LCM Lowest Common Multiple\nThe Lowest Common Multiple is the least number that is common multiple of both of the numbers.")
num1 = 4
num2 = 6
x = np.lcm(num1,num2)
print(x)

print('Finding LCM in Arrays\nTo find the Lowest Common Multiple of all values in an array, you can use the reduce() method.')
print("The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.")

arr = np.array([3,6,9])
x = np.lcm.reduce(arr)
print(x)

print("Find the LCM of all of an array where the array contains all integers from 1 to 10:")
arr = np.arange(1,11)
x = np.lcm.reduce(arr)
print(x)

print('NumPy GCD Greatest Common Denominator\nThe GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.')
num1 = 6
num2 = 9
x = np.gcd(num1,num2)
print(x)

print("Finding GCD in Arrays\nTo find the Highest Common Factor of all values in an array, you can use the reduce() method.\nThe reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.")
arr = np.array([20,8,32,36,16])
x = np.gcd.reduce(arr)
print(x)

print("NumPy Trigonometric Functions\nNumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.")
x = np.sin(np.pi/2)
print(x)
print(np.pi)
print(np.sin(np.pi))

print("\nFind sine values for all of the values in arr:")
arr = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x = np.sin(arr)
print(x)

print("Convert Degrees Into Radians\nBy default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumP.\nNote: radians values are pi/180 * degree_values.")
arr = np.array([90,180,270,360])
x = np.deg2rad(arr)
print(x)

print('Radians to Degrees')
arr = np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
x = np.rad2deg(arr)
print(x)

print('Finding Angles\nFinding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).\nNumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.')
x = np.arcsin(1.0)
print(x)

print('Angles of Each Value in Arrays')
arr = np.array([1,-1,0,0.1])
x = np.arcsin(arr)
print(x)

print("Hypotenues\nFinding hypotenues using pythagoras theorem in NumPy.\nNumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.")
base = 3
prep = 4
x = np.hypot(base,prep)
print(x)

print("NumPy Hyperbolic Functions\nNumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values.")
x = np.sinh(np.pi/2)
print(x)

print("Find cosh values for all of the values in arr:")
arr = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x = np.cosh(arr)
print(x)

print('Finding Angles\nFinding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).\nNumpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.')
x = np.arcsinh(1.0)
print(x)

print('Angles of Each Value in Arrays')
arr = np.array([0.1,0.2,0.5])
x = np.arctanh(arr)
print(x)

print("NumPy Set Operations\nWhat is a Set\nA set in mathematics is a collection of unique elements.\nSets are used for operations involving frequent intersection, union and difference operations.\nCreate Sets in NumPy\nWe can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.")
print("Convert following array with repeated elements to a set:")
arr = np.array([1,1,1,2,3,4,5,5,6,6,7,7])
x = np.unique(arr)
print(x)

print("Finding Union\nTo find the unique values of two arrays, use the union1d() method.")
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.union1d(arr1,arr2)
print(newarr)

print("Finding Intersection\nTo find only the values that are present in both arrays, use the intersect1d() method.")
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.intersect1d(arr1,arr2,assume_unique=True)
print(newarr)

print("Finding Difference\nTo find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.")
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setdiff1d(set1,set2,assume_unique=True)
print(newarr)

print("Finding Symmetric Difference\nTo find only the values that are NOT present in BOTH sets, use the setxor1d() method.")
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setxor1d(set1,set2,assume_unique=True)
print(newarr)