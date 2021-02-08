FROM jupyter/minimal-notebook:016833b15ceb
USER root
RUN pip install jupyter_contrib_nbextensions papermill seaborn
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable toc2/main --user
ENTRYPOINT ["python","run_notebook.py"]
