# Ensure you're in the repository root
Set-Location -Path pymrm/pymrm

# Build the Sphinx documentation
sphinx-build -b html docs docs/_build/html

Write-Host "API documentation built successfully!"