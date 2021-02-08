"""
Usage:
    python run_notebook <color> (G,E,F,H,D,I,J)
"""

import sys
import papermill as pm

# Check if the parameter is properly set
result = pm.inspect_notebook('example.ipynb')
assert 'color' in result

# Execute the notebook with the parameter
color = sys.argv[1]
pm.execute_notebook(
    'example.ipynb',
    f'example_{color}.ipynb',
    parameters={'color': color},
)
