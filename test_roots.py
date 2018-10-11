import pytest
import sys
import roots as rt



def test_quadroots():
    assert rt.quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

test_quadroots()

def test_quadroots_types():
    try:
        rt.quad_roots("", "green", "hi")
    except TypeError as err:
        assert(sys.exc_info()[0] == TypeError)

test_quadroots_types()

def test_quadroots_zerocoeff():
    try:
        rt.quad_roots(a=0.0)
    except ValueError as err:
        assert(sys.exc_info()[0] == ValueError)

test_quadroots_zerocoeff()

def test_linearroots():
	assert rt.linear_roots(5,10) == -2

test_linearroots()

def test_linear_zeroceoff():
	try:
		rt.linear_roots(a=0)
	except ValueError as err:
		assert (sys.exc_info()[0] == ValueError)