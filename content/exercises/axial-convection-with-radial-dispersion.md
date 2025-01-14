# Axial convection with radial dispersion

Implement species transport in a tube with reaction at the tube wall.
The governing equation is:

$$v\frac{\partial c}{\partial x} = \frac{1}{r}\frac{\partial}{\partial r}\left( r\ D_{rad}\frac{\partial c}{\partial r} \right) = div\left( D_{rad}\ grad(c) \right)$$

The inlet profile is uniform. Assume an infinitely fast surface reaction
at the tube wall. This means $c(R) = 0$. Choose your own parameters or
make equations dimensionless.

**Questions:**

a)  What is the proper boundary conditions at $r = 0$?

b)  Use the method of lines: Perform a spatial discretization in the
    radial direction to obtain a set of ODE's
    ($\frac{d\mathbf{c}}{dx} = \ldots$).

c)  Use a standard SciPy ODE solver, solve_ivp, to solve the set of
    equations.

d)  Compute the flux at the wall as function of $x$.

e)  Compute the Sherwood number (based on
    $\left\langle c \right\rangle$) as function of $x$.
