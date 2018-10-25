# unmht
**unmht** is a simple [MHTML][mhtml] extractor. It extracts `mht` files
into a browser's `Save As...`-like folder structure (i.e. for 
`google.mht` it will create `google.html` for the index file and put
the resources into `google.html_files` directory).

It uses Python's standard `email` module to facilitate message parsing
so, technically, it can be used to extract any multipart message, but it
was tested only with MHTML files.

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
* Rewrite resource paths in the resulting HTML to their new locations
* Add setup script
* Switch from compat32 policy for the email message parsing
* Set `atime` and `mtime` from the `Date` header(?)