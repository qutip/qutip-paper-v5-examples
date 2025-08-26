
import jax
import jax.numpy as jnp
import qutip
import qutip_jax

# Set JAX backend for QuTiP
qutip_jax.set_as_default()

# Define time-dependent driving function
@jax.jit
def driving_coeff(t, omega):
    return jnp.cos(omega * t)

# Define the system Hamiltonian
def setup_system(omega):
    H_0 = qutip.sigmaz() 
    H_1 = qutip.sigmax() 
    H = [H_0, [H_1, driving_coeff]] 
    return H

gamma = 0.1  # Dissipation rate
c_ops = [jnp.sqrt(gamma) * qutip.sigmam()]
psi0 = qutip.basis(2, 0) 

tlist = jnp.linspace(0.0, 10.0, 100)

e_ops = [qutip.projection(2, 1, 1)]

# Objective function: simulate and return the population of the excited state at final time
def f(omega):
    H = setup_system(omega)
    result = qutip.mcsolve(H, psi0, tlist, c_ops, e_ops, ntraj=100, args = {"omega": omega})
    return result.expect[0][-1]  

# Compute gradient of the excited-state population w.r.t. omega
grad_f = jax.grad(f)(2.0)
print(grad_f)
