# A 2D Gas-solid fluidized bed

In a gas-fluidized bed (with diameter $D = 2.0\ m$ and expanded bed
height $L = 3.0\ m$) heterogeneously catalyzed chemical reactions take
place involving the species A, B and C. The reaction scheme and
associated kinetics are as follows:

$$A\overset{K_{r,1}}{\rightarrow}B\overset{K_{r,2}}{\rightarrow}C,\ \ r_{A} = {- K}_{r,1}c_{A},\ \ r_{B} = K_{r,1}c_{A} - K_{r,2}c_{B},\ \ r_{C} = K_{r,2}c_{B}$$

The catalyst material consists of Geldart A type particles with a
particle size of 50 μm and a particle density of 1500 kg/m^3^.
Additional data are given in Table 1. In the extended Kunii and
Levenspiel fine-particle-model the radial gas (bubble) velocity profile
is taken into account as well as the radial gas dispersion. For the
radial profile of the bubble rise velocity we assume a parabolic profile
given by:

$$U_{0}(r) = 2\ \left\langle U_{0} \right\rangle\ \left\lbrack 1 - \left( \frac{r}{R} \right)^{2} \right\rbrack$$

where $\left\langle U_{0} \right\rangle$ is the average bubble rise
velocity. This expression approximately accounts for the fact that the
preferential pathway of the bubbles is located in the central part of
the gas-fluidized bed. Due to the relatively high value of the average
superficial gas velocity the axial gas dispersion can be neglected.
Moreover, it can be assumed that the reactor is isothermal. The
bubble-to-cloud mass transfer coefficients $K_{bc}$ and the
cloud-to-emulsion mass transfer coefficients $K_{ce}$ can be taken the
same for the components A, B and C (see Table 1).

**Table 1: Additional data**

\- Average bubble rise velocity \<U~0~\> : 0.50 m/s

\- Reaction rate constant K~r,1~ : 0.080 s^-1^

\- Reaction rate constant K~r,2~ : 0.010 s^-1^

\- Bubble-to-could mass transfer coefficient K~bc~ : 2.5 s^-1^

\- Cloud-to-emulsion mass transfer coefficient K~ce~ : 1.5 s^-1^

\- Radial gas dispersion coefficient D~i,r~ (i=A, B and C) : 0.01
m^2^.s^-1^

\- Bubble phase solids holdup parameter γ~b~ : 0.005 (-)

\- Cloud phase solids holdup parameter γ~c~ : 0.200 (-)

\- Emulsion phase solids holdup parameter γ~e~ : 5.000 (-)

\- Inlet concentration species A: : 5.0 mole/m^3^

\- Inlet concentration species B: : 0.0 mole/m^3^

\- Inlet concentration species C: : 0.0 mole/m^3^

**Questions**:

a)  Formulate the steady state model equations and the associated
    boundary conditions according to the extended Kunii and Levenspiel
    Fine Particle Model taking into account the radial profile of bubble
    rise velocity and the radial gas dispersion.

b)  Implement the formulated model equations in Python.

c)  Compute the steady state concentration profiles at the outlet of the
    gas-fluidized bed using the implemented Python model. Inspect the
    computed concentration profiles carefully and explain the
    qualitative shape of these profiles. Use 100 radial grid points and
    200 axial grid points.

d)  Compute the degree of chemical conversion of species A and the
    selectivity towards the desired product B. Carefully account for the
    radial gas (bubble) velocity profiles which exist.

e)  Consider the case where the bubble rise velocity is uniform and
    radial gas dispersion can be neglected (assuming uniform inlet
    conditions). Solve the resulting Ordinary Differential Equations
    (ODE's) and compute the degree of chemical conversion of species A
    and the selectivity towards the desired product B.
