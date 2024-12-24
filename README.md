# QuTiP 5 paper examples
A selection of examples released with the QuTiP 5 paper,  available on the ArXiV at https://arxiv.org/abs/2412.04705

These examples are provided in a unmaintained static format, alongside a environment requirements file for future reproducability. 
Continously maintained and documented versions of the main examples are available in the qutip tutorials repository.

Most examples here will work with the pinned versions in the environment.yml or requirements.txt file. 
However, we also provide some alternative versions of the examples using the environments class based on the latest release (5.1.0) or development version on github, in the
/environment_examples_dev/ folder, as well as an example of `mcsolve()` using JAX which requires the development versions of both QuTiP-JAX  and QuTiP.


If you use Anaconda, you can install the dependencies for this repository with

```shell
cd qutip-paper-v5-examples
conda env create --file environment.yml
conda activate qutip-paper
```

Alternatively, with `pip`

```shell
pip install -r requirements.txt
```

List of files and their purpose:

- enr_waveguide.py:  An example of how to use ENR states to simulate a qubit emitting into a waveguide. Reproduces figs 15 and 16.

- enrstates.py:  Basic example of ENR states.

- jax-countstats.py: An example of how to use QuTiP-JAX + JAX Auto-diff to calculate counting statistics from a master equation.

- jax-mesolve.py: Basic setup of an Ising spin chain model, used as a foundation for the GPU benchmark results in the QuTiP 5 paper in Fig 4.

- mcsolve.py: An example of how to QuTiP's Monte-Carlo quantum jump solver. Used to generate Fig. 5.

- mesolve.py: An example of how to use QuTiP's master equation, both directly and with globally-defined jump rates, and  a comparison to the Bloch-Redfield solver. Used to generate Fig. 2.

- mpl_setup.py: Utility file for consisten matlpotlib settings.

- nm_mcsolve_example.py: An example of how to use the non-Markovia Monte-Carlo solver (for a qubit coupled to a waveguide).  Used to generate Fig. 6.

- p_Floquet_speed_text.py: Benchmarking of Floquet states versus direct sesolve(). Used to generate Fig. 7.

- p_Ising_with_drive_Floquet.py: Benchmarking of Floquet states versus system size with the Ising model. Used to generate fig. 8.

- qip_renderer.py: Basic example of new QuTiP-QIP circuit plotting functionality. Used to generate fig. 18.

- qoc.py: Example of new optimal control methods from QuTiP-QOC. Used to generate Fig. 17.  Note, see this issue if using QuTiP-QOC with Anaconda on a windows environment (https://github.com/qutip/qutip-qoc/issues/30)

- qutipqip.py: A more involved example of how to use QuTiP-QIP for quantum simulation. Used to generate figs. 21-24.

- smesolve.py: A basic example of how to use the stochastic master equation solver. Used to generate Fig. 9.

- solver.py: A basic example of how to use the new solver interface.

- /environment_examples/environment.py: A utility file for the new environment class interface. Replaced by latest official QuTiP 5.1.0 release.

- /environment_examples/heom_example.py: A basic example of how to use the new envirionment interface with the HEOM solver. Used to generate Fig. 10 and 11.

- /environment_examples/heom_transition.py:  A more involved example of how to use the fitting features to capture the spin-boson phase transition with the HEOM solver. Used to generate Fig. 12

- /environment_examples/mesolvedriven.py: An example of how to model driven systems with mesolve and the HEOM solver. Used to generate Fig. 3.

The alternative development versions of the last examples, and the jax-based mcsolve example, are available in:

- /environment_examples_dev/

The environment-class based examples require QuTiP 5.1.0 or the development release, while jax-mcsolve.py requires the development version of both QuTiP and  QuTiP-JAX, which can be achieved with:

```shell
pip install git+https://github.com/qutip/qutip.git
pip install git+https://github.com/qutip/qutip-jax.git
```