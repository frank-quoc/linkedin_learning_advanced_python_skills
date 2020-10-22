#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil # set of utilities for manipulating files
from shutil import make_archive
from zipfile import ZipFile # can pick and choose what to compress

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dst) # only copies file content
    # shutil.copystat(src, dst) # copies metadata as well
    
    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip: # with keyword creates a local scope that simplifies working w/ obj
      newzip.write("textfile.txt") # just add these two files to archive
      newzip.write("texfile.txt.bak")
      
if __name__ == "__main__":
  main()
