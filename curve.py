import params
import random as rn

from helpers import solver


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        
        self.eq = lambda x: x**3 + self.a * x + self.b

        if 4 * self.a**3 + 27 * self.b**2 == 0:
            raise Exception('Adjusted curve is not smooth.')

    def __eq__(self, other):
        return True if self.a == other.a and self.b == other.b and self.p == other.p else False
    
        def test_point(self, x, y, z):
        return (y**2 * z) % self.p == (x**3 + self.a * x * z**2 + self.b * z**3) % self.p

    def get_random_point(self):

        res = 1, 1

        while not self.test_point(res[0], res[1], 1):

            t = rn.randint(1, self.p)
            x = pow(t, 2, self.p)

            y_2 = self.eq(x) % self.p
            y = solver(y_2, self.p)

            res = x, y

        return res


EC = EllipticCurve(params.a, params.b, params.p)
