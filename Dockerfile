FROM jupyter/minimal-notebook:f3da74a3da1e as eda
USER root
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable toc2/main --user
RUN pip install papermill seaborn
ENTRYPOINT ["python"]
