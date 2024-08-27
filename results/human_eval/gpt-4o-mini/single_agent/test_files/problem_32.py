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


    # Using Newton's method to find the root of the polynomial
    def f(x):
        return poly(xs, x)

    def df(x):
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

    x0 = 0  # Initial guess
    tolerance = 1e-7
    max_iterations = 1000

    for _ in range(max_iterations):
        fx0 = f(x0)
        dfx0 = df(x0)

        if abs(fx0) < tolerance:
            return x0

        if dfx0 == 0:  # Avoid division by zero
            break

        x1 = x0 - fx0 / dfx0

        if abs(x1 - x0) < tolerance:
            return x1

        x0 = x1

    return None  # If no root is found within max_iterations



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