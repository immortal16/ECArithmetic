import params


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

        if 4 * self.a**3 + 27 * self.b**2 == 0:
            raise Exception('Adjusted curve is not smooth.')

    def __eq__(self, other):
        return True if self.a == other.a and self.b == other.b and self.p == other.p else False


EC = EllipticCurve(params.a, params.b, params.p)