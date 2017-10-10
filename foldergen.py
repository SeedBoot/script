#!/usr/bin/env python

"""Generates directories for screenshots"""
import os

############################
# variables: DO NOT DELETE #
############################
EN_FOLDER = "EN"
FR_FOLDER = "FR"
#Rename these if needed#
CATEGORIES = [
    "_Homescreens", "1 Getting Started", "2 Device Software",
    "3 Email, Contacts,,,", "4 Sync", "5 Usage",
    "6 Trouble", "7 Wifi", "8 Travelling"
]

##############################################
# creates initial directories: DO NOT DELETE #
##############################################
os.mkdir(EN_FOLDER)
os.mkdir(FR_FOLDER)
os.mkdir("Statusbar")

###############################################
# Loops that make directories from CATEGORIES #
#  inside EN and FR directories respectively  #
###############################################
for folder in CATEGORIES:
    os.mkdir(os.path.join(EN_FOLDER, folder))

for folder in CATEGORIES:
    os.mkdir(os.path.join(FR_FOLDER, folder))
