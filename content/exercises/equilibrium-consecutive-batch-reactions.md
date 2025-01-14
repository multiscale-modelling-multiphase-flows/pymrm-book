# Equilibrium consecutive batch reactions

Implement the kinetics:

$$A\begin{matrix}
k_{1} \\
 \rightleftarrows \\
k_{- 1}
\end{matrix}B\begin{matrix}
k_{2} \\
 \rightarrow \\

\end{matrix}C$$

Suggested approach:

-   Write a function that computes the reaction rate for a provided
    concentration

-   Write this function in such a way that the reaction rate
    coefficients can be passed as function argument.

-   Concentration column vector of length 3 as input (for components A,
    B, C)

-   Reaction rate vector of length 3 as output

-   Provide an analytical expression of the concentration as function of
    time. Verify your codes with the analytical solution for the case
    $k_{1} = 2\ s^{- 1}$, $k_{- 1} = 1\ s^{- 1}$ and
    $k_{2} = 3\ s^{- 1}$, with initial concentration
    $c_{A,0} = 1\ \frac{mol}{m^{3}}$, $c_{B,0} = 0\ \frac{mol}{m^{3}}$,
    $c_{C,0} = 0\ \frac{mol}{m^{3}}$.

**Questions**:

a)  Solve using forward Euler discretization

b)  Solve using backward Euler discretization

c)  Implement backward Euler discretization, but allow for extension to
    non-linear kinetics. Express the discretized equations for a
    time-step as a root-seeking problem for the non-linear set of
    equations (and use Newton-Raphson).

d)  Solve using scipy.integrate.solve_ivp.
