import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc_cov(a, b):
	a_mean = np.mean(a)
	b_mean = np.mean(b)
	sum = 0
	for n in range(len(a)):
		sum += (a[n] - a_mean) * (b[n] - b_mean)
#	return ((sum)/(len(a) + len(b)))
	return sum / len(a)
def Charles():
	x1 = [2, 2, 4, 4, 8, 8, 1]
	y1 = [3, 3, 3, 2, 4, 8, 7]
	print("x1 Sum: {} . x1 mean: {} x1 variance {}".format(sum(x1), np.mean(x1), np.var(x1)))
	print("y1 Sum: {} . y1 mean: {} y1 variance {}".format(sum(y1), np.mean(y1), np.var(y1)))
	print("Covariance of x1 and y1 {} {}".format(((calc_cov(x1, y1))), np.cov(x1, y1, bias=True)[0][1]))
	pass
	
Charles()