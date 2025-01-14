# Kunii and Levenspiel model for a 'fine particle' fluidized bed

In reactor models of fluidized beds we usually distinguish different
'phases', such as the emulsion phase and bubble phase. Depending on the
flow regime, there can be other phases, such as cloud and wake. To
construct the reactor model one needs to determine the balance equations
for concentrations in each phase, including mass exchange between
phases.

In this exercise we will only consider two phases, namely, emulsion and
bubble. The emulsion phase is a dense particle phase, where the voidage
remains close to the value at minimum fluidization conditions,
$\varepsilon_{mf}$. At gas velocities above the minimum fluidization
velocity, excess gas can create voids, that are referred to as bubbles.
For fluidized beds with fine particles (Geldart A), the emulsion phase
has a low permeability. This makes that excess gas mostly remains in the
bubbles, and that bubbles rise fast relative to the gas velocity in the
emulsion phase, $u_{b} > \frac{u_{mf}}{\varepsilon_{mf}}$.

In this exercise, you are asked to model a catalytic fluidized bed. The
particles are catalytically active, so conversion takes place in the
emulsion phase, while most gas is transported by the bubbles. The
balances for a concentration of gas species $i$ in the two phases $b$
and $e$ can be written as:

$${\delta\ \frac{\partial c_{b,i}}{\partial t} + \delta\ u_{b}\frac{\partial c_{b,i}}{\partial z} = - \delta\ K_{be}\left( c_{b,i} - c_{e,i} \right)
}{(1 - \delta)\ \frac{\partial c_{e,i}}{\partial t} + (1 - \delta)\ u_{e}\frac{\partial c_{e,i}}{\partial z} = \delta\ K_{be}\left( c_{b,i} - c_{e,i} \right) + (1 - \delta)\ r_{e,i}}$$

We assume that the bubble fraction and the velocities are constant over
the height. Note, that if this were not the case one should be really
careful about the placement inside or outside of the spatial derivative.
The parameter $\delta$ denotes the bubble hold-up. For a specified
overall superficial gas velocity, $u_{0}$, a total balance for the
volumetric flow rate gives:

$$u_{0} = \delta\ u_{b} + (1 - \delta)\ u_{e},$$

with $u_{b}$ and $u_{e}$ the bubble rise velocity and the superficial
gas velocity in the emulsion phase, respectively.

We have a reaction rate $r_{i}$ only in the emulsion phase. Note that
this is an apparent reaction rate that includes potential mass-transfer
resistances for transport between (emulsion) gas and particle. The case
considered is that of a first order reaction of one species,

$$r_{e} = - K_{r}\ c_{e}$$

In this type of model it is conventional to use volumetrically defined
mass-transfer coefficients, based on the bubble volume. This explains
the $\delta$ appearing in-front of $K_{be}$.

  -------------------------------------------------------------------------------------------------
  Quantity                                                        Value
  --------------------------------------------------------------- ---------------------------------
  $$\mathbf{d}_{\mathbf{b}}$$                                     $$0.04\ m$$

  $$\mathbf{K}_{\mathbf{be}}$$                                    $$1.2\ s^{- 1}$$

  $$\mathbf{K}_{\mathbf{r}}$$                                     $$10.0\ \ s^{- 1}$$

  $$\mathbf{u}_{\mathbf{0}}$$                                     $$0.1\ \frac{m}{s}$$

  $$\mathbf{u}_{\mathbf{e}}\mathbf{=}\mathbf{u}_{\mathbf{mf}}$$   $$0.006\ \frac{m}{s}$$
  -------------------------------------------------------------------------------------------------

In, the standard text of Kunii and Levenspiel, one can find many
correlations for transport coefficients. These are based on theoretical
consideration mixed with empirical findings. For example, for the bubble
rise velocity in a fine-particle fluidized bed, we have:

$$u_{b} = u_{0} - u_{mf} + u_{br},\ with\ u_{br} = 0.711\sqrt{g\ d_{b}},$$

where $d_{b}$ is the bubble diameter and $g$ the gravitational constant.
In the table we provide numerical values for other key quantities.

**Questions**:

a)  Using pymrm functions implement the model for a fine-particle
    fluidized bed.

b)  Compute the conversion as function of height.

c)  Investigate the influence of parameters, $k_{r}$, $u_{0}$, and
    $d_{b}$.

As an aside: For larger particles, Geldart B, the emulsion phase is more
permeable. Here excess gas uses the bubbles as a low-resistance shortcut
through the bed. Therefore, reactant gas tries to find a low resistance
path through emulsion and then through bubble etc. In this case the rise
velocity of bubbles is lower than that of the gas in the emulsion phase.
