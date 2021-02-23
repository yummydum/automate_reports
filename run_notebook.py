"""
Usage:
    python run_notebook <color> (G,E,F,H,D,I,J)
"""

import sys
import papermill as pm

# Check if the parameter is properly set
nb_path = 'notebooks/example.ipynb'
result = pm.inspect_notebook(nb_path)
assert 'color' in result

# Execute the notebook with the parameter
color = sys.argv[1]
pm.execute_notebook(
    nb_path,
    f'notebooks/example_{color}.ipynb',
    parameters={'color': color},
)
