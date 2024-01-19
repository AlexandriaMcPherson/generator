#!/bin/bash

if [ ! -e .venv ]; then
    python3 -m venv .
    source ./bin/activate
    pip install -r requirements.txt
else
    source ./bin/activate
fi