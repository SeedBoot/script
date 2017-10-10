"""
A boilerplate PHP/ SCSS workspace
-   Place this script and the folder in 'C:/script' or similar
    and point your PATH to that folder.
-   Otherwise, place this script and the folder into the root of
    your project and comment out the ROOT variable
"""
#!/usr/bin/env python

###########
# IMPORTS #
###########

import os
import shutil
import subprocess

#############
# VARIABLES #
#############

# ROOT FOLDER FOR ASSETS #
ROOT = 'C:/script/asset/'

# Lists etc. for SCSS folders and files
STYLE_FOLDER = [
    'import',
    'export'
]

SCSS_DEST = 'style/import/'

SCSS_FILE = [
    ROOT + 'style.scss',
    ROOT + '_var.scss'
]

# PHP variables
PHP_INC = ROOT + 'includes'

PHP_FILE = ROOT + 'index.php'

# List for JS generation
JS_FILE = [
    ROOT + 'script.js',
    'script/'
]

# Generate script and style folders
os.mkdir('script')
os.mkdir('style')

# Generate import:export folders for styling
for folder in STYLE_FOLDER:
    os.mkdir(os.path.join('style', folder))

# Copy SCSS files into import folder
for i in SCSS_FILE:
    shutil.copy2(i, SCSS_DEST)

# Copy PHP files
shutil.copytree(PHP_INC, 'includes')

shutil.copy2(PHP_FILE, 'index.php')

# Copy JS files
shutil.copy2(JS_FILE[0], JS_FILE[1])

####################
# SYSTEM FUNCTIONS #
####################

# Opens a new cmd to listen for import:export SCSS files
os.system('start cmd /c sass --watch style/import:style/export')

#Opens Wamp
subprocess.call("C:\\wamp64\\wampmanager.exe", shell=True)