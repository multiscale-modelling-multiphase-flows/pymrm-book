import os

# Define paths
examples_dir = "pymrm/examples"
output_file = "content/examples/examples.rst"

# Header for the RST file
rst_header = """\
Examples
========

Below is a list of available example notebooks.

.. toctree::
   :maxdepth: 1
   :caption: Example Notebooks

"""

def find_notebooks(directory):
    """Find all Jupyter notebooks (*.ipynb) in the specified directory."""
    notebooks = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                # Get relative path without extension
                relative_path = os.path.join("../../", root, file).replace("\\", "/")
                notebooks.append(os.path.splitext(relative_path)[0])  # Exclude ".ipynb"
    return sorted(notebooks)

def generate_rst(notebooks, output_path):
    """Generate the RST file with a list of notebooks."""
    with open(output_path, "w") as f:
        # Write the header
        f.write(rst_header)
        # Write each notebook
        for notebook in notebooks:
            f.write(f"   {notebook}\n")
    print(f"RST file generated: {output_path}")

if __name__ == "__main__":
    # Find notebooks and generate the RST file
    notebooks = find_notebooks(examples_dir)
    generate_rst(notebooks, output_file)
