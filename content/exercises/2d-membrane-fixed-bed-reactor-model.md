# 2D Membrane Fixed Bed Reactor Model

In a (single tube) membrane fixed bed reactor a heterogeneously
catalyzed chemical equilibrium reaction is carried out. The reaction
scheme and associated kinetics are as follows:

$$A + B \rightleftarrows C + D,\ with\ \ $$

The tube wall of the fixed bed consists of a perm-selective membrane
through which component $C$ selectively permeates. The associated flux
expression is given by the following equation:

$$N_{C} = k_{m}\left\lbrack \left. \ c \right|_{r = R} - c_{0} \right\rbrack$$

where $k_{m}$ represents the effective mass transfer coefficient for the
intra-membrane transport and $c_{0}$ the concentration of component $C$
in the sweep gas in the annular zone (see figure below). The
concentration of species $C$ in the sweep gas $c_{0}$ can be assumed
equal to zero, corresponding to assuming a very large sweep gas flow
rate.

![D:\\Users\\eajfpeters\\Documents\\Teaching\\MRM\\MRM
2016\\Tutorials\\fixed_bed.emf](./media/image5.emf){width="4.930555555555555in"
height="2.2041666666666666in"}The effective radial dispersion
coefficient D~e,r~ of all species $A$, $B$, $C$ and $D$ amounts
$10^{- 4\ }m^{2}/s$. The inlet concentration of species $A$ and $B$
equal 10.0 mol/m^3^, whereas the inlet concentration of species $C$ and
$D$ are 0.0 mol/m^3^. In the membrane fixed bed reactor isothermal
conditions prevail.

  --------------------------------------------------- -------------------
  Superficial gas velocity, $U_{0}$                   0.2 m/s

  Inner radius fixed bed tube                         0.02 m

  Length fixed bed tube                               1.00 m

  Kinetic constant k~f~                               0.1 m^3^/(mol.s)

  Kinetic constant k~b~                               0.1 m^3^/(mol.s)
  --------------------------------------------------- -------------------

**Questions**:

a)  Calculate the thermodynamic equilibrium conversion.

b)  Formulate the model equations and the associated boundary conditions
    according to the homogeneous two-dimensional reactor model. Account
    in your model for the selective permeation of component $C$ through
    the membrane. Neglect axial dispersion effects.

c)  Implement the formulated model equations in Python. It is suggested
    to use a methods-of-line approach where the spatial discretization
    is performed in the radial direction and the axial dependence is
    solved using solve_ivp.

d)  For the case of no permeation of $C$ ($k_{m} = 0\ .0\frac{m}{s}$)
    calculate the chemical conversion.

e)  Repeat the calculation for part 4 of this problem using $k_{m}$
    values of 0.01, 0.1, 1.0, 10.0 and 100.0 m/s for the effective mass
    transfer coefficient. Explain the observed differences with respect
    to the chemical conversion and the obtained radial concentration
    profiles. Discuss the validity of the model equations for k~m~ = 100
    m/s.

f)  Repeat part 5 of this problem using an effective radial dispersion
    coefficient $D_{e,r}$ of $10^{- 5}\ m^{2}/s$. Discuss the observed
    results.
