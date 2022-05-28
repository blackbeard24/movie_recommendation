import os, random

#Path to the directory of movies
path = "/path/to/the/movie/directory"
dirs = os.listdir(path)

l = len(dirs)

#Random numbers from 0 to len(dirs)
rec = random.randrange(l+1)

print("Today you can watch:-\n",dirs[rec])
