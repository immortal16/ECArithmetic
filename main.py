from point import AffinePoint
from params import n
from curve import EC

x, y = EC.get_random_point()

P = AffinePoint(x, y)

R = P.to_projective()

O = R * n

print(O.to_affine())
