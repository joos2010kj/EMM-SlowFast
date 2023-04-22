#!/bin/bash
file=tools/run_net.py

# configs
ava=demo/AVA/SLOWFAST_32x2_R101_50_50.yaml
kinetics=configs/Kinetics/c2/SLOWFAST_8x8_R50.yaml

# kinetics=configs/Kinetics/c2/SLOWFAST_8x8_R101_50_50.yaml

## DEMO RUN
python $file --cfg $kinetics
