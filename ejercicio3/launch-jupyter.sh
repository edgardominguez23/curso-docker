#!/bin/bash
docker run --rm -p 8888:8888 \
  -v "$(pwd)/notebooks:/home/jovyan/work" \
  jupyter/base-notebook start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''
