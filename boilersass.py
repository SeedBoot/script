"""
A boilerpate SCSS workspace

-   Place this script and the folder in 'C:/script' or similar
    and point your PATH to that folder.

-   Otherwise, place this script and the folder into the root of
    your project and comment out the ROOT variable
"""
#!/usr/bin/env python

# Imports
import os
import shutil

# Variables for HTML and JS generation
ROOT = 'C:/script/asset/'

SRC = {
    'html': ROOT + 'index.html',
    'js': ROOT + 'script.js'
}
DEST = {
    'html': 'index.html',
    'js': 'script/script.js'
}

# Variables for SCSS folders and files
STYLE_FOLDER = ['import', 'export']
SCSS_FILE = [ROOT + 'style.scss', ROOT + '_var.scss']

# Generate script and style folders
os.mkdir('script')
os.mkdir('style')

# Generate import:export folders for styling
for folder in STYLE_FOLDER:
    os.mkdir(os.path.join('style', folder))

# Copy HTML, JS and SCSS files into directory
shutil.copy2(SRC['html'], DEST['html'])
shutil.copy2(SRC['js'], DEST['js'])
shutil.copy2(SCSS_FILE[0], 'style/import/')
shutil.copy2(SCSS_FILE[1], 'style/import/')

# Opens a new cmd to listen for import:export SCSS files
os.system('start cmd /c sass --watch style/import:style/export')
