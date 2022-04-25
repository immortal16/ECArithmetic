# ECArithmetic

Сontains basic functions of elliptic curves arithmetic: doubling a point, addition of two points, scalar multiplication and converting between affine/projective form.

## Including

- params - set of parameters of the P-192 curve from ECDSA;
- helpers - egcd and modular multiplicative inverse;
- curve - elliptic curve class;
- point - affine and projective point classes (contains all functionality described above);
- main - simple proof of correctness with the P-192 point.
