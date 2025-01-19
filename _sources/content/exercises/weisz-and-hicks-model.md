# Weisz and Hicks model

This exercise considers diffusion and reaction in a spherical particle
for first order kinetics. The reaction rate, however, is temperature
dependent via a Arrhenius dependence.

$${\frac{\partial c}{\partial t} = \frac{1}{r^{2}}\frac{\partial}{\partial r}\left( r^{2}D_{e}\frac{\partial c}{\partial r} \right) + r = div\left( D_{e}\ grad(c) \right) + r,\ \ with\ r = - k_{0}\exp\left\lbrack \frac{E_{a}}{R_{G}}\left( \frac{1}{T_{f}} - \frac{1}{T} \right) \right\rbrack c
}{\rho C_{p}\frac{\partial T}{\partial t} = \frac{1}{r^{2}}\frac{\partial}{\partial r}\left( r^{2}\lambda_{S}\frac{\partial T}{\partial r} \right) + r\ \Delta H_{r} = div\left( \lambda_{S}\ grad(T) \right) + r\ \Delta H_{r}}$$

Assume Dirichlet boundary conditions for both concentration and
temperature on the particle surface.

**Questions**:

a)  Formulate the model in a dimensionless way by introduction of
    characteristic numbers $\varphi$, $\beta$ and $\gamma$, Thiele
    modulus: $\varphi = R\sqrt{\frac{k_{0}}{D_{e}}}$,
    $\beta = \frac{c_{f}\left( - \Delta H_{r} \right)D_{e}}{T_{f}\lambda_{S}}$
    (ratio heat generation/transport) and
    $\gamma = \frac{E}{R_{G}T_{f}}$ (ratio activation/thermal energy).

b)  Provide a Euler-backward Python implementation of both the diffusion
    and temperature equations.

c)  Can you reproduce the case of effectiveness, $\eta > 1$ for a
    specific choice of $\beta$, $\gamma$ and $\ \phi$?

![Graphs-MRT-sheet-28](./media/image1.png){width="5.105492125984252in"
height="3.359529746281715in"}

Source: Chem. Engin. Sc., 1962, Vol. 17, pp. 265-275

Hint: Use a small enough time step to avoid stability issues. Based on
the profiles you find, explain what causes the efficiency to be larger
than 1?
