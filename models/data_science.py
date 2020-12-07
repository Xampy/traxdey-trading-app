###########################################################"
#
#
# Data science tools
#
#
#############################################################


import math


#Vectors
def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))

#Statisitques

def mean(x):
	""" Average """
	return sum(x)/len(x)

def de_mean(x):
	x_bar = mean(x)

	return [x_i - x_bar for x_i in x]

def sum_of_squares(x):
	return sum([x_i **2 for x_i in x])

def variance(x):

	n = len(x)
	deviations = de_mean(x)
	return ( sum_of_squares(deviations)/(n-1) )

# Ecart type
def standard_deviation(x):
	return math.sqrt(variance(x))


def covariance(x, y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)


def getLinearRegressionEquationYeX(x, y):

	a = covariance(x, y)/variance(x)
	b = mean(y) - a * mean(x)


	return (a, b)


def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / stdev_x / stdev_y
	else:
		return 0 # en l’absence de variation, la corrélation est à zéro





################################################################
#
#  Linear regression
#
#####################################################################

def predict(alpha, beta, x_i):
	return beta * x_i + alpha