import argparse

parser = argparse.ArgumentParser()

parser.add_argument('svg-file-path', help='input svg file path')
args = parser.parse_args()


print(args)

