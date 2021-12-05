print("SciPy Tutorial\nSciPy is a scientific computation library that uses NumPy underneath.\nSciPy stands for Scientific Python.")
print("What is SciPy?\nSciPy is a scientific computation library that uses NumPy underneath.\nSciPy stands for Scientific Python.\nIt provides more utility functions for optimization, stats and signal processing.\nLike NumPy, SciPy is open source so we can use it freely.\nSciPy was created by NumPy's creator Travis Olliphant.\n\nWhy Use SciPy?\nIf SciPy uses NumPy underneath, why can we not just use NumPy?\nSciPy has optimized and added functions that are frequently used in NumPy and Data Science.\n\nWhich Language is SciPy Written in?\nSciPy is predominantly written in Python, but a few segments are written in C.")
print("Installation of SciPy\npip install scipy")
print('\nImport SciPy\nOnce SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:\nfrom scipy import constants')
from scipy import constants
print("How many cubic meters are in one liter:")
print(constants.liter)
print('constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.')
print('Checking SciPy Version\nThe version string is stored under the __version__ attribute.')
import scipy
print(scipy.__version__)

print("SciPy Constants\nAs SciPy is more focused on scientific implementations, it provides many built-in scientific constants.\nThese constants can be helpful when you are working with Data Science.\nPI is an example of a scientific constant.")
print(constants.pi)

print('Constant Units\nA list of all units under the constants module can be seen using the dir() function.')
print(dir(constants))

print("Unit Categories\nThe units are placed under these categories:\nMetric\nBinary\nMass\nAngle\nTime\nLength\nPressure\nVolume\nSpeed\nTemperature\nEnergy\nPower\nForce")
print('\n\nMetric (SI) Prefixes:\nReturn the specified unit in meter (e.g. centi returns 0.01)')
from scipy import constants

print("yotta = ",constants.yotta)
print("zetta = ",constants.zetta)
print("exa = ",constants.exa)
print("peta = ",constants.peta)
print("tera = ",constants.tera)
print("giga = ",constants.giga)
print("mega = ",constants.mega)
print("kilo = ",constants.kilo)
print("hecto = ",constants.hecto)
print("deka = ",constants.deka)
print("deci = ",constants.deci)
print("centi = ",constants.centi)
print("milli = ",constants.milli)
print("micro = ",constants.micro)
print("nano = ",constants.nano)
print("pico = ",constants.pico)
print("femto = ",constants.femto)
print("atto = ",constants.atto)
print("zepto = ",constants.zepto)

print('\n\nBinary Prefixes:\nReturn the specified unit in bytes (e.g. kibi returns 1024)')
from scipy import constants
print("kibi = ",constants.kibi)
print("mebi = ",constants.mebi)
print("gibi = ",constants.gibi)
print("tebi = ",constants.tebi)
print("pebi = ",constants.pebi)
print("exbi = ",constants.exbi)
print("zebi = ",constants.zebi)
print("yobi = ",constants.yobi)

print("\n\nMass:\nReturn the specified unit in kg (e.g. gram returns 0.001)")
from scipy import constants
print("gram = ",constants.gram)        #0.001
print("metric_ton = ",constants.metric_ton)  #1000.0
print("grain = ",constants.grain)       #6.479891e-05
print("lb = ",constants.lb)          #0.45359236999999997
print("pound = ",constants.pound)       #0.45359236999999997
print("oz = ",constants.oz)          #0.028349523124999998
print("ounce = ",constants.ounce)       #0.028349523124999998
print("stone = ",constants.stone)       #6.3502931799999995
print("long_ton = ",constants.long_ton)    #1016.0469088
print("short_ton = ",constants.short_ton)   #907.1847399999999
print("troy_ounce = ",constants.troy_ounce)  #0.031103476799999998
print("troy_pound = ",constants.troy_pound)  #0.37324172159999996
print("carat = ",constants.carat)       #0.0002
print("atomic _mass = ",constants.atomic_mass) #1.66053904e-27
print("m_u = ",constants.m_u)         #1.66053904e-27
print("u = ",constants.u)           #1.66053904e-27

print('\n\nAngle:\nReturn the specified unit in radians (e.g. degree returns 0.017453292519943295)')
print("degree = ",constants.degree)     #0.017453292519943295
print("arcmin = ",constants.arcmin)     #0.0002908882086657216
print("arcminute = ",constants.arcminute)  #0.0002908882086657216
print("arcsec = ",constants.arcsec)     #4.84813681109536e-06
print("arcsecond = ",constants.arcsecond)  #4.84813681109536e-06

print("\n\nTime:\nReturn the specified unit in seconds (e.g. hour returns 3600.0)")
print("minute = ",constants.minute)      #60.0
print("hour = ",constants.hour)        #3600.0
print("day = ",constants.day)         #86400.0
print("week = ",constants.week)        #604800.0
print("year = ",constants.year)        #31536000.0
print("julian_year = ",constants.Julian_year) #31557600.0

print('\n\nLength:\nReturn the specified unit in meters (e.g. nautical_mile returns 1852.0)')
print("inch = ",constants.inch)              #0.0254
print("foot = ",constants.foot)              #0.30479999999999996
print("yard = ",constants.yard)              #0.9143999999999999
print("mile = ",constants.mile)              #1609.3439999999998
print("mil = ",constants.mil)               #2.5399999999999997e-05
print("pt = ",constants.pt)                #0.00035277777777777776
print("point = ",constants.point)             #0.00035277777777777776
print('survey_point = ',constants.survey_foot)       #0.3048006096012192
print("survey_mile = ",constants.survey_mile)       #1609.3472186944373
print("nautical_mile = ",constants.nautical_mile)     #1852.0
print("fermi = ",constants.fermi)             #1e-15
print("angstrom = ",constants.angstrom)          #1e-10
print("micron = ",constants.micron)            #1e-06
print("au = ",constants.au)                #149597870691.0
print("astronomical_unit = ",constants.astronomical_unit) #149597870691.0
print("light_year = ",constants.light_year)        #9460730472580800.0
print("parsec = ",constants.parsec)            #3.0856775813057292e+16

print('\n\nPressure:\nReturn the specified unit in pascals (e.g. psi returns 6894.757293168361)')
print("atm = ",constants.atm)         #101325.0
print("atmosphere = ",constants.atmosphere)  #101325.0
print("bar = ",constants.bar)         #100000.0
print("torr = ",constants.torr)        #133.32236842105263
print("mmHg = ",constants.mmHg)        #133.32236842105263
print("psi = ",constants.psi)         #6894.757293168361

print('\n\nArea:\nReturn the specified unit in square meters(e.g. hectare returns 10000.0)')
print("hectare = ",constants.hectare) #10000.0
print("acre = ",constants.acre)    #4046.8564223999992

print('\n\nVolume:\nReturn the specified unit in cubic meters (e.g. liter returns 0.001)')
print("liter = ",constants.liter)            #0.001
print("litre = ",constants.litre)            #0.001
print("gallon = ",constants.gallon)           #0.0037854117839999997
print("gallon_US = ",constants.gallon_US)        #0.0037854117839999997
print("gallon_imp = ",constants.gallon_imp)       #0.00454609
print("fiuld_ounce = ",constants.fluid_ounce)      #2.9573529562499998e-05
print("fluid_ounce_US = ",constants.fluid_ounce_US)   #2.9573529562499998e-05
print("fluid_ounce_imp = ",constants.fluid_ounce_imp)  #2.84130625e-05
print("barrel = ",constants.barrel)           #0.15898729492799998
print("bbl = ",constants.bbl)              #0.15898729492799998

print('\n\nSpeed:\nReturn the specified unit in meters per second (e.g. speed_of_sound returns 340.5)')
print("kmh = ",constants.kmh)            #0.2777777777777778
print("mph = ",constants.mph)            #0.44703999999999994
print("mach = ",constants.mach)           #340.5
print("speed_of_sound = ",constants.speed_of_sound) #340.5
print("knot = ",constants.knot)           #0.5144444444444445

print('\n\nTemperature:\nReturn the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)')
print("Zero_Celsius = ",constants.zero_Celsius)      #273.15
print("degree_Farenheit = ",constants.degree_Fahrenheit) #0.5555555555555556

print("\n\nEnergy:\nReturn the specified unit in joules (e.g. calorie returns 4.184)")
print("eV = ",constants.eV)            #1.6021766208e-19
print("electron_volt = ",constants.electron_volt) #1.6021766208e-19
print("calorie = ",constants.calorie)       #4.184
print("calorie-th = ",constants.calorie_th)    #4.184
print("calorie_IT = ",constants.calorie_IT)    #4.1868
print("erg = ",constants.erg)           #1e-07
print("Btu = ",constants.Btu)           #1055.05585262
print("Btu_it = ",constants.Btu_IT)        #1055.05585262
print("Btu_th = ",constants.Btu_th)        #1054.3502644888888
print("ton_TNT = ",constants.ton_TNT)       #4184000000.0

print('\n\nPower:\nReturn the specified unit in watts (e.g. horsepower returns 745.6998715822701)')
print("hp = ",constants.hp)         #745.6998715822701
print("horsepower = ",constants.horsepower) #745.6998715822701

print('\n\nForce:\nReturn the specified unit in newton (e.g. kilogram_force returns 9.80665)')
print("dyn = ",constants.dyn)             #1e-05
print("dyne = ",constants.dyne)            #1e-05
print("lbf = ",constants.lbf)             #4.4482216152605
print("pound_force = ",constants.pound_force)     #4.4482216152605
print("kgf = ",constants.kgf)             #9.80665
print("kilogram_force = ",constants.kilogram_force)  #9.80665

print("\n\nSciPy Optimizers\nOptimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.\nOptimizing Functions\nEssentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.\nRoots of an Equation\nNumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:\nx + cos(x)\nFor that you can use SciPy`s optimze.root function.\nThis function takes two required arguments:\nfun - a function representing an equation.\nx0 - an initial guess for the root.\nThe function returns an object with information regarding the solution.\nThe actual solution is given under attribute x of the returned object:")
print("\n\nFind root of the equation x + cos(x):")
from scipy.optimize import root
from math import cos
def eqn(x):
	return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
print('Note: The returned object has much more information about the solution.')
print(myroot)

print("Minimizing a Function\nA function, in this context, represents a curve, curves have high points and low points.\nHigh points are called maxima.\nLow points are called minima.\nThe highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.\nThe lowest point in whole curve is called global minima, whereas the rest of them are called local minima.")
print("Finding Minima\nWe can use scipy.optimize.minimize() function to minimize the function.\nThe minimize() function takes the following arguments:\nfun - a function representing an equation.\nx0 - an initial guess for the root.\nmethod - name of the method to use. Legal values:\n    'CG'\n    'BFGS'\n    'Newton-CG'\n    'L-BFGS-B'\n    'TNC'\n    'COBYLA'\n    'SLSQP'\ncallback - function called after each iteration of optimization.\noptions - a dictionary defining extra params:\n{\n     'disp': boolean - print detailed description\n     'gtol': number - the tolerance of the error\n  }")

from scipy.optimize import minimize
def eqn(x):
	return x**2 + x + 2
mymin = minimize(eqn,0,method="BFGS")
print(mymin)

print("SciPy Sparse Data\nWhat is Sparse Data\nSparse data is data that has mostly unused elements (elements that don't carry any information ).\nIt can be an array like this one:\n[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]\nSparse Data: is a data set where most of the item values are zero.\nDense Array: is the opposite of a sparse array: most of the values are not zero.\nIn scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.\nHow to Work With Sparse Data\nSciPy has a module, scipy.sparse that provides functions to deal with sparse data.\nThere are primarily two types of sparse matrices that we use:\nCSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.\nCSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products\nWe will use the CSR matrix in this tutorial.\nCSR Matrix\nWe can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().")
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

print('From the result we can see that there are 3 items with value.\nThe 1. item is in row 0 position 5 and has the value 1.\nThe 2. item is in row 0 position 6 and has the value 1.\nThe 3. item is in row 0 position 8 and has the value 2.')

print("\nSparse Matrix Methods\nViewing stored data (not the zero items) with the data property:")
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).data)

print("Counting nonzeros with the count_nonzero() method:")
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).count_nonzero())

print('Removing zero-entries from the matrix with the eliminate_zeros() method:')
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

print('Eliminating duplicate entries with the sum_duplicates() method:')
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

print('Converting from csr to csc with the tocsc() method:')
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)

print("\n\nSciPy Graphs\nWorking with Graphs\nGraphs are an essential data structure.\nSciPy provides us with the module scipy.sparse.csgraph for working with such data structures.\nAdjacency Matrix\nAdjacency matrix is a nxn matrix where n is the number of elements in a graph.\nAnd the values represents the connection between the elements.")
print("Connected Components\nFind all of the connected components with the connected_components() method.")

from scipy.sparse.csgraph import connected_components
arr = np.array([
	[0,1,2],
	[1,0,0],
	[2,0,0]
])
newarr = csr_matrix(arr)
print(connected_components(newarr))

print('Dijkstra\nUse the dijkstra method to find the shortest path in a graph from one element to another.\nIt takes following arguments:\nreturn_predecessors: boolean (True to return whole path of traversal otherwise False).\nindices: index of the element to return all paths from that element only.\nlimit: max weight of path.')
print("Find the shortest path from element 1 to 2:")
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
arr = np.array([
	[0,1,2],
	[1,0,0],
	[2,0,0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr,return_predecessors=True, indices=0))
