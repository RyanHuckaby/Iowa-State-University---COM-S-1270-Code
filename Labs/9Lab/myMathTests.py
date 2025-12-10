"""
Ryan Huckaby
Lab #9 (Week Eleven)
Date Started: 11/5/2025
This code tests whether the math functions are correct or not.
"""
import myMath as m

def test_add():
    assert m.add(1, 1) == 2
    assert m.add(10, 0) == 10

def test_subtract():
    assert m.subtract(2, 1) == 1
    assert m.subtract(2, 3) == -1

def test_multiply():
    assert m.multiply(5, 4) == 20
    assert m.multiply(1, 5) == 5

def test_divide():
    assert m.divide(5, 0) == 5
    assert m.divide(10, 2) == 5

def test_power():
    assert m.power(1, 2) == 1
    assert m.power(2, 4) == 16

def test_factorial():
    assert m.factorial(5) == 120
    assert m.factorial(7) == 5040

def test_is_prime():
    assert m.is_prime(11) == True
    assert m.is_prime(2) == True

def test_sum_of_digits():
    assert m.sum_of_digits(22) == 4
    assert m.sum_of_digits(3) == 3

def test_gcd():
    assert m.gcd(10, 2) == 2
    assert m.gcd(12, 8) == 4

def test_fib():
    assert m.fib(15) ==  610
    assert m.fib(4) == 3

def test_lcm():
    assert m.lcm(12, 4) == 12
    assert m.lcm(20, 100) == 100

def test_square_root():
    assert m.square_root(-4) == 2
    assert m.square_root(16) == 4

def test_abs_diff():
    assert m.abs_diff(2, 10) == 8
    assert m.abs_diff(1, 0) == 1

def test_log():
    assert m.log(4, 2) == 2
    assert m.log(4, 4) == 1

def test_mod():
    assert m.mod(12, 5) == 2
    assert m.mod(2, 2) == 0

def test_mean():
    assert m.mean((1, 2, 3, 4)) == 2.5
    assert m.mean((2, 10, 40, -10)) == 10.5

def test_median():
    assert m.median((1, 2, 3, 4, 5)) == 3
    assert m.median((1, 2, 8, 8)) == 5

def test_mode():
    assert m.mode((1, 2, 2, 2, 4, 5, 6, 7)) == 2
    assert m.mode(()) == 1

def test_celsius_to_fahrenheit():
    assert m.celsius_to_fahrenheit(0) == 32
    assert m.celsius_to_fahrenheit(10) == 50

def test_fahrenheit_to_celsius():
    assert m.fahrenheit_to_celsius(32) == 0
    assert m.fahrenheit_to_celsius(50) == 10

def test_inverse():
    assert m.inverse(1/2) == 2
    assert m.inverse(0) == 0
    assert m.inverse(2) == 1/2

def test_triangular_number():
    assert m.triangular_number(2) == 3
    assert m.triangular_number(10) == 55