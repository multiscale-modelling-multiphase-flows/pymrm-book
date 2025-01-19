# Particle model: first order reaction

Numerically solve the stationary spherical symmetric problem

$$\frac{1}{r^{2}}\frac{\partial}{\partial r}\left( r^{2}D\frac{\partial c}{\partial r} \right) - kc = div\left( D\ grad(c) \right) - kc = 0$$

with $c(R) = 1$.

**Questions**:

a)  Perform the spatial discretization (start with a uniform grid) and
    make a Python implementation. Note that the spherical geometry is
    accounted for by the proper definition of the divergence operator.

b)  Construct, implement and solve the matrix-vector equation.

c)  Compute the apparent reaction rate from the concentration gradient
    on the surface of the particle.

d)  Investigate the effectiveness as function of Thiele modulus

e)  Does the result correspond to the analytical solution?

f)  Consider the high Thiele modulus case and provide an improvement by
    using a spatial discretization that is refined near the wall.
