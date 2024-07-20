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
    writer = PdfWriter()

    for file in files:
        writer.merge(None, fileobj=PdfReader(file, True))

    writer.write(result_path.with_suffix(PDF_SUFFIX))


def main():
    args = parser.parse_args()

    files = pdf_files_in_directory(Path(args.directory))
    if files is not None:
        merge_pdf_files(files, args.output)


main()
