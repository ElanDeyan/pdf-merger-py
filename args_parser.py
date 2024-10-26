from argparse import ArgumentParser
from pathlib import Path

from constants import MERGER_COMMAND_NAME, REPEATER_COMMAND_NAME


parser = ArgumentParser(
    description="Basic python script to merge pdf files in specific dir, and repeat n files in one"
)

subparsers = parser.add_subparsers(dest="command")

merger_parser = subparsers.add_parser(
    MERGER_COMMAND_NAME,
    help="Merge all PDF in provided dir",
    usage="pdf_merger merge -d ./ -o ./result.pdf",
)

merger_parser.add_argument(
    "--dir",
    "-d",
    type=Path,
    dest="directory",
    help="Directory with pdf files to merge",
)
merger_parser.add_argument(
    "--output",
    "-o",
    type=Path,
    dest="output",
    help="File (with .pdf suffix) to write the result. The directory needs to be existent.",
)

repeater_parser = subparsers.add_parser(
    REPEATER_COMMAND_NAME,
    help="Merge the provided .pdf file n time in one file",
    usage="pdf_merger repeat -f ./file.pdf -n 3 -o ./result.pdf",
)

repeater_parser.add_argument(
    "--number",
    "-n",
    default=1,
    type=int,
    help="How many copies of the provided file",
)

repeater_parser.add_argument(
    "--file",
    "-f",
    required=True,
    type=Path,
    help="File to be copied",
)

repeater_parser.add_argument(
    "-o",
    "--output",
    type=Path,
    dest="output",
    help="File (with .pdf suffix) to write the result. The directory needs to be existent.",
)
