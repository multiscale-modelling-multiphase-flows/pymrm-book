# Reactor model for heterogeneous bubble columns

In this exercise you are asked to model the mass-transfer in a slurry
bubble column as proposed by Maretto and Krishna, Catalysis Today 52
(1999) 279-289. In this model the column is described by three phases,
two bubble phases, namely, a large and small bubble phase, and a slurry
phase. Large bubbles transport gas in a plug flow fashion, and small
bubbles have a more turbulent flow pattern that is described in the
model as well-mixed. From the bubble phases, gas can dissolve in the
slurry phase. This is liquid with suspended particles. Catalytic
conversion take place in the particles.

![](./media/image2.emf){width="3.4330708661417324in"
height="3.7401574803149606in"}Here we consider the balances of the
phases, where subscript $b$ labels the large bubbles, *df*, the small
bubbles and *s* the slurry:

$$\varepsilon_{b}\ \frac{\partial c_{b,i}}{\partial t} + \frac{\partial}{\partial z}\left( U_{b}\ c_{b,i} - \varepsilon_{b}E_{b}\frac{\partial c_{b,i}}{\partial z} \right) = - \left( k_{l}a \right)_{b,i}\left( \frac{c_{b,i}}{m_{i}} - c_{sl,i} \right)$$

$$\left( 1 - \varepsilon_{b} \right)\varepsilon_{df}\ \frac{\partial c_{df,i}}{\partial t} + \frac{\partial}{\partial z}\left( U_{df}\ c_{df,i} - \left( 1 - \varepsilon_{b} \right)\varepsilon_{df}\ E_{df}\frac{\partial c_{df,i}}{\partial z} \right) = - \left( k_{l}a \right)_{df,i}\left( \frac{c_{df,i}}{m_{i}} - c_{sl,i} \right)$$

$$\left( 1 - \varepsilon_{b} \right)\left( 1 - \varepsilon_{df} \right)\ \frac{\partial c_{sl,i}}{\partial t} + \frac{\partial}{\partial z}\left( - \left( 1 - \varepsilon_{b} \right)\left( 1 - \varepsilon_{df} \right)E_{s}\frac{\partial c_{sl,i}}{\partial z} \right) = {\left( k_{l}a \right)_{b,i}\left( \frac{c_{b,i}}{m_{i}} - c_{sl,i} \right) + \left( k_{l}a \right)}_{df,i}\left( \frac{c_{df,i}}{m_{i}} - c_{sl,i} \right) + \left( 1 - \varepsilon_{b} \right)\left( 1 - \varepsilon_{df} \right)\varepsilon_{s}\ r_{i}$$

Although only the steady state is of interest, solving the equations
time-dependently might help to find this steady state. Similarly, the
dispersion coefficient are numerical parameters, since we are interested
in limit values. The bubble phase is modelled as plug-flow, so
$E_{b} = 0$. For the small-bubble and slurry phases a well-mixed state
is assumed. This can be achieved by choosing $E_{df}$ and $E_{s}$ large.
They should be large enough to have almost no axial profiles for these
phases. Note that, there might arise numerical problems when values are
chosen very large. The optimal choice can best be determined by a
trial-and-error procedure.

In the work of Maretto and Krishna the Fischer-Tropsch reaction is
considered, where CO and $H_{2}$ are aided by the catalyst particles in
the slurry to form hydrocarbons. Hold-ups, superficial velocities and
mass transfer coefficients follow from correlations. Here we are mostly
interested as an exercise to implement the model and investigate its
behavior depending on where the main resistance to mass transfer lies.

**Questions**:

a)  Implement the slurry bubble column model for one inert tracer
    species.

  -----------------------------------------------------------------------------------------------------------------------------------------------
  Quantity                              Large bubble                          Small bubble                           Slurry
  ------------------------------------- ------------------------------------- -------------------------------------- ----------------------------
  Holdup                                $$\varepsilon_{b} = 0.096$$           $$\varepsilon_{df} = 0.135$$           $$\varepsilon_{s} = 0.30$$

  Superficial velocity                  $$U_{b} = 0.255$$                     $$U_{df} = 0.045$$                     0
  \[$\frac{\mathbf{m}}{\mathbf{s}}$\]                                                                                

  Mass transfer coeff.,                 $$\left( k_{l}a \right)_{b} = 0.2$$   $$\left( k_{l}a \right)_{df} = 1.2$$   \-
  \[$\mathbf{s}^{\mathbf{- 1}}$\]                                                                                    
  -----------------------------------------------------------------------------------------------------------------------------------------------

b)  Determine the cumulative residence distribution for a tracer species
    introduced in the gas phase. Assume values:

For the distribution coefficient take $m = 3$. Vary the height of the
column (up to 30m)

c)  Assume that the species is reactive and undergoes a first order
    reaction at the catalyst particle. Perform a parameter study for the
    reaction rate coefficient $k$ of the first order reaction.
