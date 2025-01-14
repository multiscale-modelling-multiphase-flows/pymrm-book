# Multi-component 1D counter-diffusion with reaction

Build a model of two reactive components counter-diffusing in a
membrane. A chemical reaction is carried out in a membrane reactor. The
reaction scheme and reaction kinetics are given as follows:

$$A + B \rightleftarrows C + D$$

Reaction kinetics:
$- r_{A} = \  - r_{B} = r_{C} = r_{D} = k_{1}c_{A}c_{B} - k_{2}c_{C}c_{D}\ $.
The reactants A and B are fed at different sides of a porous membrane.
The concentrations on the boundaries are provided in the figure below.
For the description of this problem you may assume that the diffusion
obeys Fick's law.

A

c~A~ = 10 kmol/m^3^

c~B~ = 0

c~C~ = 0

c~D~ = 0

C, D

B

c~A~ = 0

c~B~ = 10 kmol/m^3^

c~C~ = 0

c~D~ = 0

C, D

y = 0 y = L\
y

Ceramic membrane

  --------------------------------------------------- -------------------
  Membrane thickness $L$                              0.01 m

  Kinetic constant $k_{1}$                            10^6^ m^3^/(kmol s)

  Kinetic constant $k_{2}$                            0 m^3^/(kmol s)

  Effective diffusion coefficients of A, B, C and D   10^-5^ m^2^/s
  --------------------------------------------------- -------------------

**Questions**:

a)  Write down the governing steady-state equations. For the diffusive
    term use the notation with a divergence and gradient operator.

b)  Write down the spatially discretized equations in terms of matrices
    corresponding to the discretization of the divergence and gradient
    operator. Discuss, how the boundary conditions contribute to the
    discretized equations.

c)  The reaction term is non-linear. Formulate the equation to be solved
    as a root-seeking problem (i.e. a set of non-linear equations that
    all need equal zero).

d)  Formulate the solution algorithm applying the Newton-Raphson method.

e)  Provide a Python implementation for the set of equations and its
    Jacobian using the pymrm building blocks: construct_grad,
    construct_div and numjac_local.

f)  Implement the numerical solution using the newton function from the
    py_mrm package.

g)  Obtain the steady state solution using Newton-Raphson iteration.

h)  Make an unsteady implementation assuming initial zero
    concentrations.

i)  Play with the reaction rates and boundary conditions.
