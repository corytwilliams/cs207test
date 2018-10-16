import cmath

def quad_roots(a,b=0,c=0):

	'''returns roots of a quadratic function given inputs a,b,c for ax^2+bx+c.

	INPUTS
	==========
	a:	the coefficient for x^2
		type: int or float
	b:	the coefficient for x
		type: int or float
	c: the constant
		type: int or float

	RETURNS
	==========
	roots [(r1,r1c),(r2,r2c)], where r1c and r2c are the complex numbers for the roots.

	NOTES
	==========
	Pre:
		a,b,c are all int or float types. a cannot be zero.
	Post:
		a,b,c are not modified
		returns roots (r1,r1c),(r2,r2c)]


	EXAMPLES
	==========
	>>> quad_roots(1.0,1.0,-12.0)
	((3+0j), (-4+0j))
	'''
	if a==0:
		raise ValueError("The quadratic coefficient cannot equal zero")
	else:
		sqrtdisc = cmath.sqrt(b * b - 4.0 * a * c)
		r1 = -b + sqrtdisc
		r2 = -b - sqrtdisc
		twoa = 2.0 * a
		return (r1 / twoa, r2 / twoa)


def linear_roots(a,b=0):
	'''returns roots of a linear function f(x)=ax+b

	INPUTS
	=========
	a:	the coefficient for x
		type: int or float
	b: the constant
		type: int or float

	RETURNS
	=========
	root r1

	NOTES
	=========
	Pre:
		a,b are all int or float types. a cannot be zero.
	Post:
		a,b are not modified
		returns root r1


	EXAMPLES
	=========
	>>> linear_roots(1,2)
	-2.0
	>>> linear_roots(5,-15)
	3.0
	
	'''
	if a==0:
		raise ValueError("The linear coefficient cannot equal zero")
	else:
		return -b/a
