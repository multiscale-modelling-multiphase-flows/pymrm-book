# First order reaction in a batch reactor

Implement first order kinetics of one species in a batch reactor.

$$\frac{dc}{dt} = - kc.$$

Suggested approach:

-   Write a function that computes the reaction rate for a provided
    concentration

-   Write this function in such a way that the reaction rate
    coefficients can be passed as parameters.

-   Provide an analytical expression of the concentration as function of
    time. Verify your codes with the analytical solution for the case
    $k = 1\ s^{- 1}$, with initial concentration
    $c_{0} = 1\ \frac{mol}{m^{3}}$.

**Questions**:

a)  Solve using forward Euler discretization

b)  Solve using backward Euler discretization

c)  Solve using scipy.integrate.solve_ivp
