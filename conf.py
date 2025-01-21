import os
import sys
sys.path.insert(0, os.path.abspath("./pymrm"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
]

# Other Sphinx configurations
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
