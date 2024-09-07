Here is a personal script I use to move videos and pictures to their respective directories.

I surf the web a lot, and I collect a lot of pictures along the way. Some of them reveal what I was interested in at the time, but most of them are unrelated. I created this script to move each media file to its folder with no particular order. The files are renamed to a random string and moved to either a pics/ or vids/ folder.

- First, it tracks specific files
- Move each of them
- Rename them
- Tells how many files are left

I borrowed the string generator from this [answer](https://stackoverflow.com/a/2257449).

Warning: the script assumes the directories already exist. If they don't exist, the files are renamed to the destination folder name and they lose their file extensions.
