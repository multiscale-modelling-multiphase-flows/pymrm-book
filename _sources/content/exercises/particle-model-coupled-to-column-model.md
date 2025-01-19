# Particle model coupled to column model

Consider both a batch model and particle model. Inside a particle a
diffusion-reaction equation is solved in a spherical symmetric geometry:

$$\frac{\partial c_{s}}{\partial t} = \frac{1}{r^{2}}\frac{\partial}{\partial r}\left( r^{2}D\ \frac{\partial c_{s}}{\partial r} \right) + react = {div}_{r}\left( D{\ grad}_{r}\left( c_{s} \right) \right) + react$$

with boundary condition

$$- D\left. \ \frac{\partial c_{s}}{\partial r} \right|_{R} = k_{m}\left( c_{s}(R) - c_{f} \right)$$

This modeled is coupled to a balance of a column:

$${\frac{\partial\varepsilon_{b}c_{f}}{\partial t} + \frac{\partial Uc_{f}}{\partial z} - \frac{\partial}{\partial z}\left( D_{ax}\frac{\partial c_{f}}{\partial z} \right) = {\ r}_{app}^{}
}{\frac{\partial\varepsilon_{b}c_{f}}{\partial t} + {div}_{z}\left( U\ c_{f} - D_{ax}\ {grad}_{z}\left( c_{f} \right) \right) = {\ r}_{app}^{}}$$

Where the apparent reaction rate can be obtained from the particle model
as

$$r_{}^{app}(x) = - a\ D\left. \ \frac{\partial c_{s}}{\partial r} \right|_{R},\ with\ a = \frac{3\left( 1 - \varepsilon_{b} \right)}{R}$$

**Questions**:

a)  Make separate implementations for the particle and reactor model.

b)  Verify both implementations. (Think of good critical test cases).

c)  Combine the two models such that the particle model can provide the
    apparent reaction rate for the batch reactor. Use an explicit
    coupling where, within a time step, you call the models
    sequentially.

d)  Verify the explicit coupling.

e)  Provide a implicitly coupled implementation using a 'Schur
    compliment' strategy.

f)  Verify the implicit coupling.
