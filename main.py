from point import AffinePoint
from params import n


P = AffinePoint(10724, 502737023801445091398620853578557381889154568338727796470)
R = P.to_projective()

O = R * n

print(O.to_affine())
