#!/bin/bash

raspivid -vf -n -w 640 -h 480 -o - -t 0 -b 2000000 | nc 10.0.33.2 5777
