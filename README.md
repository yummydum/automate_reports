# Jupyter Notebook Ops


## Execute parametrized notebook via docker
```shell
docker build . -t diamond_notebook
docker run --mount type=bind,source="$(pwd)",target=/home/jovyan/ diamond_notebook <color>
```
Where `<color>` should be one from [G,E,F,H,D,I,J].

## Run commuter in local

Install by `yarn global add @nteract/commuter`, then

```shell
COMMUTER_LOCAL_STORAGE_BASEDIRECTORY=./notebooks commuter
```
Open browser and see `localhost:4000`.

## Slides
https://www.slideshare.net/AtsushiSumita/jupyter-notebook-ops

## References
https://netflixtechblog.com/notebook-innovation-591ee3221233