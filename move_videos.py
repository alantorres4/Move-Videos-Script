# Problem: iPhone cameras can take "Live" photos which basically makes each photo taken on "Live" mode into a 2-3 sec GIF. This is a problem if you move all your photos/videos to your computer, because it recognized these Live photos as .MOV 2-3 sec videos. Thus, your actual videos and these weird GIFs are all in the same folder and it's hard to separate them.

# Solution: This program goes through a folder and gets the metadata for that video file. Then, if the video is longer than 4 seconds, it will be moved to a new folder.

# To Run in the command line:  python3 sortVideos.py   input_directory   output_directory

import os
import sys
import shutil
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

inputDirectoryPath = os.path.join(os.getcwd(), sys.argv[1])
outputDirectoryPath = os.path.join(os.getcwd(), sys.argv[2])

print(f"input = {inputDirectoryPath}")
print(f"output = {outputDirectoryPath}")

# Get list of files in directory
input_files = os.listdir(inputDirectoryPath)

# Keep track of how many files were actually successful 
successful = 0
failed = 0

# Go through entire directory
for file in input_files:
        try:
                print(f"VIDEO PATH: {os.path.join(inputDirectoryPath, file)}")
                fileParser = createParser(os.path.join(inputDirectoryPath, file))
                fileInfo = extractMetadata(fileParser)
                durationTime = fileInfo.get('duration')
                if(durationTime.seconds > 4):
                        shutil.move(os.path.join(inputDirectoryPath, file), outputDirectoryPath)
                print("-----------------------------")
                successful+=1
        except:
                print("[-] Something went wrong.")
                failed+=1


print(f"\nSUCCESSFUL FILES: {successful}")
print(f"FAILED FILES: {failed}")
