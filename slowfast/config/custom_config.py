#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

"""Add custom configs and default values"""

PUPILLAB_SAMPLE = "/home/kevin/repo/EngageMMent/data/2023-04-05_16-22-53-56aaa2a6/PI world v1 ps1.mp4" 


def add_custom_config(_C):
    dataset = ["kinetics", "ava"][1]    # ava or kinetics?
    mode = ["demo", "train", "test"][0]
    _C.NUM_GPUS = [1, 2, 4, 8][2]

    """
    applicable to demo only
    """
    input_video = "video_list/ava_demo_clone.mp4" # input video?
    output_file = "temp.mp4"    # output location?
    localize_and_label_actions = True

    """
    DO NOT TOUCH BELOW
    """
    path_to_pretrained_ckpt = {
        "kinetics": "checkpoints/SLOWFAST_8x8_R50.pkl",
        "ava": "checkpoints/ava/SLOWFAST_32x2_R101_50_50.pkl"
    }[dataset]

    framework = {
        "kinetics": "caffe2",
        "ava": "pytorch"
    }[dataset]

    # GLOBAL
    _C.TRAIN.CHECKPOINT_FILE_PATH = path_to_pretrained_ckpt
    _C.TEST.CHECKPOINT_FILE_PATH = path_to_pretrained_ckpt
    _C.TRAIN.CHECKPOINT_TYPE = framework
    _C.TEST.CHECKPOINT_TYPE = framework
    _C.DEMO.LABEL_FILE_PATH = {
        "kinetics": "labels/kinetics-400-demo-labels.json",
        "ava": "labels/ava-labels-ind-0.json"
    }[dataset]

    if mode == "demo":
        _C.TRAIN.ENABLE = False
        _C.TEST.ENABLE = False
        _C.DEMO.ENABLE = True
        # _C.DEMO.CLIP_VIS_SIZE = 50 # Prediction & BBox Annotation Rate (higher = longer)

        _C.DEMO.INPUT_VIDEO = input_video
        _C.DEMO.OUTPUT_FILE = output_file
        _C.DEMO.UNCOMMON_CLASS_THRES = 0.3 # 0.7
        _C.DEMO.WEBCAM = -1

        _C.DETECTION.ENABLE = localize_and_label_actions
        _C.DETECTION.ALIGNED = True # not localize_and_label_actions
    elif mode == "test":
        _C.TRAIN.ENABLE = False
        _C.TEST.ENABLE = True
        _C.DEMO.ENABLE = False
