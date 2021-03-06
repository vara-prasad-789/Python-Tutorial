print("Matplotlib Tutorial\nWhat is Matplotlib?\nMatplotlib is a low level graph plotting library in python that serves as a visualization utility.\nMatplotlib was created by John D. Hunter.\nMatplotlib is open source and we can use it freely.\nMatplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.")
import matplotlib
print("Checking Matplotlib Version")
print(matplotlib.__version__)

print("Matplotlib Pyplot\nMost of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:")
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])
#plt.plot(xpoints,ypoints)
#plt.show()

print("Matplotlib Plotting\nPlotting x and y points\nThe plot() function is used to draw points (markers) in a diagram.\nBy default, the plot() function draws a line from point to point.\nThe function takes parameters for specifying points in the diagram.\nParameter 1 is an array containing the points on the x-axis.\nParameter 2 is an array containing the points on the y-axis.\nIf we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.")

xpoints = np.array([1,8])
ypoints = np.array([3,10])
#plt.plot(xpoints,ypoints)
#plt.show()

print("Plotting Without Line\nTo plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.")
xpoints = np.array([1,8])
ypoints = np.array([3,10])
#plt.plot(xpoints,ypoints,'o')
#plt.show()

print("Multiple Points\nYou can plot as many points as you like, just make sure you have the same number of points in both axis.")
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

#plt.plot(xpoints, ypoints)
#plt.show()

print('Default X-Points\nIf we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.\nSo, if we take the same example as above, and leave out the x-points, the diagram will look like this:')
ypoints = np.array([3,8,1,10,5,7])
#plt.plot(ypoints)
#plt.show()

print("\nMatplotlib Markers\nYou can use the keyword argument marker to emphasize each point with a specified marker:")
ypoints = np.array([3,8,1,10])
#plt.plot(ypoints,marker = 'o')
#plt.show()

print("Mark each point with a star:")
print("Point")
#plt.plot(ypoints,marker = ".")
#plt.show()
print("Plus")
#plt.plot(ypoints,marker = "+")
#plt.show()
print("pixel")
#plt.plot(ypoints,marker = ",")
#plt.show()
print("x mark")
#plt.plot(ypoints,marker = "x")
#plt.show()
print('X filled')
#plt.plot(ypoints,marker = "X")
#plt.show()
print("Plus filled")
#plt.plot(ypoints,marker = "P")
#plt.show()
print("Square")
#plt.plot(ypoints,marker = "s")
#plt.show()
print("Diamond")
#plt.plot(ypoints,marker = "D")
#plt.show()
print('Diamond (thin)')
#plt.plot(ypoints,marker = "d")
#plt.show()
print('Pentagon')
#plt.plot(ypoints,marker = "p")
#plt.show()
print('Hexagon')
#plt.plot(ypoints,marker = "H")
#plt.show()
print("hexagon")
#plt.plot(ypoints,marker = "h")
#plt.show()
print("Triangle Down")
#plt.plot(ypoints,marker = "v")
#plt.show()
print("Triangle up")
#plt.plot(ypoints,marker = "^")
#plt.show()
print("Triangle left")
#plt.plot(ypoints,marker = "<")
#plt.show()
print('Triangle Right')
#plt.plot(ypoints,marker = ">")
#plt.show()
print("Tri Down")
#plt.plot(ypoints,marker = "1")
#plt.show()
print('Tri Up')
#plt.plot(ypoints,marker = "2")
#plt.show()
print("tri Left")
#plt.plot(ypoints,marker = "3")
#plt.show()
print("Tri right")
#plt.plot(ypoints,marker = "4")
#plt.show()
print("Vline")
#plt.plot(ypoints,marker = "|")
#plt.show()
print("Hline")
#plt.plot(ypoints,marker = "_")
#plt.show()

print("\nFormat Strings fmt\nYou can use also use the shortcut string notation parameter to specify the marker.\nThis parameter is also called fmt, and is written with this syntax:\nmarker|line|color")
print("Dotted Line")
#plt.plot(ypoints,"o:r")
#plt.show()
print("Line Reference")
print("Solid Line")
#plt.plot(ypoints,"o-r")
#plt.show()
print("Dashed Line")
#plt.plot(ypoints,"o--r")
#plt.show()
print("Dashed/Dotted line")
#plt.plot(ypoints,"o-.r")
#plt.show()

print("Color Reference")
print("Red")
#plt.plot(ypoints,"o--r")
#plt.show()
print("Green")
#plt.plot(ypoints,"o--g")
#plt.show()
print("Blue")
#plt.plot(ypoints,"o--b")
#plt.show()
print("Cyan")
#plt.plot(ypoints,"o--c")
#plt.show()
print("Magneta")
#plt.plot(ypoints,"o--m")
#plt.show()
print("Yellow")
#plt.plot(ypoints,"o--y")
#plt.show()
print("Black")
#plt.plot(ypoints,"o--b")
#plt.show()
print("White")
#plt.plot(ypoints,"o--w")
#plt.show()

print('Marker Size\nYou can use the keyword argument markersize or the shorter version, ms to set the size of the markers:')
#plt.plot(ypoints,marker = "o", ms = 20)
#plt.show()

print("Marker Color\nYou can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:")
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
#plt.show()
print('You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:')
#plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
#plt.show()
print("Use both the mec and mfc arguments to color of the entire marker:")
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
#plt.show()
print('You can also use Hexadecimal color values:')
#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
#plt.show()
print("Or any of the 140 supported color names.")
#plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
#plt.show()

print("Matplotlib Line\nLinestyle\nYou can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:")
#plt.plot(ypoints, linestyle = "dotted")
#plt.show()
print("Use a dashed line:")
#plt.plot(ypoints, linestyle = "dashed")
#plt.show()
print("Shorter Syntax\nThe line style can be written in a shorter syntax:\nlinestyle can be written as ls.\ndotted can be written as :.\ndashed can be written as --.")
#plt.plot(ypoints, ls = ':')
#plt.show()
print("Line Color\nYou can use the keyword argument color or the shorter c to set the color of the line:")
#plt.plot(ypoints, color = 'r')
#plt.show()
print("You can also use Hexadecimal color values:")
#plt.plot(ypoints, c = '#4CAF50')
#plt.show()
print("Line Width\nYou can use the keyword argument linewidth or the shorter lw to change the width of the line.\nThe value is a floating number, in points:")
#plt.plot(ypoints, linewidth = "20.5")
#plt.show()
print("Multiple Lines\nYou can plot as many lines as you like by simply adding more plt.plot() functions:")
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
#plt.plot(y1)
#plt.plot(y2)
plt.show()

print('You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.')
print('The x- and y- values come in pairs:')
print('Draw two lines by specifiyng the x- and y-point values for both lines:')
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

#plt.plot(x1, y1, x2, y2)
#plt.show()

print("Matplotlib Labels and Title")
print("Create Labels for a Plot\nWith Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.")
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
#plt.plot(x,y)
#plt.xlabel("Average Pulse")
#plt.ylabel("Calorie Burnage")
#plt.show()

print('Create a Title for a Plot\nWith Pyplot, you can use the title() function to set a title for the plot.\nAdd a plot title and labels for the x- and y-axis:')
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
#plt.plot(x,y)
#plt.title("Sports Watch Data")
#plt.xlabel("Average Pulse")
#plt.ylabel("Calorie Burnage")
#plt.show()

print("Set Font Properties for Title and Labels\nYou can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.")
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
#font1 = {'family':'serif','color':'blue','size':15}
#font2 = {'family':'serif','color':'darkred','size':20}
#plt.title('Sports Watch Data', fontdict = font1)
#plt.xlabel("Average Pulse",fontdict = font2)
#plt.ylabel('Calorie Burnage',fontdict = font2)

#plt.plot(x,y)
#plt.show()

print("Position the Title\nYou can use the loc parameter in title() to position the title.\nLegal values are: 'left', 'right', and 'center'. Default value is 'center'")
#plt.title("Sports Watch Data", loc = 'left')
#plt.xlabel("Average Pulse")
#plt.ylabel("Calorie Burnage")
#plt.plot(x,y)
#plt.show()

print("Matplotlib Adding Grid Lines\nAdd Grid Lines to a Plot\nWith Pyplot, you can use the grid() function to add grid lines to the plot.")
#plt.title("Sports Watch Data")
#plt.xlabel("Average Pulse")
#plt.ylabel('Calorie Burnage')
#plt.plot(x,y)
#plt.grid()
#plt.show()

print("Specify Which Grid Lines to Display\nYou can use the axis parameter in the grid() function to specify which grid lines to display.\nLegal values are: 'x', 'y', and 'both'. Default value is 'both'.")
#plt.grid(axis = 'x')
#plt.grid(axis =  'y')
#plt.show()

print("Set Line Properties for the Grid\nYou can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).")
#plt.plot(x,y)
#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
#plt.show()

print("Matplotlib Subplots\nDisplay Multiple Plots\nWith the subplots() function you can draw multiple plots in one figure:")
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
#plt.subplot(1,2,1)
#plt.plot(x,y)
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
#plt.subplot(1,2,2)
#plt.plot(x,y)
#plt.show()

print('The subplots() Function\nThe subplots() function takes three arguments that describes the layout of the figure.\nThe layout is organized in rows and columns, which are represented by the first and second argument.\nThe third argument represents the index of the current plot.\n\nplt.subplot(1, 2, 1)\n#the figure has 1 row, 2 columns, and this plot is the first plot.\n\nplt.subplot(1, 2, 2)\n#the figure has 1 row, 2 columns, and this plot is the second plot.\n\nSo, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:')
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
#plt.subplot(2,1,1)
#plt.plot(x,y)
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
#plt.subplot(2,1,2)
#plt.plot(x,y)
#plt.show()

print('You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.')
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
#plt.subplot(2,3,1)
#plt.plot(x,y)
#plt.title("Sales")
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
#plt.subplot(2,3,2)
#plt.plot(x,y)
#plt.title("Income")
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
#plt.subplot(2,3,3)
#plt.plot(x,y)
#plt.title('Sales')
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
#plt.subplot(2,3,4)
#plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
#plt.subplot(2,3,5)
#plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
#plt.subplot(2,3,6)
#plt.plot(x,y)
#plt.show()

print('Matplotlib Scatter\nCreating Scatter Plots\nWith Pyplot, you can use the scatter() function to draw a scatter plot.\nThe scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:')
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#plt.scatter(x,y)
#plt.show()
print("The observation in the example above is the result of 13 cars passing by.\nThe X-axis shows how old the car is.\nThe Y-axis shows the speed of the car when it passes.\nAre there any relationships between the observations?\nIt seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.")
print("\n\nCompare Plots\nIn the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?")
#day one, the age and speed of 13 cars:Note: The two plots are plotted with two different colors, by default blue and orange
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#plt.scatter(x, y)
#day two, the age and speed of 15 cars:
x1 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y1 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
#plt.scatter(x, y)
#plt.show()

print('Note: The two plots are plotted with two different colors, by default blue and orange')
print("\nColors\nYou can set your own color for each scatter plot with the color or the c argument:")
#plt.scatter(x,y,color = 'hotpink')
#plt.scatter(x1,y1,color = '#88c999')
#plt.show()

print("Color Each Dot\nYou can even set a specific color for each dot by using an array of colors as value for the c argument:\nNote: You cannot use the color argument for this, only the c argument.")
print('Set your own color of the markers:')
#colors = np.array(["red","green","blue","Yellow","pink","Black","orange","purple","beige","brown","gray","cyan","magenta"])
#plt.scatter(x,y,c = colors)
#plt.show()

print("ColorMap\nThe Matplotlib module has a number of available colormaps.\nA colormap is like a list of colors, where each color has a value that ranges from 0 to 100.\nThis colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.\nHow to Use the ColorMap\nYou can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.\nIn addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:")
colors = np.array([0,9,18,27,36,45,54,63,72,81,90,95,100])
#plt.scatter(x,y,c=colors,cmap='viridis')
#plt.show()

print('You can include the colormap in the drawing by including the plt.colorbar() statement:')
#plt.scatter(x,y,c=colors,cmap='viridis')
#plt.colorbar()
#plt.show()

print("Size\nYou can change the size of the dots with the s argument.\nJust like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:")
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#plt.scatter(x,y, s=sizes)
#plt.show()

print("Alpha\nYou can adjust the transparency of the dots with the alpha argument.\nJust like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:")
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#plt.scatter(x,y, s=sizes, alpha=0.5)
#plt.show()

print("Combine Color Size and Alpha\nYou can combine a colormap with different sizes on the dots. This is best visualized if the dots are transparent:")
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = np.random.randint(400, size=(100))
#plt.scatter(x,y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
#plt.colorbar()
#plt.show()

print('Matplotlib Bars\nCreating Bars\nWith Pyplot, you can use the bar() function to draw bar graphs:')
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
#plt.bar(x,y)
#plt.show()
print("The categories and their values represented by the first and second argument as arrays.")
print("Horizontal Bars\nIf you want the bars to be displayed horizontally instead of vertically, use the barh() function:")
#plt.barh(x,y)
#plt.show()
print("Bar Color\nThe bar() and barh() takes the keyword argument color to set the color of the bars:")
#plt.bar(x,y,color="red")
#plt.show()
print('Color Names\nYou can use any of the 140 supported color names.')
#plt.bar(x,y, color = "hotpink")
#plt.show()
print("Color Hex\nOr you can use Hexadecimal color values:")
#plt.bar(x,y, color = "#4CAF50")
#plt.show()
print('Bar Width\nThe bar() takes the keyword argument width to set the width of the bars:')
#plt.bar(x,y,width = 0.1)
#plt.show()
print('The default width value is 0.8\n For horizontal bars, use height instead of width.')
print('\nBar Height\nThe barh() takes the keyword argument height to set the height of the bars:\nThe default height value is 0.8')
#plt.barh(x,y,height = 0.1)
#plt.show()

print("Matplotlib Histograms\nA histogram is a graph showing frequency distributions.\nIt is a graph showing the number of observations within each given interval.")
print('Create Histogram\nIn Matplotlib, we use the hist() function to create histograms.\nThe hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.\nFor simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10. Learn more about Normal Data Distribution in our Machine Learning Tutorial.')
x = np.random.normal(170,10,250)
#plt.hist(x)
#plt.show()

print("Matplotlib Pie Charts\nCreating Pie Charts\nWith Pyplot, you can use the pie() function to draw pie charts:")
y = np.array([35,25,25,15])
#plt.pie(y)
#plt.show()
print('Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:\nThe value divided by the sum of all values: x/sum(x)')
print("Labels\nAdd labels to the pie chart with the label parameter.\nThe label parameter must be an array with one label for each wedge:")
mylabels = ["Apples","Bananas","Cherries","Dates"]
#plt.pie(y, labels = mylabels)
#plt.show()

print('Start Angle\nsAs mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.\nThe startangle parameter is defined with an angle in degrees, default angle is 0:')
#plt.pie(y, labels = mylabels, startangle=90)
#plt.show()

print('Explode\nMaybe you want one of the wedges to stand out? The explode parameter allows you to do that.\nThe explode parameter, if specified, and not None, must be an array with one value for each wedge.\nEach value represents how far from the center each wedge is displayed:')
myexplode = [0.2,0.1,0.1,0]
#plt.pie(y, labels = mylabels, explode = myexplode)
#plt.show()

print("Shadow\nAdd a shadow to the pie chart by setting the shadows parameter to True:")
#plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
#plt.show()

print('Colors\nYou can set the color of each wedge with the colors parameter.\nThe colors parameter, if specified, must be an array with one value for each wedge:')
mycolors = ["black", "hotpink", "b", "#4CAF50"]
#plt.pie(y, labels = mylabels, colors = mycolors)
#plt.show() 

print('Legend\nTo add a list of explanation for each wedge, use the legend() function:')
#plt.pie(y, labels = mylabels)
#plt.legend()
#plt.show()

print("Legend With Header\nTo add a header to the legend, add the title parameter to the legend function.")
#plt.pie(y, labels = mylabels)
#plt.legend(title = "Four Fruits:")
#plt.show()
