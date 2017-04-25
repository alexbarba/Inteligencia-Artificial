import random
import math
import numpy as np

LIMIT = 10

def update_temperature(T, k):
    return T - 0.001

def get_neighbors(i, L):
    assert L > 1 and i >= 0 and i < L
    if i == 0:
        return [1]
    elif i == L - 1:
        return [L - 2]
    else:
        return [i - 1, i + 1]

def make_move(x, A, T):
    # nhbs = get_neighbors(x, len(A))
    # nhb = nhbs[random.choice(range(0, len(nhbs)))]
    nhb = random.choice(xrange(0, len(A))) # choose from all points

    delta = A[nhb] - A[x]

    if delta < 0:
        return nhb
    else:
        p = math.exp(-delta / T)
        return nhb if random.random() < p else x

def simulated_annealing(A):
    L = len(A)
    x0 = random.choice(xrange(0, L))
    T = 1.
    k = 1

    x = x0
    x_best = x0

    while T > 1e-3:
        x = make_move(x, A, T)
        if(A[x] < A[x_best]):
            x_best = x
        T = update_temperature(T, k)
        k += 1

    print "iterations:", k
    return x, x_best, x0

def isminima_local(p, A):
    return all(A[p] < A[i] for i in get_neighbors(p, len(A)))

def func(x):
    return math.sin((2 * math.pi / LIMIT) * x) + 0.001 * random.random()
'''
def initialize(L):
    return map(func, xrange(0, L))
'''
def initialize():
	A = np.matrix(
		[[float('inf'), 4180, 2306, 2848, 2529, 2409, 4005, 1583],
		[4180, float('inf'), 1874, 1332, 1719, 2046, 1062, 2819],
		[2306, 1874, float('inf'), 542, 223, 789, 1699, 1202],
		[2848, 1332, 542, float('inf'), 389, 933, 1557, 1487],
		[2529, 1719, 223, 389, float('inf'), 711, 1544, 1140],
		[2409, 2046, 789, 933, 711, float('inf'), 1803, 826],
		[4005, 1062, 1699, 1157, 1544, 1803, float('inf'), 2644],
		[1583, 2819, 1202, 1487, 1140, 826, 2644, float('inf')]])
		
	costs = []
	n = len(A)	
	print A
	'''
	for i in range(n):
			A[i][i]=float('inf')
	
	for i in range(n):
		for j in xrange(i, i+1):
			1 +1 
	'''
	return A	
def main():
    A = initialize()
    
    #print A[0][0]
    
'''
    local_minima = []
    for i in xrange(0, LIMIT):
        if(isminima_local(i, A)):
            local_minima.append([i, A[i]])
            
    print
    print local_minima

    x = 0
    y = A[x]
    for xi, yi in enumerate(A):
        if yi < y:
            x = xi
            y = yi
    global_minumum = x

    print "number of local minima: %d" % (len(local_minima))
    print "global minimum @%d = %0.3f" % (global_minumum, A[global_minumum])

    x, x_best, x0 = simulated_annealing(A)
    print "Solution is @%d = %0.3f" % (x, A[x])
    print "Best solution is @%d = %0.3f" % (x_best, A[x_best])
    print "Start solution is @%d = %0.3f" % (x0, A[x0])
    '''


main()
