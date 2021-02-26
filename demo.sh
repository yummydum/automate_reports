#!/bin/bash

########################
# include the magic
########################
. demo-magic.sh

# hide the evidence
clear

# Put your stuff here
wait
pei "ls notebooks"
PROMPT_TIMEOUT=2
wait
pei "COMMUTER_LOCAL_STORAGE_BASEDIRECTORY=./notebooks commuter > /dev/null 2>&1 &"
PROMPT_TIMEOUT=0
wait
pei 'docker run --mount type=bind,source="$(pwd)",target=/home/jovyan/ diamond_notebook G'
PROMPT_TIMEOUT=2
wait
pei "ls notebooks"