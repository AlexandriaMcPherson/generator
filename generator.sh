#!/bin/bash

source setup_venv.sh

if [ -n "$3" ]; then
    ./run_generator.sh $1 $2 $3
else
    ./run_generator.sh $1 $2
fi

deactivate