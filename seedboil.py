"""
A boilerplate workspace
-   Place this script and the folder in 'C:/script' or similar
    and point your PATH to that folder.
-   Otherwise, place this script and the folder into the root of
    your project and comment out the ROOT variable

-   Use this script to tailor your dev environment.
    Choose from PHP/ HTML and CSS/SCSS

-   This script assumes you have Sass installed!
    & the asset folder containing the files below.
"""
#!/usr/bin/env python

###########
# IMPORTS #
###########
import os
import shutil
import time

#############
# VARIABLES #
#############
# ROOT FOLDER FOR ASSETS #
root = 'C:/script/asset/'

# VANILLA DEV VARIABLES #
#########################
#source for html, js and css files
src = {
    'html': root + 'index.html',
    'css': root + 'style.css',
    'js': root + 'script.js'
}

# Destination for html, css and js
dest = {
    'html': 'index.html',
    'css': 'style/style.css',
    'js': 'script/script.js'
}

# SCSS VARIABLES #
##################
# source for scss files
scss_file = [root + 'style.scss', root + '_var.scss']

# Variables for SCSS destination folders
scss_dest = 'style/import/'

style_folder = ['import', 'export']

# PHP VARIABLES #
#################
# includes folder
php_inc = root + 'includes'

# php index file
php_file = root + 'index.php'

#############
# FUNCTIONS #
#############
# PHP #
#######

def php_gen():
    """
    This function copies PHP files and folders
    into the target location
    """
    shutil.copytree(php_inc, 'includes')
    shutil.copy2(php_file, 'index.php')

# SCSS #
########
def scss_gen():
    """
    This function generates import:export folders for styling
    & then copies SCSS files into the import folder
    """
    for folder in style_folder:
        os.mkdir(os.path.join('style', folder))

    for i in scss_file:
        shutil.copy2(i, scss_dest)

######################
## ON WITH THE SHOW ##
######################
print('Welcome to SeedBoot\'s boilerplate generator!')
time.sleep(1)
print('Generating intial files...')

# generate style and script folders
os.mkdir('style')
os.mkdir('script')

# copy js script file
shutil.copy2(src['js'], dest['js'])

time.sleep(0.5)
print('style and script folders generated.')
time.sleep(0.6)
print('JS file generated.')
time.sleep(0.7)

# HTML or PHP loop #
####################
# create empty variable for html/ php loop
hp = ''

while hp != '0' or hp != '1':
    # turn hp to input
    hp = input('Now, will you be using [0]HTML or [1]PHP today?\n')

    # give user the choice of HTML or PHP file to be generated
    if hp == '0':
        time.sleep(0.5)
        print('Ok, HTML it is!')

        #copy HTML file
        shutil.copy2(src['html'], dest['html'])
        break

    elif hp == '1':
        time.sleep(0.5)
        print('Ok, PHP it is!')

        php_gen()

    else:
        time.sleep(0.5)
        print('wut')
    break

time.sleep(0.7)
print('Now for some style!')

# CSS or SCSS loop #
####################

# create empty variable for css/ scss loop
css = ''

while css != '0' or css != '1':
    time.sleep(0.7)
  # turn css to input
    css = input('Will you be using [0]CSS or [1]SCSS today?\n')

    if css == '0':
        time.sleep(0.5)
        print('CSS it is!')
        # copy css file
        shutil.copy2(src['css'], dest['css'])
        break

    elif css == '1':
        time.sleep(0.5)
        print('SCSS it is!')

        scss_gen()

        # create empty variable for sass --watch command
        sasswatch = ''

        while sasswatch != 'y' or sasswatch != 'n':
            time.sleep(0.5)
            # turn sasswatch to input
            sasswatch = input('Do you want sass watching your SCSS folders? [y/n]\n').lower()

            if sasswatch == 'y':
                time.sleep(0.5)
                print('...')

                # Opens a new cmd to listen for import:export SCSS files
                os.system('start cmd /c sass --watch style/import:style/export')
                time.sleep(0.3)
                print('Done!')
                break

            elif sasswatch == 'n':
                time.sleep(0.5)
                print('Your loss!')
                break

            else:
                time.sleep(0.5)
                print('wut')
        break
        # END WHILE SCSS LOOP
    else:
        time.sleep(0.5)
        print('wut')

time.sleep(0.5)
print('Your dev setup is complete...')
time.sleep(0.7)
print('Happy coding!')
time.sleep(1.3)
