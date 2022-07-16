from mutagen.flac import FLAC
import zipfile
import os
def extract(file, destination): 
    with zipfile.ZipFile(file, 'r') as z:
        z.extractall(destination)

        