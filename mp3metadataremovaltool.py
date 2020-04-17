from sys import argv
from mutagen.mp3 import MP3
from threading import Thread
import os

if len(argv) > 1:
    FILE_PATH = argv[1]
else:
    print('Usage: python path/to/script.py "path/to/directory" ')
    exit(0)


def deleteAllMetadata(path):
    folders = []
    for filename in os.listdir(path):
        fname = os.path.join(path, filename)

        #Code block inspired/remixed by 
        # https://code.activestate.com/recipes/577139-remove-id3-tags-from-mp3-files/
        # Licensed under MIT 
        if fname.lower().endswith(".mp3"):
            mp3 = MP3(fname)
            
            try:
                mp3.delete()
                mp3.save()
                print(f"Done for {fname}")
            except Exception as e:
                print(f"Got {e}")
                
        elif os.path.isdir(f"{path}\\{filename}"):
            print(f"found folder {filename}")
            folders.append(f"{path}\\{filename}")
        
    for folder in folders:
        Thread(target = deleteAllMetadata, args = (folder,)).start()
        

if __name__ == "__main__":
    deleteAllMetadata(FILE_PATH)
