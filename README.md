# Move-Videos-Script
This Python program takes in a directory name, combs through the files in that directory, and moves them to a given output directory based on a specific criteria. 

This idea was born from a hassle with Apple's "Live Photos". Since these Live Photos are 2-3 second videos, they're interesting to see in a text message, but when you have a folder full of long videos (ex. 2 min each) mixed with these short 2-3 second videos, it can be tiresome to comb through the list of videos to see which one's aren't Live Photos. 

This program gets the metadata from a list of video files, and if their duration (in seconds) is larger than 4, then those videos are moved to a new folder. This saved me so much time when trying to comb through 3 hours worth of content for a YouTube video! 
