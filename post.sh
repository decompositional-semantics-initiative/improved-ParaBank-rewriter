#!/bin/bash

sed -r 's/@@( |$)//g' \
| \
python detok.py
