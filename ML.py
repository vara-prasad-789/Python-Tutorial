print("Machine Learning\nMachine Learning is making the computer learn from studying data and statistics.\nMachine Learning is a step into the direction of artificial intelligence (AI).\nMachine Learning is a program that analyses data and learns to predict the outcome.")
print("\n\nData Types\nTo analyze data, it is important to know what type of data we are dealing with.\nWe can split the data types into three main categories:\nNumerical\nCategorical\nOrdinal\nNumerical data are numbers, and can be split into two numerical categories:\nDiscrete Data\n- numbers that are limited to integers. Example: The number of cars passing by.\nContinuous Data\n- numbers that are of infinite value. Example: The price of an item, or the size of an item\nCategorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.\nOrdinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.\nBy knowing the data type of your data source, you will be able to know what technique to use when analyzing them.")
print("\n\nMachine Learning - Mean Median Mode\nIn Machine Learning (and in mathematics) there are often three values that interests us:\nMean - The average value\nMedian - The mid point value\nMode - The most common value")
print("\n\nMean\nThe mean value is the average value.\nTo calculate the mean, find the sum of all values, and divide the sum by the number of values:\nThe NumPy module has a method for this. Using numpy")
import numpy as np
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(speed)
print("\nMean : ",x)
print("\nMedian\nThe median value is the value in the middle, after you have sorted all the values:\nIt is important that the numbers are sorted before you can find the median.")
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.median(speed)
print("\nMedian : ",x)

print("If there are two numbers in the middle, divide the sum of those numbers by two.")
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = np.median(speed)
print(x)

print("Mode\nThe Mode value is the value that appears the most number of times:\nThe SciPy module has a method for this.")
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

print("\nMachine Learning - Standard Deviation\nStandard deviation is a number that describes how spread out the values are.\nA low standard deviation means that most of the numbers are close to the mean (average) value.\nA high standard deviation means that the values are spread out over a wider range.")
print("\nExample: This time we have registered the speed of 7 cars:\nspeed = [86,87,88,86,87,85,86]\nThe standard deviation is:\n0.9\nMeaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.")
print("\nLet us do the same with a selection of numbers with a wider range:\nspeed = [32,111,138,28,59,77,97]\nThe standard deviation is:\n37.85\nMeaning that most of the values are within the range of 37.85 from the mean value, which is 77.4.")
print("standard deviation")
speed = [86,87,88,86,87,85,86]
x = np.std(speed)
print("Low standard Deviation : ",x)

speed = [32,111,138,28,59,77,97]
x = np.std(speed)
print("High Standard Deviation : ",x)

print("Variance\nVariance is another number that indicates how spread out the values are.\nIn fact, if you take the square root of the variance, you get the standard deviation!\nOr the other way around, if you multiply the standard deviation by itself, you get the variance!")
print("\nTo calculate the variance you have to do as follows:\n\n1. Find the mean:\n(32+111+138+28+59+77+97) / 7 = 77.4\n\n2. For each value: find the difference from the mean:\n 32 - 77.4 = -45.4\n111 - 77.4 =  33.6\n138 - 77.4 =  60.6\n 28 - 77.4 = -49.4\n 59 - 77.4 = -18.4\n 77 - 77.4 = - 0.4\n 97 - 77.4 =  19.6\n\n3. For each difference: find the square value:\n(-45.4)2 = 2061.16\n (33.6)2 = 1128.96\n (60.6)2 = 3672.36\n(-49.4)2 = 2440.36\n(-18.4)2 =  338.56\n(- 0.4)2 =    0.16\n (19.6)2 =  384.16\n\n4. The variance is the average number of these squared differences:\n(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2")
print("\nLuckily, NumPy has a method to calculate the variance:")
speed = [32,111,138,28,59,77,97]
x = np.var(speed)
print("Variance : ",x)

print("\nStandard Deviation\nthe formula to find the standard deviation is the square root of the variance:\n√1432.25 = 37.85")
speed = [32,111,138,28,59,77,97]
x = np.std(speed)
print("\nStandard Deviation : ",x)

print("\nStandard Deviation is often represented by the symbol Sigma: σ\nVariance is often represented by the symbol Sigma Square: σ2")

print("Machine Learning - Percentiles\nPercentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.")
print("\nExample: Let's say we have an array of the ages of all the people that lives in a street.\nages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]\nWhat is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.\nThe NumPy module has a method for finding the specified percentile:")
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = np.percentile(ages,75)
print("75% of the people are 43 or younger : ",x)

x = np.percentile(ages,90)
print("90% of people age : ",x)

print("Machine Learning - Data Distribution\nHow Can we Get Big Data Sets?\nTo create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.")
print('Create an array containing 250 random floats between 0 and 5:')
y = np.random.uniform(0,500,250)
print(y)

print('Histogram\nTo visualize the data set we can draw a histogram with the data we collected.\nWe will use the Python module Matplotlib to draw a histogram.')
import matplotlib.pyplot as plt
#plt.hist(y,5)
#plt.show()

print("Histogram Explained\nWe use the array from the example above to draw a histogram with 5 bars.\nThe first bar represents how many values in the array are between 0 and 1.\nThe second bar represents how many values are between 1 and 2.\nEtc.\nWhich gives us this result:\n52 values are between 0 and 1\n48 values are between 1 and 2\n49 values are between 2 and 3\n51 values are between 3 and 4\n50 values are between 4 and 5\nNote: The array values are random numbers and will not show the exact same result on your computer.")

print("\n\nBig Data Distributions\nAn array containing 250 values is not considered very big, but now you know how to create a random set of values, and by changing the parameters, you can create the data set as big as you want.")
print("Create an array with 100000 random numbers, and display them using a histogram with 100 bars:")
x = np.random.uniform(0,9999,100000)
#plt.hist(x,2000)
#plt.show()

print("Machine Learning - Normal Data Distribution")
print("how to create an array where the values are concentrated around a given value.\nIn probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution")
print("A typical normal data distribution:")
x = np.random.normal(5.0,2.0,1000)
print(x)
#plt.hist(x,100)
#plt.show()

print("Histogram Explained\nWe use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.\nWe specify that the mean value is 5.0, and the standard deviation is 1.0.\nMeaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.\nAnd as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.")

print("\n\nMachine Learning - Scatter Plot\nA scatter plot is a diagram where each value in the data set is represented by a dot.")
print("The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:\nx = [5,7,8,7,2,17,2,9,4,11,12,9,6]\ny = [99,86,87,88,111,86,103,87,94,78,77,85,86]\nThe x array represents the age of each car.\nThe y array represents the speed of each car.")
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#plt.scatter(x,y)
#plt.show()
print("Scatter Plot Explained\nThe x-axis represents ages, and the y-axis represents speeds.\nWhat we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.")

print("\n\nRandom Data Distributions\nIn Machine Learning the data sets can contain thousands-, or even millions, of values.\nYou might not have real world data when you are testing an algorithm, you might have to use randomly generated values.\nAs we have learned in the previous chapter, the NumPy module can help us with that!\nLet us create two arrays that are both filled with 1000 random numbers from a normal data distribution.\nThe first array will have the mean set to 5.0 with a standard deviation of 1.0.\nThe second array will have the mean set to 10.0 with a standard deviation of 2.0:")
x = np.random.normal(5.0,1.0,1000)
y = np.random.normal(10.0,2.0,1000)
#plt.scatter(x,y)
#plt.show()
print("dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.")

print("\n\nMachine Learning - Linear Regression")
print("\n\nRegression\nThe term regression is used when you try to find the relationship between variables.\nIn Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.")
print("Linear Regression\nLinear regression uses the relationship between the data-points to draw a straight line through all them.\nThis line can be used to predict future values.")
print("How Does it Work?\nPython has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the mathematic formula.\nIn the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:")
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

print("Import scipy and draw the line of Linear Regression:")
slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfunc(x):
	return slope * x + intercept
mymodel = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()