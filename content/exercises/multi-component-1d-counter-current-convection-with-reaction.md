# Multi-component 1D counter-current convection with reaction

Consider the reaction kinetics and boundary conditions as in exercise
3.2 but now with counter-current convection instead of diffusion. Assume
that reactant A and product C move from left to right, and reactant B
and product D from right to left. One can imagine counter-current liquid
and gas flows where some of the components are liquid and others gas.
This is modeling a counter-current process where any mass-transfer
resistance are neglected.

$${\frac{\partial c_{A}}{\partial t} + div\left( v\ c_{A} \right) = - r,\ with\ r = - k_{1}c_{A}c_{B} + k_{2}c_{C}c_{D}
}{\frac{\partial c_{B}}{\partial t} - div\left( v\ c_{B} \right) = - r
}{\frac{\partial c_{C}}{\partial t} + div\left( v\ c_{C} \right) = r,
}{\frac{\partial c_{D}}{\partial t} - div\left( v\ c_{D} \right) = r\ }$$

$c_{A}(0) = 10\frac{kmol}{m3},\ c_{B}(L) = 10\frac{kmol}{m3},\ c_{C}(0) = 0\frac{kmol}{m3},\ c_{D}(L) = 0\frac{kmol}{m3}$

  --------------------------------------------------- --------------------------
  Reactor length $L$                                  1.0 m

  Kinetic constant $k_{1}$                            1.0 m^3^/(kmol s)

  Kinetic constant $k_{2}$                            0 m^3^/(kmol s)

  Velocities                                          $$\pm 1.0\ \frac{m}{s}$$
  --------------------------------------------------- --------------------------

**Questions**:

a)  Write down the governing time-dependent evolution equations.

b)  Write down the spatially discretized equations in terms of matrices
    corresponding to the discretization of the divergence and gradient
    operator. Discuss, how the boundary conditions contribute to the
    discretized equations.

c)  Use backwards Euler time discretization for all terms. Write down
    the root-seeking problem that needs to be solved. Also provide the
    Jacobian of the function that needs to be solved.

d)  Formulate the solution algorithm applying the Newton-Raphson method.

e)  Provide a Python implementation for the set of equations and its
    Jacobian using the pymrm building blocks: construct_grad,
    construct_div and numjac_local.

f)  Implement the numerical solution using the newton function from the
    py_mrm package.

g)  Provide the an unsteady solution using Newton-Raphson iteration for
    each time-step.

h)  Play with the reaction rates and boundary conditions. For higher
    reaction rates, when do numerical issues arise? How can these be
    resolved. Hint: the pymrm function clip_approach can be used as a
    callback function in newton, to make sure that values stay within
    bounds also inside iterations.
