# A 2D Bubble column model

In a bubble column the gas hold up is larger in the middle. In rising
bubbles induce a circulation pattern, dragging along the liquid in the
middle, which circulates downward at the wall. We will model this by
using radial profiles of hold-up and velocities. In most of the column
these profiles are constant along the height. However, at the bottom and
top of the column the flow will also be radially directed. These end
zones will be modeled as ideally mixed, such as indicated in the figure
below.

  ----------------------------------------------------------------------------------------------------
  ![A graph of a function Description automatically            ![](./media/image7.emf){width="1.9in"
  generated](./media/image6.png){width="2.058333333333333in"   height="1.862678258967629in"}
  height="5.4628915135608045in"}                               
  ------------------------------------------------------------ ---------------------------------------
                                                               ![](./media/image8.emf){width="1.9in"
                                                               height="1.8669553805774277in"}

                                                               ![](./media/image9.emf){width="1.9in"
                                                               height="1.87625in"}

  Model for a bubble column. For most of the length of the     
  column the flow is purely axial. Radial flow is modeled in   
  an effective way by means ideal mixers in the end-zones.     
  ----------------------------------------------------------------------------------------------------

The profiles plotted on the right are measured by means of radioactive
particle tracking and taken from Degaleesan et al. (*Ind. Eng. Chem.
Res.* **1997**, *36*, 4670-4680). The column diameter is $19\ cm$ and
the height$\ 190\ cm$. The flow is in the churn turbulent regime.

From the experimental data plotted in the graphs above we approximate:

$${\varepsilon_{G}(r) = 0.25 - 0.18\ \frac{r}{R},\ \ \varepsilon_{L} = 1 - \varepsilon_{G},
}{v_{L}(r) = v_{L,0}\left( 1 - \frac{r}{0.7\ R} \right)
}{D_{ax} = 200\frac{cm^{2}}{s} + \left( 300\frac{cm^{2}}{s} \right)\ \frac{r}{R}
}{D_{rad} = 40\ \frac{cm^{2}}{s}}$$

We assume that there is difference $\Delta v_{GL}$ between the
gas-velocity and liquid velocity independent of $y$, such that

$$v_{G}(r) = v(r) + \Delta v_{GL}.$$

The superficial velocity of the liquid equals $U_{L} = 1\frac{cm}{s}$
and of the gas: $U_{G} = 10\ \frac{cm}{s}$.

The total height of 190 cm will be divided in 3 parts: a bottom section
of 19 cm, a middle section of 152 cm and a top section of 19 cm. The
middle section is modeled by means of convection-diffusion reaction
equation

$${\frac{\partial}{\partial t}\left( \varepsilon_{L}c_{L} \right) + \frac{\partial}{\partial x}\left( \varepsilon_{L}v_{L}c_{L} - \varepsilon_{L}D_{ax}\frac{\partial c_{L}}{\partial x} \right) - \frac{1}{r}\frac{\partial}{\partial r}\left( r\left\lbrack \varepsilon_{L}D_{rad}\frac{\partial c_{L}}{\partial y} \right\rbrack \right) = k_{L}a\left( c_{L}^{*} - c_{L} \right) + \varepsilon_{L}R_{L}
}{\frac{\partial}{\partial t}\left( \varepsilon_{G}c_{G} \right) + \frac{\partial}{\partial x}\left( \varepsilon_{G}v_{G}c_{G} - \varepsilon_{G}D_{ax}\frac{\partial c_{G}}{\partial x} \right) - \frac{1}{r}\frac{\partial}{\partial r}\left( r\left\lbrack \varepsilon_{G}D_{rad}\frac{\partial c_{G}}{\partial y} \right\rbrack \right) = {- k}_{L}a\left( c_{L}^{*} - c_{L} \right) + \varepsilon_{G}R_{G}}$$

Note that we take the turbulent diffusion coefficient of both liquid and
gas are taken to be identical. The reason is that (small) bubbles will
be dragged along with the liquid.

The top and bottom sections are modeled as ideally mixed. It is advised
to model this by using artificially large axial and radial turbulent
diffusion coefficients $D_{ax}$ and $D_{rad}$ in these sections. Also
make sure that the inflow in the bottom section is actually inflow
(i.e., has no negative velocities) and that at the top there is only
outflow.

**Questions:**

a)  Compute the average hold-ups and determine the values of $v_{L,0}$
    and $\Delta v_{GL}$ such that the prescribed superficial velocities
    are obeyed.

b)  Implement the formulated model equations in Python for the case of
    insoluble species ($k_{L}a = 0$).

c)  Model a first order reaction in the liquid phase. Hint: Because you
    consider first-order kinetics the result will be independent of the
    inlet concentration. A simple choice is
    $c_{L,in} = 1\ \frac{mol}{m^{3}}( = 10^{- 6}\ \frac{mol}{{cm}^{3}})$.
    How do the results for a range of kinetic coefficients compare to
    the conversion in an ideal CSTR and in a plug flow reactor?

d)  Model a first order reaction in the gas phase (for a range of
    kinetic coefficients). How does it compare to the conversion in an
    ideal CSTR and in a plug flow reactor?

e)  Play with the model. Implement a realistic value of $k_{L}a$, a
    proper equilibrium relation between gas and liquid concentrations
    (i.e. $c_{L}^{*}\left( c_{G} \right)$) and interesting kinetics.
