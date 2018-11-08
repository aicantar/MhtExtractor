# MhtExtractor
Simple [MHTML][mhtml] extractor.

This software uses Python's `email` library to facilitate message parsing.
Technically, it is possible to unpack any multipart message with it, although
it was tested only with MHTML.

[mhtml]: https://en.wikipedia.org/wiki/MHTML

# Usage
```
usage: unmht [-h] [-o OUTPUT_DIR] [-v] FILE [FILE ...]

mht extractor; info: https://github.com/aicantar/unmht

positional arguments:
  FILE           files to extract

optional arguments:
  -h, --help     show this help message and exit
  -o OUTPUT_DIR  output directory
  -v             enable verbose mode
```
