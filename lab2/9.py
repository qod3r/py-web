import argparse
from format_text import format_text_block


parser = argparse.ArgumentParser()
parser.add_argument('--frame-height', type=int)
parser.add_argument('--frame-width', type=int)
parser.add_argument('file')

args = parser.parse_args()

print(format_text_block(args.frame_height, args.frame_width, args.file))