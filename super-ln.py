import os
import sys

def scan_directory(source_dir, dest_dir, offset):
    print("Enter " + source_dir + offset)
    for path in os.listdir(source_dir + offset):
        off = offset + "/" + path
        if os.path.isdir(source_dir + off):
            try:
                print("mkdir " + dest_dir + off)
                os.mkdir(dest_dir + off)
            except:
                print("Folder already exists")
            scan_directory(source_dir, dest_dir, off)
        else:
            try:
                print("ln " + source_dir + off + " " + dest_dir + off)
                os.link(source_dir + off, dest_dir + off)
            except:
                print("File already linked")

def die():
    print("usage:\n\t" + sys.argv[0] + " [SOURCE DIRECTORY] [TARGET DIRECTORY]\n\tTarget base dir must already exist.")
    sys.exit()
    
try:
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    if not os.path.isdir(source_dir) or not os.path.isdir(dest_dir):
        die()
    else:
        scan_directory(source_dir, dest_dir, "")
except:
    die()
