# unmht
**unmht** is a simple [MHTML][mhtml] extractor.

It uses Python's `email` module to facilitate message parsing, so technically it
can be used to extract any multipart messages, although it was tested to work
only with MHTML.

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

# TODO
* Change resource paths in resulting HTMLs to their new locations