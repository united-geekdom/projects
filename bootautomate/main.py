from mutagen.mp3 import MP3
import zipfile
import os
with zipfile.ZipFile("../../commiequaver/player/songs.zip", 'r') as z:
        z.extractall("place")
for filename in os.listdir("place"):
    f = os.path.join("place", filename)
    if f.endswith('.mp3'):
        audio = MP3(f)
        print(audio.info.length)
