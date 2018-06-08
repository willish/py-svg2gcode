import argparse
import svg2gcode as s2g; 


def convert(svgfile_path):
    s2g.generate_gcode(svgfile_path)


parser = argparse.ArgumentParser()

parser.add_argument('svgfile', help='input svg file path')
args = parser.parse_args()

svgfile_path = args.svgfile

convert(svgfile_path)


