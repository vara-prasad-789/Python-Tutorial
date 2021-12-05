print("Pandas Tutorial\nPandas is a Python library.\nPandas is used to analyze data")
print('What is Pandas?\nPandas is a Python library used for working with data sets.\nIt has functions for analyzing, cleaning, exploring, and manipulating data.\nThe name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.\nWhy Use Pandas?\nPandas allows us to analyze big data and make conclusions based on statistical theories.\nPandas can clean messy data sets, and make them readable and relevant.\nRelevant data is very important in data science.')
print("What Can Pandas Do?\nPandas gives you answers about the data. Like:\nIs there a correlation between two or more columns?\nWhat is average value?\nMax value?\nMin value?\nPandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.")
print("Installation of Pandas\npip install pandas")
print('Import Pandas\nOnce Pandas is installed, import it in your applications by adding the import keyword')
import pandas as pd
mydataset = {
	'cars': ["BMW","Volvo","Ford"],
	'passings': [3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print('Checking Pandas Version\nThe version string is stored under __version__ attribute.')
print(pd.__version__)

print("Pandas Series\nA Pandas Series is like a column in a table.\nIt is a one-dimensional array holding data of any type.")
print('Create a simple Pandas Series from a list:')
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

print('Labels\nIf nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.\nThis label can be used to access a specified value.')
print(myvar[0])
print("\nCreate Labels\nWith the index argument, you can name your own labels.")
print("When you have created labels, you can access an item by referring to the label.")
a = [1,7,2]
myvar = pd.Series(a,index = ["x","y","z"])
print(myvar,"\n",myvar["x"],myvar["y"],myvar["z"])

print("Key/Value Objects as Series\nYou can also use a key/value object, like a dictionary, when creating a Series.")
print('Create a simple Pandas Series from a dictionary:')
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories)
print(myvar)
print('The keys of the dictionary become the labels.')

print("\nTo select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.")
print('Create a Series using only data from "day1" and "day2":')
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories,index = ["day1","day2"])
print(myvar)

print("DataFrames\nData sets in Pandas are usually multi-dimensional tables, called DataFrames.\nSeries is like a column, a DataFrame is the whole table.")
print('Create a DataFrame from two Series:')
data = {
	"calories": [420,380,390],
	"duration": [50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)

print('Pandas DataFrames\nA Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.')
print("Create a simple Pandas DataFrame:")
data = {
	"calories": [420,380,390],
	"duration": [50,40,45]
}
df = pd.DataFrame(data)
print(df)

print('Locate Row\nAs you can see from the result above, the DataFrame is like a table with rows and columns.\nPandas use the loc attribute to return one or more specified row(s)')
print(df.loc[0])
print("This example returns a Pandas Series.\nThis example returns a Pandas Series.")
print(df.loc[[0,1]])
print('When using [], the result is a Pandas DataFrame.')

print("Named Indexes\nWith the index argument, you can name your own indexes")
data = {
	"calories": [420,380,390],
	"duration": [50,40,45]
}
df = pd.DataFrame(data,index = ["day1","day2","day3"])
print(df)

print("Locate Named Indexes\nUse the named index in the loc attribute to return the specified row(s).")
print(df.loc["day2"])

print('Load Files Into a DataFrame\nIf your data sets are stored in a file, Pandas can load them into a DataFrame.')
df = pd.read_csv('E:\learning\webpages\HTML\Python\data.csv')
print(df)

print("Pandas Read CSV\nA simple way to store big data sets is to use CSV files (comma separated files).\nCSV files contains plain text and is a well know format that can be read by everyone including Pandas.\nIn our examples we will be using a CSV file called 'data.csv'.")
print(df.to_string())
print('use to_string() to print the entire DataFrame.')
print('By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:')

print("Pandas Read JSON\nBig data sets are often stored, or extracted as JSON.\nJSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.\nIn our examples we will be using a JSON file called 'data.json'.")
df = pd.read_json('E:\learning\webpages\HTML\Python\data.json')
print(df.to_string())
print(df)

print('Dictionary as JSON\nJSON = Python Dictionary\nJSON objects have the same format as Python dictionaries.')
print('If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:')
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)

print("Pandas - Analyzing DataFrames\nViewing the Data\nOne of the most used method for getting a quick overview of the DataFrame, is the head() method.\nThe head() method returns the headers and a specified number of rows, starting from the top.")
df = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
print(df.head(10))
print('if the number of rows is not specified, the head() method will return the top 5 rows.')
print(df.head())
print('There is also a tail() method for viewing the last rows of the DataFrame.\nThe tail() method returns the headers and a specified number of rows, starting from the bottom.')
print(df.tail())
print("Info About the Data\nThe DataFrames object has a method called info(), that gives you more information about the data set.")
print(df.info())


print("Pandas - Cleaning Data\nData Cleaning\nData cleaning means fixing bad data in your data set.\nBad data could be:\nEmpty cells\nData in wrong format\nWrong data\nDuplicates\nIn this tutorial you will learn how to deal with all of them.")
print('Pandas - Cleaning Empty Cells\nEmpty Cells\nEmpty cells can potentially give you a wrong result when you analyze data.')
print('Remove Rows\nOne way to deal with empty cells is to remove rows that contain empty cells.\nThis is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.')
print('Return a new Data Frame with no empty cells:')
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
print(df.to_string())
new_df = df.dropna()
print(new_df.to_string())
print('By default, the dropna() method returns a new DataFrame, and will not change the original.')
print('If you want to change the original DataFrame, use the inplace = True argument:')
#df.dropna(inplace = True)
#print(df.to_string())

print('Replace Empty Values\nAnother way of dealing with empty cells is to insert a new value instead.\nThis way you do not have to delete entire rows just because of some empty cells.\nThe fillna() method allows us to replace empty cells with a value:')
print('Replace NULL values with the number 130:')
df = pd.read_csv("E:\learning\webpages\HTML\Python\dirtydata.csv")
df.fillna(130,inplace = True)
print(df.to_string())

print("Replace Only For a Specified Columns\nThe example above replaces all empty cells in the whole Data Frame.\nTo only replace empty values for one column, specify the column name for the DataFrame:")
print('Replace NULL values in the "Calories" columns with the number 130:')
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
df["Calories"].fillna(130,inplace = True)
print(df.to_string())

print('Replace Using Mean, Median, or Mode\nA common way to replace empty cells, is to calculate the mean, median or mode value of the column.\nPandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:')
df = pd.read_csv("E:\learning\webpages\HTML\Python\dirtydata.csv")
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())

print("\nMean = the average value (the sum of all values divided by number of values).\n")
print('Calculate the MEDIAN, and replace any empty values with it:')
df = pd.read_csv("E:\learning\webpages\HTML\Python\dirtydata.csv")
x = df["Calories"].median()
df['Calories'].fillna(x, inplace = True)
print(df.to_string())

print('\nMedian = the value in the middle, after you have sorted all values ascending.\n')

print("Calculate the MODE, and replace any empty values with it:")
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x,inplace = True)
print(df.to_string())
print(x)

print("Pandas - Cleaning Data of Wrong Format\nCells with data of wrong format can make it difficult, or even impossible, to analyze data.\nTo fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.")
print('Convert Into a Correct Format\nIn our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the "Date" column should be a string that represents a date:')
print("\nLet's try to convert all cells in the Date column into dates.\nPandas has a to_datetime() method for this:\n")
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
df["Date"] = pd.to_datetime(df["Date"])
print(df.to_string())

print('As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.')
print("Removing Rows\nThe result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.")
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
df.dropna(subset=["Date"],inplace=True)
print(df.to_string())

print('Pandas - Fixing Wrong Data\n"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".\nSometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.\nIf you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.\nIt doesn`t have to be wrong, but taking in consideration that this is the data set of someone`s workout sessions, we conclude with the fact that this person did not work out in 450 minutes.')
print("Replacing Values\nOne way to fix wrong values is to replace them with something else.\nIn our example, it is most likely a typo, and the value should be '45' instead of '450', and we could just insert '45' in row 7:")
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
df.loc[7,"Duration"] = 45
print(df.to_string())

print('For small data sets you might be able to replace the wrong data one by one, but not for big data sets.\nTo replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.')
print('Loop through all values in the "Duration" column.\nIf the value is higher than 120, set it to 120:')
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
for x in df.index:
	if df.loc[x,"Duration"] > 120:
		df.loc[x,"Duration"] = 120

print(df.to_string())

print('Removing Rows\nAnother way of handling wrong data is to remove the rows that contains wrong data.\nThis way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.')
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
for x in df.index:
	if df.loc[x,"Duration"] > 120:
		df.drop(x,inplace = True)
print(df.to_string())

print("Pandas - Removing Duplicates\nDiscovering Duplicates\nDuplicate rows are rows that have been registered more than one time.")
print("we can use the duplicated() method.\nThe duplicated() method returns a Boolean values for each row:")
print("Returns True for every row that is a duplicate, othwerwise False:")
df = pd.read_csv('E:\learning\webpages\HTML\Python\dirtydata.csv')
print(df.duplicated())

print('Removing Duplicates\nTo remove duplicates, use the drop_duplicates() method.')
df.drop_duplicates(inplace = True)
print(df.to_string())

print("Pandas - Data Correlations\nFinding Relationships\nA great aspect of the Pandas module is the corr() method.\nThe corr() method calculates the relationship between each column in your data set.")
df = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
print(df.to_string())
print(df.corr())
print('The corr() method ignores "not numeric" columns.')

print("Result Explained\nThe Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.\nThe number varies from -1 to 1.\n1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.\n0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.\n-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.\n0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.")
print("\nWhat is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.\n")
print("Perfect Correlation:\nWe can see that 'Duration' and 'Duration' got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.\n\nGood Correlation:\n'Duration' and 'Calories' got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.\n\nBad Correlation:\n'Duration' and 'Maxpulse' got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.")

print("Pandas - Plotting\nPlotting\nPandas uses the plot() method to create diagrams.\nWe can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.")
import matplotlib.pyplot as plt
df = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
df.plot()
plt.show()

print("Scatter Plot\nSpecify that you want a scatter plot with the kind argument:\nkind = 'scatter'\nA scatter plot needs an x- and a y-axis.\nIn the example below we will use 'Duration' for the x-axis and 'Calories' for the y-axis.\nInclude the x and y arguments like this:\nx = 'Duration', y = 'Calories'")
df1 = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
df1.plot(kind = "scatter", x = "Duration", y = "Calories")
plt.show()

print("Remember: In the previous example, we learned that the correlation between 'Duration' and 'Calories' was 0.922721, and we conluded with the fact that higher duration means more calories burned.\nBy looking at the scatterplot, I will agree.")
print("\nLet's create another scatterplot, where there is a bad relationship between the columns, like 'Duration' and 'Maxpulse', with the correlation 0.009403:")
df2 = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
df2.plot(kind = "scatter", x = "Duration", y = "Maxpulse" )
plt.show()

print("Histogram\nUse the kind argument to specify that you want a histogram:\nkind = 'hist'\nA histogram needs only one column.\nA histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?\nIn the example below we will use the 'Duration' column to create the histogram:")
df3 = pd.read_csv("E:\learning\webpages\HTML\Python\data.csv")
df3["Duration"].plot(kind = 'hist')
plt.show()
print('Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.')