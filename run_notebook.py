import sys
import papermill as pm

# Check if the parameter is properly set
nb_path = 'notebooks/example.ipynb'
params = pm.inspect_notebook(nb_path)
assert 'color' in params

# Execute the notebook with the parameter
color = sys.argv[1]
pm.execute_notebook(
    nb_path,
    f'notebooks/example_{color}.ipynb',
    parameters={'color': color},
)
