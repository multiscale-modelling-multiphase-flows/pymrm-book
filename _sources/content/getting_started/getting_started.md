# Getting Started with PyMRM

To get familiar with the basics of PyMRM, start by running some Jupyter notebooks. A great first step is the [](../../pymrm/examples/counter_diffusion_reaction.ipynb) notebook. After that, you can explore a variety of [examples](../examples/examples.rst) to deepen your understanding, and then try developing your own models. For additional practice, consider working through the [exercises](../exercises/index.md). To fully understand PyMRM's functions and classes, consult the [API documentation](../api/api.rst).

For setting up your environment to run and develop multiphase reactor models with PyMRM, follow our [installation guide](../../pymrm/docs/installation.md).

If you prefer to explore sample notebooks quickly, you can use [Google Colab](https://colab.research.google.com/). Follow these steps to open a sample notebook from GitHub on Colab:

1. **Go to Google Colab**: [Google Colab](https://colab.research.google.com/).
2. **Open the GitHub tab**:
   - Navigate to **File → Open Notebook**.
   - Click on the **GitHub** tab.
3. **Enter the repository URL**:  
   Paste this URL into the input box:  
   [](https://github.com/multiscale-modelling-multiphase-flows/pymrm).
4. Navigate to the [examples folder](https://github.com/multiscale-modelling-multiphase-flows/pymrm/tree/main/examples) and choose a notebook, such as [counter_diffusion_reaction.ipynb](https://github.com/multiscale-modelling-multiphase-flows/pymrm/blob/main/examples/counter_diffusion_reaction.ipynb).

Using this setup, you can explore and run sample notebooks directly from the repository.

To use PyMRM, you need to install the package. Add a code cell at the top of a notebook, then paste and execute the following code:

```python
!pip install pymrm