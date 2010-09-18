from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

setup(
    name = 'ROM Downloader',
    version = '2.0',
    author = 'Hondros',
    company = 'pH Productions',
    description = 'Console',
    options = {
        'py2exe': {
            'bundle_files': 1,
            }
        },
    console=['ROM Downloader.py'],
    zipfile = None,
    )
