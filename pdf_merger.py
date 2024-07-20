from pathlib import Path
from typing import Optional
from pypdf import PdfWriter, PdfReader

from args_parser import parser

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


def merge_pdf_files(files: list[Path], result_path: Path):
    try:
        writer = PdfWriter()

        for file in files:
            writer.merge(None, fileobj=PdfReader(file, True))

        if result_path.with_suffix(PDF_SUFFIX).exists():
            response = input(
                f"The file {result_path.name}.pdf exists, do you want to overwrite? (y/N): "
            )

            if response.lower() != "y":
                print("Operation canceled.")
                return

        writer.write(result_path.with_suffix(PDF_SUFFIX))
        print('PDFs merged succesfully!')
    except Exception as e:
        print(f"Failed to merge: {e}")


def main():
    args = parser.parse_args()

    files = pdf_files_in_directory(Path(args.directory))
    if files is not None:
        merge_pdf_files(files, args.output)


main()
