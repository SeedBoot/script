"""
Change yo names
"""
#!/usr/bin/env python

import os

path = "C:\\Downloads\\Game of Thrones\\Game of thrones season 1\\testing"

#[os.rename(f, f.replace('.', ' ')) for f in os.listdir('.') if not f.startswith('.')]

fileLists = print(os.listdir(path))
fileList = os.listdir(path)

for words in fileList:
    words.split(' ')
    print(words)

"""
for joining in fileList:
    '.'.join(joining)
    print(joining)
"""
