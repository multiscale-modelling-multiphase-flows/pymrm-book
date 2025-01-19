# Computing residence time distributions

An important characterization of flow patterns and mixing
characteristics in a chemical reactor are residence time distributions.
The cumulative residence time distribution, $F(t)$, can be obtained by
measuring the total flow of a non-reactive tracer component at the
outlet, starting with an empty reactor at $t = 0$ and suppling a
constant inlet tracer flux.

**Questions**:

a)  Write a routine to output the total outlet flux for a multiphase
    model.

b)  Implement the 1D 1-component unsteady convection-dispersion
    equation. Use the Danckwerts boundary condition for inflow and
    Neumann boundary condition at outflow. Implement the dispersive term
    implicitly. For the convective term you can either choose implicit,
    explicit, upwind with or without TVD.

c)  Investigate the accumulative residence time distribution produced by
    this model using the written routine. That is, supply a
    concentration step at the input and measure the fluxes that leave
    the reactor. Plot the flux that leaves the reactor as function of
    time, properly normalized such that you get the accumulative
    residence time distribution, $F(t)$.

The analytical solution, for not too large axial dispersion, is given by

$$F(t) = \frac{1}{2}\ {erfc}\left( \frac{L - v\ t}{2\sqrt{D_{ax}t}} \right)$$

For very large axial diffusion, $D_{ax} \rightarrow \infty$, the
behavior should be CISTR and you have

$$F(t) = 1 - \exp\left( - \frac{v\ t}{L} \right)$$

Compare numerical results with the analytical solution. Investigate both
physical and numerical aspects (i.e. time step and grid size
dependencies).

d)  Model a system with a moving and stagnant phase that exchange mass.
    In the moving phase both convection and dispersion takes place. One
    could think of a trickle bed where liquid trickles down, but some
    liquid close to the packing is stagnant due to capillary forces.
    Investigate the effect on the residence time distribution due to
    mass transfer to and from the stagnant liquid.

e)  Use the routine to determine the residence time distribution in the
    next exercise, and for other multiphase models.
