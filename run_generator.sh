#!/bin/bash

rows=$1
in_file=$2

if [ -n "$3" ];
then
    seed=$3
    python3 main.py "$rows" "$in_file" "$seed"
else
    python3 main.py "$rows" "$in_file"
fi