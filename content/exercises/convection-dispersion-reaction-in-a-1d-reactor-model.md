# Convection-dispersion-reaction in a 1D reactor model 

In this exercise you will build an implicit solver for unsteady
convection-dispersion-reaction equations. A one-component unsteady
convection-reaction equation with constant coefficients has the form

$$\frac{\partial c}{\partial t} + v\ \frac{\partial c}{\partial x} - D_{ax}\ \frac{\partial^{2}c}{\partial x^{2}} - r = 0\  \rightarrow \ \frac{\partial c}{\partial t} + div\left( vc - D_{ax}\ grad(c) \right) - r = 0$$

The solution method will be the method-of-lines where the spatial
dependence is discretized first. After discretization you will get a set
of ODE's that can be written as

$$\frac{\partial\mathbf{c}}{\partial t} + \mathbf{Div} \cdot \left( \mathbf{Conv}\ \mathbf{c + con}\mathbf{v}_{bc}\mathbf{-}D_{ax}\ \left( \mathbf{Grad\ c + gra}\mathbf{d}_{bc} \right) \right) = 0\ $$

Here a component $c_{j}$ of column vector $\mathbf{c}$ denotes the
concentration is spatial cell $j$. For time-discretization we will use
implicit Euler:

$$\mathbf{g}\left( \mathbf{c}^{n + 1} \right)\mathbf{=}\frac{\mathbf{c}^{n + 1}\mathbf{-}\mathbf{c}^{n}}{\Delta t} + \mathbf{Div} \cdot \left( \mathbf{Conv}\ \mathbf{c}^{n + 1}\mathbf{+ con}\mathbf{v}_{bc}\mathbf{-}D_{ax}\ \left( \mathbf{Grad\ }\mathbf{c}^{n + 1}\mathbf{+ gra}\mathbf{d}_{bc} \right) \right) = 0\ $$

**Questions**:

a)  Perform the spatial discretization by constructing the sparse
    matrices for the dispersion and convective terms. Assume a general
    boundary condition at the inlet,

> $$D_{ax}\frac{\partial c}{\partial n} + v\ c = v\ c_{0}$$

and a Neumann boundary condition at the outlet

$$\frac{\partial c}{\partial n} = 0$$

> Make use of the pymrm functions construct_grad, construct_conv, and
> construct_div.

b)  Perform the time discretization for the convection-dispersion by
    means of the implicit Euler scheme, and formulate the problem,
    without reaction, as a root-seeking problem:
    $\mathbf{g}\left( \mathbf{c}^{n + 1} \right)\mathbf{=}0$ for each
    time step.

c)  Provide an Python implementation, that consists of a time-loop,
    where for each timestep the newton method from the pymrm package is
    applied to solve the root-seeking problem.

d)  Test your code for only dispersion, only convection, combined etc.
    Play around with parameters (numerical and physical ones).

e)  Include a first order reaction term. Compare results to the
    analytical solution (in a semi-infinite domain) for steady state.

f)  Adapt the code for general non-linear kinetics. Make use of the
    function numjac_loc to compute the Jacobian of such a reaction term.

g)  Verify your code by implementing a reaction kinetics
    $r = - k\ c^{\alpha}$.
