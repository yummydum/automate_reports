FROM jupyter/base-notebook
RUN pip install papermill seaborn
ENTRYPOINT ["python","run_notebook.py"]
