# Mass transfer limitations using Maxwell-Stefan equations

We consider the same exothermal catalytic fixed bed 1D column process as
in previous exercise 1.3. In this exercise you will investigate the
influence of external mass transfer limitations.

In a fixed bed catalyst tube of length $L = 0.5\ m$ the following
exothermal reaction takes place in catalytic particles

$$A \rightarrow B + C,\ \ \ \ \ \ \ r = k_{r}\ c_{A},\ \ with\ k_{r} = k_{0}\exp\left\lbrack - \frac{E_{a}}{RT} \right\rbrack,\ \ {- r}_{A} = r_{B} = r_{C} = r
$$where $k_{0} = 1.0\ 10^{9}\ s^{- 1}$, *E~a~*=50 kJ/mol. The reaction
is exothermic with $- \Delta H_{r} = 15\ kJ/mol$ at the reference
temperature of 293 K. The molar heat capacities of the gases equal 100,
60 and 40 J/(mol K), for $A$, $B$ and $C$, respectively. The reactor
operates adiabatically. The inlet gas stream consists of pure A and is
at a pressure of 1 bar and a temperature 293 K. The interstitial inlet
gas velocity $v$ equals 2.0 m/s.

In the earlier tutorials the effect of external mass transfer
limitations from the gas bulk to the active sites on the catalyst
surface were neglected, which allowed for a homogeneous reaction rate
source term if also intra-particle resistances are small. Now, let's
assume that the catalyst particles are spherical with a uniform diameter
of 3.0 mm (bed porosity of 0.4), and that the mass transfer coefficients
$k_{AB} = 0.005\ m/s$, $k_{BC} = k_{AC} = 0.020\ m/s$ are independent of
the operating conditions (simplification!).

**Remarks**

-   **In this tutorial we consider 3 species only, i.e., there is no
    fourth inert species. Note, that because the reaction is
    non-equimolar this would mean in practice that the superficial
    velocity increases along the reactor length. This effect is
    neglected in this exercise.**

-   **Note that there is a ambiguity in the different exercises on the
    exact definition of the reaction rate, i.e., is it per m^3^-reactor,
    solid or fluid? For the purpose if the current exercise make a
    convenient choice and make sure your equations are consistent with
    this choice. Make sure that when you evaluate the influence of mass
    transfer resistances you compare similar situations, i.e., with the
    same definitions of the reaction rate.**

**Questions**:

a)  Show with a simple estimation whether external mass transfer
    limitations could be important and should be included in the
    computations.

b)  Formulate the (simplified) equations to account for external mass
    transfer limitations using the Maxwell-Stefan approach. Make the
    assumption of linearization of the concentration profiles.

c)  Implement the formulated heterogeneous model to account for external
    mass transfer limitations using the linearized Maxwell-Stefan
    equations and calculate the axial profiles of the reactant
    concentration and bed temperature. Assume there are no internal mass
    transfer limitation.

> **Hint: For each species there are now two type of concentrations,
> namely the concentrations in the bulk of the fluid and the fluid
> concentrations at the particle surface. There are two approaches to
> introduce these surface concentrations:**

i.  **Only consider these in the reaction term of the column model and
    eliminate these from the set of equations, such that it returns the
    apparent reaction rate as function of the bulk fluid concentrations
    only.**

ii. **Extend the number of variables of unknowns in the column model
    with the surface concentrations. Solve the set of equations for the
    full set of variables simultaneously. The equations for the surface
    concentrations are algebraic.**

> **Choose one of the approaches and at the end of the exercise return
> and attempt the other one.**

d)  Verify that the profiles coincide with the results obtained with the
    homogeneous reaction rate expressions in case the mass transfer
    coefficients are increased a thousand fold. Compare the axial
    profiles of the reactant concentration with and without mass
    transfer limitations and explain the observed differences.

e)  Advanced: Formulate the equations to adequately account for external
    mass transfer limitations using the Maxwell-Stefan approach. Assume
    that the ideal gas law is valid and use the (exact) matrix method.

f)  Advanced: Implement the formulated heterogeneous model with the
    Maxwell-Stefan equations using the exact matrix method. Compare the
    results with the linearized solutions.

g)  Advanced (optional): Combine the (linearized) Maxwell-Stefan model
    with the particle-model implementation.
