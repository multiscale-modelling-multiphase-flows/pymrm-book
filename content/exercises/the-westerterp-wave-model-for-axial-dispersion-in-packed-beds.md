# The Westerterp wave-model for axial dispersion in packed beds

Flow profiles in a tube, combined with diffusion in the radial direction
can cause dispersion of a solute. The reason is that solute particles
experience different flow velocities depending on their radial position
within the tube. Particles near the center move faster, while those near
the walls move slower. This difference in velocity causes the solute to
spread along the length of the tube. This phenomenon is called Taylor
dispersion. This is explicitly modeled in exercise 5.7.

In 1D models of a tubular reactor, this dispersion is often
mathematically modelled as a diffusive term. This axial dispersion
coefficient for a parabolic velocity profile is:

$$D_{ax} = D + \frac{v^{2}R^{2}}{48\ D},$$

with $D$ the molecular diffusion coefficient, $v$ the average velocity
in the tube and $R$ its radius.

Modelling dispersion using a diffusion term has been criticized. An
alternative approach was proposed by Westerterp et al., AIChE Journal 41
(1995) 2013--2028. In this approach Taylor dispersion can be modeled in
a 1D model as two phases that have different velocities and mass
transfer in between:

$${\varepsilon_{1}\frac{\partial c_{1}}{\partial t} + \varepsilon_{1}v_{1}\frac{\partial c_{1}}{\partial z} - \varepsilon_{1}D\frac{\partial^{2}c_{1}}{\partial z^{2}} = \frac{1}{\tau}\ \left( c_{2} - c_{1} \right)
}{\varepsilon_{2}\frac{\partial c_{2}}{\partial t} + \varepsilon_{2}v_{2}\frac{\partial c_{2}}{\partial z} - \varepsilon_{2}D\frac{\partial^{2}c_{2}}{\partial z^{2}} = - \frac{1}{\tau}\ \left( c_{2} - c_{1} \right),\ \ with}$$

$$\varepsilon_{1} = \text{0.37493},\ \varepsilon_{2} = \text{0.6250}\text{7},\ v_{1} = \text{1.83395}\ v,v_{2} = \text{0.4997}\text{8}\ v,\ \tau = \text{0.213}\text{10}\frac{R^{2}}{D}$$

**Questions**:

a)  Implement a 1D diffusion-convection model, where the diffusion term
    models Taylor dispersion.

b)  Implement the two-phases model of Taylor dispersion.

c)  Determine the residence time distributions for the two models for a
    range of dimensionless Péclet numbers, $Pe = \frac{vR}{D}$ and
    aspect ratios $\frac{L}{R}$.
