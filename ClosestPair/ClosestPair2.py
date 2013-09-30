# python
#
# Author: FreeTymeKiyan
# Date: 2013-09-30
#
# implement a divide and conquer closest pair algorithm
# 1. read and parse .txt file
# 2. use the parsed result as input
# 3. find the closest pair in these input points
# 4. output the closest pair and the distance between the pair
#	output format
#	the closest pair is (x1, x2) and (y1, y2).
#	the distance between them is d = xxx.

from sys import argv
from operator import attrgetter, itemgetter
from math import sqrt

infinity = float('inf')

# define a class to express point
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def print_self(self):
		return '(%g, %g)' % (self.x, self.y) 

# calculate square
def square(x):
	return x * x

# calculate the distance between two points
def distance(point_1, point_2):
	return sqrt(square(point_1.x - point_2.x) + square(point_1.y - point_2.y))

# 
def closest_pair(point):
	x_p = sorted(point, key = attrgetter('x'))
	y_p = sorted(point, key = attrgetter('y'))
	#for p in x_p:
	#	p.print_self()
	#for p in y_p:
	#	p.print_self()

	return divide_and_conquer(x_p, y_p)

# implement divide and conquer algorithm 
def divide_and_conquer(x_p, y_p):
	n = len(x_p)
	if n <= 3:
		return brute_force(x_p)
	p_l = x_p[:n / 2]
	p_r = x_p[n / 2:]
	y_l, y_r = [], []
	x_divider = p_l[-1].x
	
	for p in y_p:
		if p.x <= x_divider:
			y_l.append(p)
		else:
			y_r.append(p)
	d_l, pair_l = divide_and_conquer(p_l, y_l)
	d_r, pair_r = divide_and_conquer(p_r, y_r)

	d_m, pair_m = (d_l, pair_l) if d_l < d_r else (d_r, pair_r)

	close_y = [p for p in y_p if abs(p.x - x_divider < d_m)] # choose from y_p
	n_close_y = len(close_y)
	if n_close_y > 1:
		closest_y = min(((distance(close_y[i], close_y[j]), (close_y[i], close_y[j]))
		for i in range(n_close_y - 1)
		for j in range(i + 1, min(i + 8, n_close_y))), 
		key = itemgetter(0)) # why 8? change itemgetter.
		return (d_m, pair_m) if d_m <= closest_y[0] else closest_y
	else:
		d_m, pair_m

# implement the brute-force algorithm
def brute_force(point):
	n = len(point)
	if n < 2:
		return infinity, (None, None)
	return min( ((distance(point[i], point[j]), (point[i], point[j]))
		for i in range(n - 1)
		for j in range(i + 1, n)),
		key = itemgetter(0))

# main, start here
# add a usage notice
if len(argv) != 2:
	print 'Usage: python ClosestPair.py <filename>'
	exit (1) 	

script, filename = argv
txt = open(filename)

# parse a certain format of .txt file
points = []
for line in txt:
	x = float(line.split(',')[0])
	y = float(line.split(',')[1])
	p = Point(x, y)
	#print p.x, p.y
	points.append(p)

#for p in points:
#	print p

min_d, (point_1, point_2) = closest_pair(points)

print 'the closest pair is: ', point_1.print_self(), point_2.print_self()
print 'the distance between them is d = ', min_d

txt.close()
