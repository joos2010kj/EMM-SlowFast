#!/bin/bash

# GLOBAL
file=tools/run_net.py
export CUDA_VISIBLE_DEVICES=4,5,6,7

# # KINETICS SETUP
# cfg=configs/Kinetics/c2/SLOWFAST_8x8_R50.yaml # CAFFE2

# AVA SETUP
cfg=demo/AVA/SLOWFAST_32x2_R101_50_50.yaml # PYTORCH

## DEMO RUN
python $file --cfg $cfg
