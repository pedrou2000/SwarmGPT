import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """


import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float) -> float:
    """
    Evaluates the derivative of polynomial with coefficients xs at point x.
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(xs, x) = 0.
    find_zero returns only one zero point, even if there are many.
    """
    # Initial guess
    x0 = 0.0
    tolerance = 1e-7
    max_iterations = 1000

    for _ in range(max_iterations):
        fx = poly(xs, x0)
        fpx = poly_derivative(xs, x0)
        
        if abs(fpx) < tolerance:
            raise ValueError("Derivative too small; Newton-Raphson method fails.")
        
        x1 = x0 - fx / fpx
        
        if abs(x1 - x0) < tolerance:
            return x1
        
        x0 = x1

    raise ValueError("Maximum iterations reached; solution did not converge.")

# Example usage and test cases
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Expected: -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Expected: 1.0



METADATA = {}


def check(candidate):
    import math
    import random
    rng = random.Random(42)
    import copy
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        solution = candidate(copy.deepcopy(coeffs))
        assert math.fabs(poly(coeffs, solution)) < 1e-4


check(find_zero)