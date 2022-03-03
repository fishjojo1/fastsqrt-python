import math
import timeit


import_module = "import math"
test_code = '''
x = 4238974 
n = 7

def fastsqrt():
	initguess = x >> (int(math.log10(x)+1))


	for i in range(n):
		initguess = 0.5 * (initguess + x/initguess)

'''
print(timeit.timeit(stmt=test_code, setup=import_module))
print(timeit.timeit('import math;math.sqrt(4238974)'))

