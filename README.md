# Report Generation Example

Run the below command for the demo.
The color parameter should be one from [G,E,F,H,D,I,J].

```
docker build . -t diamond_notebook
docker run --mount type=bind,source="$(pwd)",target=/home/jovyan/ diamond_notebook <color>
```
