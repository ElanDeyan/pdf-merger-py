from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(description='Basic python script to merge pdf files in specific dir')

parser.add_argument(
    "-d", "--dir", type=Path, dest="directory", help="Directory with pdf files to merge"
)
parser.add_argument(
    "-o",
    "--output",
    type=Path,
    dest="output",
    help="File (with .pdf suffix) to write the result. The directory needs to be existent.",
)
