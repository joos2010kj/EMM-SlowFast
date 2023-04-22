from argparse import ArgumentParser
import os

arg_parser = ArgumentParser()

arg_parser.add_argument("--name", type=str)
arg_parser.add_argument("--start", type=int, default=0)
arg_parser.add_argument("--duration", type=int, default=-1)
arg_parser.add_argument("--fps", type=int, default=10)
arg_parser.add_argument("--output", type=str, default="temp.gif")


config = arg_parser.parse_args()

cmd = "ffmpeg "

if config.start != 0:
    cmd += f"-ss {config.start} "

if config.duration != -1:
    cmd += f"-t {config.duration} "
    
cmd += f"-i {config.name} "

cmd += f'-vf "fps={config.fps},split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {config.output} -hide_banner -loglevel error'
 
os.system(cmd)

"""
e.g.,
python giffy.py --name res.mp4 --start 10 --duration 5 
"""