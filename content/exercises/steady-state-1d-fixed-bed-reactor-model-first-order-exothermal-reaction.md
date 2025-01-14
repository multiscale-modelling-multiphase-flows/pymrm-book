# Steady state 1D fixed bed reactor model: first order exothermal reaction

In a fixed bed catalyst tube of 0.5 m long a heterogeneously catalyzed
exothermic (gas phase) chemical reaction takes place. The reaction
scheme and associated kinetics are as follows:

$$A \rightarrow B + C,\ \ \ \ \ \ \ r = k_{r}\ c_{A},\ \ with\ k_{r} = k_{0}\exp\left\lbrack - \frac{E_{a}}{RT} \right\rbrack,\ \ {- r}_{A} = r_{B} = r_{C} = r$$

where $k_{0} = 1.0 \times 10^{9}\ s^{- 1}$, *E~a~*=50 kJ/mol. The
reaction is exothermic with --∆H~r~=15 kJ/mol at the reference
temperature of 293 K. The molar heat capacities of the gases equal 100,
60 and 40 J/(mol K), for $A$, $B$ and $C$, respectively.

Here we will model the reactor as adiabatic. (Of course the reactor
should be cooled but this will be considered in a later tutorial). The
inlet gas stream consists of pure A and is at a pressure of 1 bar and a
temperature 293 K. The interstitial inlet gas velocity $v$ equals 2.0
m/s.

**Questions**:

a)  Formulate the stationary convection-reaction equations for species
    $A$, $B$ and $C$ as well as for the temperature assuming a constant
    gas velocity.

b)  Solve the set of ordinary differential equations assuming constant
    gas velocity using a standard Python IVP solver.

c)  Formulate the stationary convection-reaction equations for species
    $A$, $B$ and $C$ as well as for the temperature assuming a constant
    pressure throughout the reactor. Hint: be cautious about placing the
    velocity inside or outside of the spatial derivative.

d)  Solve this set of ordinary differential equations assuming constant
    pressure using a standard Python IVP solver.

e)  Are the results according to your expectations? Is the temperature
    increase consistent with the adiabatic temperature rise? Is the
    increase in velocity in accordance with expectations?

f)  Try solving both sets of ODE's using your own Euler backward solver.
