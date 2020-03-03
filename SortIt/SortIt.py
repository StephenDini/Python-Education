# This can organize/move files.
# and in the future maintain a storage drive's structure
#
# It will organize Video files into
# Videos > Movies > Genre > SHOW NAME
# Videos > Tv Shows > Genre > SHOW NAME
# Videos > Anime > Genre > SHOW NAME
from pathlib import Path
import imdb 

# Movie database initializing
movieDatabase = imdb.IMDb()

# Video Directory(ies)

# Main Folder to organize into. First run it will organize this folder.
videoMain = ""


# Folder(s) to import and organize into videoMain.
# if blank it will just organize the videoMain
importFolders = ""

# Organization

# Index all files.

# Check if a database exists,
#   Check if new files,
#       Update
# Else scrape file information and save into a database

# Create new Folders if not already there. [Movies, TV Shows, Anime, etc.]

# organize based on Movie, TV Show, Anime

# Organize Movies based on Genre

# Each Movie in its own folder.

# Grab Subtitles, Movie Poster, and Marquee/landscape

# Organize TV Shows based on Genre

# Each TV Show in its own folder.

# Grab Poster, Landscape

# Each episode in its own folder.

# Grab Subtiles

# Organize Anime based on Genre

# Each Show in its own folder

# Grab a Poster, Landscape
