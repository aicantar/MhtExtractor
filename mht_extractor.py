import os
import email
import argparse
from urllib.parse import urlparse


class Helpers:
    @staticmethod
    def partname_or_filename(fp, url):
        return os.path.basename(urlparse(url).path) or '{}.html'.format(os.path.basename(os.path.splitext(fp.name)[0]))


class Extractor:
    def __init__(self, fp, output_dir, verbose=False):
        self.fp = fp
        self.output_dir = output_dir
        self.verbose = verbose
        self.fdir = '{}.html_files'.format(os.path.basename(os.path.splitext(self.fp.name)[0]))

    @classmethod
    def extract_files(cls, files, output_dir, verbose=False):
        for file in files:
            with open(file, 'r') as fp:
                yield cls(fp, output_dir, verbose)

    def extract(self):
        message = email.message_from_file(self.fp)

        self._print(f'Extracting {self.fp.name}', verbose_only=True)

        for part in message.walk():
            content_type = part.get_content_type()
            content_location = part['Content-Location']
            name = Helpers.partname_or_filename(self.fp, content_location)

            if content_type.startswith('multipart'):
                continue

            #TODO: using legacy api
            self._write(name, part.get_payload(decode=True))

    def _write(self, name, content):
        newpath = ''

        if name.endswith('html'):
            newpath = os.path.join(self.output_dir, name)
        else:
            if not os.path.exists(os.path.join(self.output_dir, self.fdir)):
                os.mkdir(os.path.join(self.output_dir, self.fdir))

            newpath = os.path.join(self.output_dir, self.fdir, name)

        self._print(f'{name} -> {newpath}')

        with open(newpath, 'wb') as fp:
            fp.write(content)

    def _print(self, *args, verbose_only=False, **kwargs):
        if verbose_only:
            if self.verbose:
                print(*args, **kwargs)
        else:
            print(*args, **kwargs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='mht_extractor',
        description='info: https://github.com/aicantar/MhtExtractor'
    )

    parser.add_argument(
        'FILE',
        nargs='+',
        help='files to extract'
    )

    parser.add_argument(
        '-o',
        default='.',
        dest='output_dir',
        help='output directory'
    )

    parser.add_argument(
        '-v',
        action='store_true',
        dest='verbose',
        help='enable verbose mode'
    )

    args = parser.parse_args()

    for ex in Extractor.extract_files(args.FILE, args.output_dir, args.verbose):
        ex.extract()
