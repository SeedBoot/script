"""
A boilerplate static HTML website creator

-   Place this script and the folder in 'C:/script' or similar
    and point your PATH to that folder.

-   Otherwise, place this script and the folder into the root of
    your project and comment out the ROOT variable
"""
#!/usr/bin/env python

from os import mkdir
from shutil import copy2

ROOT = 'C:/script/'

SRC = {
    'html': ROOT + 'asset/index.html',
    'css': ROOT + 'asset/style.css',
    'js': ROOT + 'asset/script.js'
}
DEST = {
    'html': 'index.html',
    'css': 'style/style.css',
    'js': 'script/script.js'
}

mkdir('style')
mkdir('script')

copy2(SRC['html'], DEST['html'])
copy2(SRC['css'], DEST['css'])
copy2(SRC['js'], DEST['js'])
