# Counter-current column processes

Many (separation) processes, such as absorption, stripping and
extraction are often operated in counter-current mode. In this exercise
we consider a simple stationary two phase coun0ter-current process for
one component with linear driving forces for mass transfer:\
$${div\left( U_{g}c_{g} \right) = k_{ov}a\left( c_{l} - \frac{c_{g}}{m} \right),\ \ with\ sgn\left( U_{g} \right) > 0
}{div\left( U_{l}c_{l} \right) = - k_{ov}a\left( c_{l} - \frac{c_{g}}{m} \right),\ \ with\ sgn\left( U_{l} \right) < 0
}$$with boundary conditions: $c_{g}(0) = c_{g,in}$,
$c_{l}(L) = c_{l,in}$

Here $U_{l}$ and $U_{g}$ are superficial velocities, $k_{ov}a$ an
overall mass-transfer coefficient and $a$ the specific surface area of
the interface between the phases $g$ and $l$. The coefficient $m$ is a
distribution coefficient. At phase equilibrium
$\frac{c_{g}}{c_{l}} = m$. The driving force of mass transfer is
non-zero when there is a deviation from this equilibrium.

**Questions**:

a)  Make a Python implementation of the model.

b)  **Advanced**: Find the analytical solution of the model. Verify the
    implementation with the analytical solution.

c)  This model can serve as a basis for more advanced modelling of
    counter-current processes. Consider the implementation of a
    multicomponent system with a non-linear equilibrium relation between
    the components in the two phases.
