from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

setup(
    name = 'ROM Downloader',
    version = '1.0',
    author = 'Hondros',
    company = 'pH Productions',
    description = 'Rom Downloader',
    options = {
        'py2exe': {
            'bundle_files': 1,
            "includes" : ["sip"]
            },
        },
    windows=[{"script" : 'ROM Downloader.pyw'}],
    zipfile = None,
    )