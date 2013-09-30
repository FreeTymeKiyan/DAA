# python
# implement a divide and conquer closest pair algorithm
# 1. check read and parse .txt file
# 2. use the parsed result as the input
# 3. find the closest pair in these input points
# 4. output the closest pair and the distance between the pair
#	output format
#	The closest pair is (x1, x2) and (y1, y2).
#	The distance between them is d = xxx.

from sys import argv
from random import randint, randrange
from operator import itemgetter, attrgetter

infinity = float('inf')

# calculate the square of a number 
#def square(x):
#	return x * x

# calculate distance between two points
#def square_distance(p, q):
#	return square(p[0] - q[0]) + square(p[1] - q[1])

# closest_pair, use real numbers to express points
def closest_pair(point):
	x_p = sorted(point, key = attrgetter('real')) # x is the real part
	#print 'x_p: ', x_p
	y_p = sorted(point, key = attrgetter('imag')) # y is the imaginary part
	#print 'y_p: ', y_p
	return divide_and_conquer(x_p, y_p)
#
def brute_force(point):
	n = len(point)
	if n < 2:
		return infinity, (None, None)
	return min( ((abs(point[i] - point[j]), (point[i], point[j]))
		for i in range(n - 1)
		for j in range(i + 1, n)),
		key = itemgetter(0))
#
def divide_and_conquer(x_p, y_p):
	n = len(x_p) # number of points
	if n <= 3:
		return brute_force(x_p)
	print 'n: ', n
	p_l = x_p[:n / 2] # when n == 1, p_l is empty
	p_r = x_p[n / 2:]
	print 'p_l: ', p_l
	print 'p_r: ', p_r
	y_l, y_r = [], []
	x_divider = p_l[-1].real # last x of p_l, when p_l is empty, wrong
	print 'x_divider: ', x_divider
	for p in y_p:
		if p.real <= x_divider:
			y_l.append(p)
		else:
			y_r.append(p)
	d_l, pair_l = divide_and_conquer(p_l, y_l) # divide into left and right
	d_r, pair_r = divide_and_conquer(p_r, y_r)

	d_m, pair_m = (d_l, pair_l) if d_l < d_r else (d_r, pair_r)

	close_y = [p for p in y_p if abs(p.real - x_divider) < d_m]
	n_close_y = len(close_y) # points with d_m
	if n_close_y > 1:
		closest_y = min(((abs(close_y[i] - close_y[j]), (close_y[i], close_y[j]))
		for i in range(n_close_y - 1)
		for j in range(i+1, min(i+8, n_close_y))),
		key = itemgetter(0))
		return (d_m, pair_m) if d_m <= closest_y[0] else closest_y
	else:
		return d_m, pair_m

# main start from here	
point_list = [randint(0,5) + 1j * randint(0, 5) for i in range(10)]

print point_list
print '		closest pair:', closest_pair(point_list)

# read .txt file
#script, filename = argv
#txt = open(filename)
#print "Here's your file %r: " % filename
# check read result
# print txt.read()
# parse .txt file
#for line in txt:
#	x = line.split(',')[0]
#	y = line.split(',')[1]
#	print x,
#	print y
	
# remember to close
#txt.close()

