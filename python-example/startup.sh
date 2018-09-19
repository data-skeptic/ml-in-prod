#!/bin/bash

echo "Starting!"
if [ -n $MODE ]
then
  if [ $MODE = "DEV" ]
  then
    echo "Starting in DEV mode"
    jupyter lab --port=8888 --ip=0.0.0.0 --allow-root
    exit
  elif [ $MODE = "API" ]
  then
    echo "Starting in API mode"
    cd /app
    ls
    python model_service.py
    exit
  else
    echo "Could not recognize MODE = $(echo $MODE) parameter.  Please use DEV or API"
    exit
  fi
else
  echo -e "MODE not set.  Please restart image with MODE=DEV or MODE=API\n"
fi
