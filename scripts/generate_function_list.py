import pymrm
import inspect

modules = [
    pymrm.grid,
    pymrm.convect,
    pymrm.numjac,
    pymrm.solve,
    pymrm.interpolate,
    pymrm.operators,
    pymrm.helpers,
]

all_items = []
for module in modules:
    for name, obj in inspect.getmembers(module):
        if (inspect.isfunction(obj) or inspect.isclass(obj)) and obj.__module__ == module.__name__:
            all_items.append(f"{module.__name__}.{name}")

all_items = sorted(all_items)

# Write the sorted list to api.rst or a separate file
with open("content/api/alphabetical_overview.rst", "w") as f:
    f.write("Alphabetical Overview\n")
    f.write("=====================\n\n")
    f.write("An overview of all functions and classes in the `pymrm package.\n\n")
    f.write(".. autosummary::\n")
    f.write("   :toctree: generated/all\n")
    f.write("   :nosignatures:\n\n")
    for item in all_items:
        f.write(f"   {item}\n")
