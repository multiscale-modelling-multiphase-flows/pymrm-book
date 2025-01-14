# Taylor Dispersion

Taylor dispersion is caused by the presence of a velocity profile.
Solute particles experience different flow velocities depending on their
(radial) position. By means of molecular diffusion the particles sample
these different velocity, which gives a spread in residence time.

The spread of the solute can be described by a 2D convection-diffusion
equation:

$$\frac{\partial c}{\partial t} + div\left( \mathbf{v}c - D_{m}\ grad(c) \right) = 0$$

In a tube with laminar (Poiseuille) flow the velocity profile is

$$v_{z}(r) = 2\overline{v}\ \left( 1 - \frac{r^{2}}{R^{2}} \right)$$

**Questions**:

a)  Implement the 2D time-dependent convection-diffusion equations for a
    cylinder with developed Poiseuille flow.

b)  Obtain the molar flow leaving the reactor as function of time and
    construct a cumulative residence time distribution (RTD from that.

c)  Critically compare the RTD with results of the 1D models in exercise
    4.5
