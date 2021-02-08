# automate_reports

```
docker build . -t diamond_notebook
docker run --mount type=bind,source="$(pwd)",target=/home/jovyan/ diamond_notebook <color>
```
