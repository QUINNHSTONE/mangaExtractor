import subprocess
import re

import sys

import requests
import os
from bs4 import BeautifulSoup
from PIL import Image

def install(package):
    subprocess.call([sys.executable, '-m', 'pip', 'install', package])

def getManga(manga, link, chapter_start, chapter_end):
    print("-------------------starting download sequence---------------------")
    # Making a GET request
    chapter = chapter_start
    parentlink = link
    directory = manga
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    while(chapter <= chapter_end):
        print(chapter)
        nextlink =  parentlink + "/chapter-" + str(chapter)
        print(nextlink)
        r = requests.get(parentlink + "/chapter-" + str(chapter))
        soup = BeautifulSoup(r.content, "html.parser")

        # check status code for response received
        # success code - 200
        print(r)

        content = soup.find_all("img")

        pdfpath = os.path.join(directory , os.path.basename("chapter-" + str(chapter) + ".pdf")) 

        page = 1

        for img in content:
            link = img['src']
            if link.startswith("https"):
                # print (link) 
                pagerequest = requests.get(link)
                filename = os.path.join(directory , os.path.basename(str(page)+".jpg"))
                # Save the image content to a file
                if not os.path.exists(directory):
                    os.makedirs(directory)
                with open(filename, 'wb') as f:
                    f.write(pagerequest.content)
                    print(f"Image {filename} downloaded successfully.")
                    page = page + 1
                    

        # Get a list of all files in the directory
        files = os.listdir(directory)

        # Filter out only the files that end with ".jpg"
        jpg_files = [f for f in files if f.endswith(".jpg")]
        jpg_files_sorted = sorted(jpg_files, key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

        # print(jpg_files_sorted)
        # Open each jpg file and store them in a list
        images = [Image.open(os.path.join(directory, f)) for f in jpg_files_sorted]

        #save to PDF
        images[0].save(
            pdfpath, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
        )

        for jpg_file in jpg_files:
            file_path = os.path.join(directory, jpg_file)
            os.remove(file_path)
            # print(f"Deleted: {file_path}")

        chapter = chapter + 1

            

def main(args):
    manga = args[0]
    link = args[1]
    chapter_start = int(args[2])
    chapter_end = int(args[3])
    getManga(manga, link, chapter_start, chapter_end)


if __name__ == "__main__":
    packages = ["requests", "os", "bs4", "pillow", "re", "subprocess", "sys"]
    for package in packages:
        install(package)    
    main(sys.argv[1:])

