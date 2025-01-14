# Ternary diffusion with Maxwell-Stefan equations

Consider the two-bulb diffusion experiment where bulb A contains a 50-50
molar-% $N_{2}$ and ${CO}_{2}$ mixture and bulb B a 50-50 molar-%
$N_{2}$ and $H_{2}$ mixture. The bulbs are connected by a capillary with
length $\delta = 0.086\ m$. We will consider the diffusion of the three
gasses.

![A diagram of a blue circle with text Description automatically
generated](./media/image10.png){width="5.532772309711286in"
height="1.0947233158355205in"}

Let's label the three components as 1: $H_{2}$, 2: $N_{2}$ and 3:
${CO}_{2}$. The binary Maxwell-Stefan diffusivities are
$Đ_{12} = 83.6 \cdot 10^{- 6}\ \frac{m^{2}}{s}$,
$Đ_{13} = 68 \cdot 10^{- 6}\ \frac{m^{2}}{s}$ and
$Đ_{23} = 16.8 \cdot 10^{- 6}\ \frac{m^{2}}{s}$. The pressure and
temperature are $P = 1.01 \cdot 10^{5}\ Pa$ and $T = 308\ K$,
respectively.

The Maxwell-Stefan equations for the first two components can be written
as:

$${\frac{dx_{1}}{dz} = \frac{x_{1}N_{2} - x_{2}N_{1}}{c_{tot}\ Đ_{12}\ } + \frac{x_{1}N_{3} - x_{3}N_{1}}{c_{tot}\ Đ_{13}\ }
}{\frac{dx_{2}}{dz} = \frac{x_{2}N_{1} - x_{1}N_{2}}{c_{tot}\ Đ_{12}\ } + \frac{x_{2}N_{3} - x_{3}N_{2}}{c_{tot}\ Đ_{23}\ }}$$

Using the constraint $x_{3} = 1 - x_{1} - x_{2}$ and the bootstrap
$N_{1} + N_{2} + N_{3} = 0$ the mole fraction and molar flux of the
third component can be eliminated from the set of equation.

**Questions**:

a)  Implement and numerically the ODE for the components $1$ and $2$
    using the boundary conditions at $z = 0$: $x_{1} = 0$ and
    $x_{2} = 0.5$. Use a shooting method to compute $N_{1}$ and $N_{2}$
    from the boundary conditions at $z = \delta$: : $x_{1} = 0.5$ and
    $x_{2} = 0.5$.

**Hints: In Python you can use SciPy's solve_ivp to solve the ODE and
SciPy's root (or newton from pymrm) to obtain**
$\mathbf{N}_{\mathbf{1}}$ **and** $\mathbf{N}_{\mathbf{2}}$ **such that
the boundary conditions at** $\mathbf{z = \delta}$ **are obeyed.**

b)  Linearize the Maxwell-Stefan equations and compute the fluxes by
    solving the set of two linear equations.

c)  Use the method of Toor, Steward and Prober to solve the ternary
    Maxwell-Stefan diffusion problem.

d)  Numerically solve the problem as a boundary value problem to compute
    the fluxes and compositions in the capillary (e.g. using the pymrm
    building blocks).

e)  Consider a time-dependent problem where the concentrations in the
    bulb evolve. The bulb volumes are
    $V_{A} = 77.99 \cdot 10^{- 6}\ m^{3}$,
    $V_{B} = 78.63 \cdot 10^{- 6}\ m^{3}$. The capillary has
    cross-sectional area $A_{d} = 3.87{\cdot 10}^{- 5}\ m^{2}$ and
    length $d = 0.086\ m$. Assume, constant pressures is maintained in
    the bulbs and ideal gas-law, such that $c_{tot}$ is equal and
    constant in time throughout the system and $N_{tot} = 0$. Assume
    pseudo-steady state in the capillary and use a linearization to
    compute the flux as function of composition in the bulbs.
