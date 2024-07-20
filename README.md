# PDF merger in Python

This is a basic project to merge pdf files.

## Getting started

To get help, run:

```sh
python -m pdf_merger -h
```

You can use it like this:

```sh
python -m pdf_merger -d dir/with/pdf/files -o result/file.pdf
```

Or using the long form:

```sh
python -m pdf_merger --dir dir/with/pdf/files --output result/file.pdf
```

> [!NOTE]
> You don't need to type the .pdf extension, the script will add it.

> [!IMPORTANT]
> The output directory should exists. For example, if you pass a path to a non-existent directory, the script will fail
