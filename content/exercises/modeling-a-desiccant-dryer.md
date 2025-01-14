# Modeling a desiccant dryer

A typical rotating drum desiccant dryer consists of air channels coated
by desiccant material. The drum rotates through different air streams in
order to dry a process stream and next be regenerated.

The flow of a (humid) gas and simultaneously adsorption of water through
a channel can be described by transport equations for mass and heat.

This process can be described by a homogeneous model, where mass and
heat transfer resistances between the gas and adsorbent are neglected.
Here there is one PDE for humidity in both phases, and also one PDE for
temperature:

$${\frac{\partial}{\partial t}\left( \varepsilon\ \rho_{g}w_{g} + (1 - \varepsilon)\ f_{ds}\ \rho_{s}W_{ds} \right) + \frac{\partial}{\partial x}\left( v\ \rho_{g}\ w_{g} \right) = 0
}{\frac{\partial}{\partial t}\left( \left\lbrack \varepsilon\ \rho_{g}C_{p,g} + (1 - \varepsilon)\ \rho_{s}C_{p,s} \right\rbrack\ T - (1 - \varepsilon)\ f_{ds}\ \rho_{s}W_{ds}\ H_{sor} \right) + \frac{\partial}{\partial x}\left( v\ \rho_{g}C_{p,g}T \right) = 0}$$

In these equations $w_{g}$ is the weight fraction of water in the air
stream and $W_{ds}$ the weight of adsorbed water per kg desiccant (a
fraction $f_{ds}$ is used because there is also some inert solid
material). The first equation expresses a mass balance where the
accumulation of water both in air and desiccant is balanced by the
transport of water by the air stream. The superficial gas velocity is
$v = 1.5\ \frac{m}{s}$. The length of a channel is $L = 0.2\ m$.

In the enthalpy balance the accumulation term has two contribution, one
due to heat capacity and next one due to the (lower) enthalpy of
adsorbed water. Here $H_{sor}$ is the enthalpy of sorption. This will
cause heat to be created when water is adsorbed. Enthalpy is transported
along the channel by the gas flow.

The material properties are:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Material    Densities                                                                       Heat capac.                                                           Volume fractions
              $\mathbf{\lbrack}\frac{\mathbf{kg}}{\mathbf{m}^{\mathbf{3}}}\mathbf{\rbrack}$   $\mathbf{\lbrack}\frac{\mathbf{J}}{\mathbf{kg\ K}}\mathbf{\rbrack}$   
  ----------- ------------------------------------------------------------------------------- --------------------------------------------------------------------- ------------------------
  Air         $$\rho_{g} = 1.2$$                                                              $$C_{p,g} = 1872$$                                                    $$\varepsilon = 0.8$$

  Adsorbent   $\rho_{s} = 930$                                                                $$C_{p,s} = 1340$$                                                    $$f_{ds} = 0.8$$
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Locally the water in the air stream is assumed to be in equilibrium with
the adsorbed amount of gas. The amount of adsorbed water is related to
the relative humidity $\phi_{w}$ is described by the following
adsorption isotherm: $W_{ds} = 0.30\ \phi_{w}^{0.75}$, with
$\phi_{w} = \frac{p}{p_{sat}}\frac{w_{g}}{0.64 + 0.36w_{g}}\ $and
$p_{sat} = \exp\left( 23.20 - \frac{3816}{(T - 46.13)} \right)$, with K
the unit of temperature and Pa the unit of pressure. $p_{sat}$ is the
saturation pressure of water at the temperature $T$ and $p$ the total
pressure in the channel. In our case $p = 1\ bar$. The heat of sorption
per kilogram desiccant is

$$H_{sor}\left\lbrack \frac{kJ}{kg} \right\rbrack = \left\{ \begin{matrix}
2850 - 13.4 \cdot 10^{3}\ (W - 0.05), & W \leq 0.05 \\
2850 - 1.40 \cdot 10^{3}\ (W - 0.05), & W > 0.05
\end{matrix} \right.\ $$

**Questions**:

a)  Implement the model for water weight fraction in air, $w_{g}$ and
    temperature, $T$ as function of position $x$ and time $t$. Suggested
    approach:

    a.  Use a coupled formulation where you solve $w_{g}$ and $T$
        simultaneously as component 0 and 1 of a NumPy array.

    b.  Evaluate the convection term explicitly using first order upwind
        (that can be extended later to e.g. min-mod).

    c.  The non-linear accumulation term can be treated using
        Newton-Raphson (using newton from the pymrm package). Compute
        the Jacobian of the accumulation term numerically (using
        numjac_local).

b)  Model adsorption of a humid stream with $w_{g,\ in} = 0.015$ and
    $T_{in} = 307.7\ K$.

c)  Advanced (optional): Simulate, up to cyclic stationary state, of
    drying and regeneration, as if a drum is rotating through both
    theses streams. For the regeneration stage the stream enters form
    the other side. Both stages take 90 seconds, with the inlet
    conditions of the humid stream: $w_{g,\ in} = 0.015$ and
    $T_{in} = 307.7\ K$ and the regeneration air stream:
    $w_{g,\ in} = 0.018$ and $T_{in} = 393.2\ K$.
