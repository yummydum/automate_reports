# Report Generation Example


## Execute parametrized notebook via docker
```shell
docker build . -t diamond_notebook
docker run --mount type=bind,source="$(pwd)",target=/home/jovyan/ diamond_notebook <color>
```
Where `<color>` should be one from [G,E,F,H,D,I,J].

## Run commuter in local

```shell
yarn global add @nteract/commuter
COMMUTER_LOCAL_STORAGE_BASEDIRECTORY=./notebooks commuter
open localhost:4000
```

