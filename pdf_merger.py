from argparse import Namespace
from pathlib import Path
from typing import Optional
from pypdf import PdfWriter, PdfReader

from args_parser import parser
from constants import MERGER_COMMAND_NAME

PDF_SUFFIX = ".pdf"


def pdf_files_in_directory(path: Path) -> Optional[list[Path]]:
    files: list[Path] = []

    if path.is_dir():
        for file in path.iterdir():
            if file.suffix == PDF_SUFFIX:
                files.append(file.absolute())
    elif path.suffix == PDF_SUFFIX:
        return [path.absolute()]

    return files if len(files) > 0 else None


def merge_pdf_files(files: list[Path], result_path: Path) -> None:
    writer = PdfWriter()

    for file in files:
        writer.merge(None, fileobj=PdfReader(file, True))

    write_to_output(writer, result_path, "Files merged succesfully")


def repeat_files(file: Path, number: int, result_path: Path) -> None:
    pdf_writer = PdfWriter()

    for _ in range(number):
        pdf_writer.merge(None, fileobj=PdfReader(file, True))

    write_to_output(pdf_writer, result_path, "Success!")


def write_to_output(
    writer: PdfWriter,
    result_path: Path,
    message_on_success: Optional[str] = None,
) -> None:
    try:
        if result_path.with_suffix(PDF_SUFFIX).exists():
            response = input(
                f"The file {result_path.name}.pdf exists, do you want to overwrite? (y/N): "
            )

            if response.lower() != "y":
                print("Operation canceled.")
                return
        writer.write(result_path.with_suffix(PDF_SUFFIX))
        if message_on_success is not None:
            print(message_on_success)
    except Exception as e:
        print(f"Failed: {e}")


def main() -> None:
    cli_args: Namespace = parser.parse_args()

    if cli_args.command == MERGER_COMMAND_NAME:
        files_to_merge = pdf_files_in_directory(Path(cli_args.directory))
        if files_to_merge is not None:
            merge_pdf_files(files_to_merge, cli_args.output)
    else:
        file_to_repeat: Path = cli_args.file
        if not file_to_repeat.is_dir():
            repeat_files(cli_args.file, cli_args.number, cli_args.output)
        else:
            print(
                "Directory not available, to merge files in a directory, use merge command instead"
            )


main()
